# coding: utf-8
###########################################################################
# Copyright (C) 2016-2019 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#############################################################################

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "03/05/2019"


import functools
import logging

from processview.core.manager import DatasetState, ProcessManager
from processview.core.superviseprocess import SuperviseProcess
from silx.gui import qt

from tomwer.core.process.reconstruction.axis import AxisTask
from tomwer.core.process.reconstruction.axis.axis import NoAxisUrl
from tomwer.core.process.reconstruction.axis.mode import AxisMode
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.settings import get_lbsram_path, isOnLbsram
from tomwer.core.utils.lbsram import is_low_on_memory
from tomwer.synctools.axis import QAxisRP

from ..processingstack import FIFO, ProcessingThread

_logger = logging.getLogger(__name__)


class AxisProcessStack(FIFO, qt.QObject):
    """Implementation of the `.AxisProcess` but having a stack for treating
    scans and making computation in threads"""

    def __init__(self, axis_params, process_id=None):
        qt.QObject.__init__(self)
        FIFO.__init__(self, process_id=process_id)
        assert axis_params is not None
        self._axis_params = axis_params

    def _process(self, data, configuration, callback=None):
        ProcessManager().notify_dataset_state(
            dataset=data,
            process=self,
            state=DatasetState.ON_GOING,
        )
        assert isinstance(data, TomwerScanBase)
        if data.axis_params is None:
            data.axis_params = QAxisRP()
        self._data_currently_computed = data
        self._axis_params.frame_width = data.dim_1
        mode = self._axis_params.mode
        if isOnLbsram(data) and is_low_on_memory(get_lbsram_path()) is True:
            # if computer is running into low memory on lbsram skip it
            mess = "low memory, skip axis calculation", data.path
            ProcessManager().notify_dataset_state(
                dataset=data, process=self._process_id, state=DatasetState.SKIPPED
            )
            _logger.processSkipped(mess)
            data.axis_params.set_relative_value(None)
            if callback is not None:
                callback()
            self.scan_ready(scan=data)
        elif not self._axis_params.use_sinogram and mode in (
            AxisMode.manual,
            AxisMode.read,
        ):
            # if cor is not set then set it to 0 (can be the case if no)
            # interaction has been dne
            cor = self._axis_params.relative_cor_value
            if cor is None:
                cor = 0
            data._axis_params.set_relative_value(cor)
            cor = data._axis_params.relative_cor_value
            if isinstance(data, NXtomoScan):
                entry = data.entry
            else:
                entry = "entry"
            try:
                with data.acquire_process_file_lock():
                    AxisTask._register_process(
                        process_file=data.process_file,
                        entry=entry,
                        process=AxisTask,
                        results={"center_of_rotation": cor if cor is not None else "-"},
                        configuration=self._axis_params.to_dict(),
                        process_index=data.pop_process_index(),
                        overwrite=True,
                    )
            except Exception as e:
                _logger.warning(f"Fail to register Axis process. Reason is {e}")
            # If mode is read or manual the position_value is not computed and
            # we will keep the actual one (should have been defined previously)
            self._end_computation(data=data, future_tomo_obj=None, callback=callback)

        elif (
            not self._axis_params.use_sinogram
            and mode not in AxisTask._CALCULATIONS_METHODS
        ):
            _logger.warning(f"no method defined to compute {mode}")
            if callback is not None:
                callback()
            self._process_next()
        else:
            _logger.processStarted(
                f"Start cor calculation on {data} ({self._axis_params.get_simple_str()})"
            )
            data.axis_params.set_relative_value("...")
            self._axis_params.set_relative_value("...")
            assert self._axis_params.relative_cor_value == "..."
            self._data_currently_computed = data
            self._computationThread.init(data=data, axis_params=configuration)
            fct_callback = functools.partial(self._end_threaded_computation, callback)
            self._computationThread.finished.connect(fct_callback)
            self._computationThread.start()

    def _end_computation(self, data, future_tomo_obj, callback):
        """
        callback when the computation thread is finished

        :param scan: pass if no call to '_computationThread is made'
        """
        assert isinstance(data, TomwerScanBase)
        assert self._axis_params is not None
        # copy result computed on scan on the AxisProcess reconsparams
        self._axis_params.set_relative_value(
            data.axis_params.relative_cor_value
        )  # noqa
        self._axis_params.frame_width = data.dim_1
        FIFO._end_computation(
            self, data=data, future_tomo_obj=future_tomo_obj, callback=callback
        )

    def _end_threaded_computation(self, callback=None):
        assert self._data_currently_computed is not None
        self._axis_params.set_relative_value(self._computationThread.center_of_rotation)
        self._computationThread.finished.disconnect()
        if callback:
            callback()
        FIFO._end_threaded_computation(self)

    def _create_processing_thread(self, process_id=None) -> qt.QThread:
        return _ProcessingThread(process_id=process_id)


class _ProcessingThread(ProcessingThread, SuperviseProcess):
    """
    Thread use to execute the processing of the axis position
    """

    def __init__(self, process_id=None):
        SuperviseProcess.__init__(self, process_id=process_id)
        try:
            ProcessingThread.__init__(self, process_id=process_id)
        except TypeError:
            ProcessingThread.__init__(self)
        self.center_of_rotation = None
        self._scan = None
        self._axis_params = None
        """function pointer to know which function to call for the axis
        calculation"""
        self.__patch = {}
        """Used to patch some calculation method (for test purpose)"""

    def init(self, data, axis_params):
        self._scan = data
        self._axis_params = axis_params

    def run(self):
        self.sigComputationStarted.emit()
        axis = AxisTask(
            inputs={
                "data": self._scan,
                "axis_params": self._axis_params,
                "serialize_output_data": False,
            },
            process_id=self.process_id,
        )
        axis = self.apply_patch(axis=axis)
        try:
            axis.run()
        except NoAxisUrl as e:
            self.center_of_rotation = None
            _logger.error(str(e))
        except Exception as e:
            _logger.error(str(e))
            self.center_of_rotation = None
        else:
            self.center_of_rotation = self._scan.axis_params.relative_cor_value

    def patch_calc_method(self, mode, function):
        self.__patch[mode] = function

    def apply_patch(self, axis):
        for mode, patch_fct in self.__patch.items():
            if mode in AxisMode:
                axis._CALCULATIONS_METHODS[mode] = patch_fct
        return axis
