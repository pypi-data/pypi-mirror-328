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
__date__ = "28/08/2020"


import logging

from processview.core.manager import DatasetState, ProcessManager
from processview.core.superviseprocess import SuperviseProcess
from silx.gui import qt
from silx.io.url import DataUrl

from tomwer.core.process.edit import darkflatpatch
from tomwer.core.scan.edfscan import EDFTomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.settings import get_lbsram_path, isOnLbsram
from tomwer.core.utils.lbsram import is_low_on_memory

from ..processingstack import FIFO, ProcessingThread

_logger = logging.getLogger(__name__)


class DarkFlatPatchProcessStack(FIFO, qt.QObject):
    """Implementation of the `.AxisProcess` but having a stack for treating
    scans and making computation in threads"""

    def __init__(self, parent=None, process_id=None):
        qt.QObject.__init__(self, parent=parent)
        FIFO.__init__(self, process_id=process_id)
        self._dry_run = False

    def _process(self, data, configuration, callback=None):
        _logger.info(f"dark-flat patch stack is processing {data}")
        self._data_currently_computed = data
        assert isinstance(data, TomwerScanBase)
        self._computationThread.finished.connect(self._end_threaded_computation)

        if isOnLbsram(data) and is_low_on_memory(get_lbsram_path()) is True:
            # if computer is running into low memory on lbsram skip it
            mess = "low memory, skip dark-flat-patch reconstruction for", data.path
            _logger.processSkipped(mess)
            ProcessManager().notify_dataset_state(
                dataset=data,
                process=self,
                state=DatasetState.SKIPPED,
                details=mess,
            )
            self._end_threaded_computation()
        else:
            self._computationThread.init(data=data, configuration=configuration)
            # need to manage connect before starting it because
            ProcessManager().notify_dataset_state(
                dataset=data,
                process=self,
                state=DatasetState.ON_GOING,
                details=None,
            )
            self._computationThread.start()

    def _end_threaded_computation(self, callback=None):
        self._computationThread.finished.disconnect(self._end_threaded_computation)
        super()._end_threaded_computation(callback=callback)

    def _create_processing_thread(self, process_id=None) -> qt.QThread:
        return _DarkFlatPatchProcessingThread(process_id=process_id)


class _DarkFlatPatchProcessingThread(ProcessingThread, SuperviseProcess):
    """
    Thread use to execute the processing of dark-flat patch
    """

    def __init__(self, process_id=None):
        try:
            ProcessingThread.__init__(self, process_id=process_id)
        except TypeError:
            ProcessingThread.__init__(self)
        SuperviseProcess.__init__(self, process_id=process_id)
        self._scan = None
        self._configuration = None

    def init(self, data, configuration):
        self._scan = data
        self._configuration = configuration

    def run(self):
        # TODO: must be replace by calling the 'DarkFlatPatch' task directly
        self.sigComputationStarted.emit()
        _logger.processStarted(f"{self._scan} Start dark-flat patch")
        process = darkflatpatch.DarkFlatPatchTask(
            inputs={
                "data": self._scan,
                "configuration": self._configuration,
                "serialize_output_data": False,
            }
        )
        try:
            process.run()
        except Exception as e:
            info = f"Fail to patch dark-flat for {self._scan}. Reason is {e}"
            _logger.processFailed(info)
            ProcessManager().notify_dataset_state(
                dataset=self._scan,
                process=self,
                state=DatasetState.FAILED,
                details=info,
            )
            return

        index = self._scan.pop_process_index()
        if isinstance(self._scan, EDFTomoScan):
            entry = None
        else:
            entry = self._scan.entry
        configuration_to_dump = self._configuration
        keys = list(configuration_to_dump.keys())
        for key in keys:
            if isinstance(configuration_to_dump[key], DataUrl):
                configuration_to_dump[key] = configuration_to_dump[key].path()

        with self._scan.acquire_process_file_lock():

            try:
                darkflatpatch.DarkFlatPatchTask._register_process(
                    process_file=self._scan.process_file,
                    entry=entry,
                    configuration=configuration_to_dump,
                    results={},
                    process=darkflatpatch.DarkFlatPatchTask,
                    process_index=index,
                    overwrite=True,
                )
            except Exception as e:
                _logger.warning(
                    f"Fail to register DarkFlatPatch process. Reason is {e}"
                )
        info = f"Dark-flat patched for {self._scan}."
        _logger.processSucceed(info)
        ProcessManager().notify_dataset_state(
            dataset=self._scan,
            process=self,
            state=DatasetState.SUCCEED,
            details=info,
        )
