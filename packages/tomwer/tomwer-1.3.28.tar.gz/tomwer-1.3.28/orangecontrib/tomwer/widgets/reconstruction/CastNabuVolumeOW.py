# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "15/12/2021"

import logging
from typing import Optional

from orangewidget import gui
from orangewidget.settings import Setting
from orangewidget.widget import Input, Output
from processview.core.manager.manager import DatasetState, ProcessManager
from silx.gui import qt

import tomwer.core.process.reconstruction.nabu.castvolume
from orangecontrib.tomwer.widgets.utils import WidgetLongProcessing
from tomwer.core import settings
from tomwer.core.cluster.cluster import SlurmClusterConfiguration
from tomwer.core.futureobject import FutureTomwerObject
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.utils.lbsram import is_low_on_memory
from tomwer.core.volume.volumebase import TomwerVolumeBase
from tomwer.gui.reconstruction.nabu.castvolume import CastVolumeWidget
from tomwer.synctools.stacks.reconstruction.castvolume import CastVolumeProcessStack
from tomwer.utils import docstring

from ...orange.managedprocess import SuperviseOW

_logger = logging.getLogger(__name__)


class CastNabuVolumeOW(WidgetLongProcessing, SuperviseOW):
    """
    widget used to cast from 32 bits tiff to 16 bits tiff.

    This is done in a separate process because:

    * this is done in cpu when nabu reconstruct on GPU and this should free sooner GPU ressources with the current architecture.
    * this is not included in nabu but also done as post processing.
    * limitation is that not having computed the histogram during volume construction will slow down the cast

    :param parent: the parent widget
    """

    # note of this widget should be the one registered on the documentation
    name = "cast volume"
    id = "orange.widgets.tomwer.reconstruction.CastNabuVolumeOW.CastNabuVolumeOW"
    description = "This widget will allow to cast a nabu volume data type / format to another one."
    icon = "icons/nabu_cast.svg"
    priority = 60
    keywords = [
        "tomography",
        "nabu",
        "reconstruction",
        "volume",
        "cast",
        "tiff",
        "32 bits",
        "16 bits",
        "tif",
    ]

    ewokstaskclass = tomwer.core.process.reconstruction.nabu.castvolume.CastVolumeTask

    want_main_area = True
    resizing_enabled = True

    _ewoks_default_inputs = Setting({"data": None, "cast_volume_params": {}})

    sigScanReady = qt.Signal(TomwerScanBase)
    "Signal emitted when a scan is ended"

    TIMEOUT = 30

    class Inputs:
        data = Input(
            name="data",
            type=TomwerScanBase,
            doc="one scan to be process",
            default=True,
            multiple=False,
        )

        volume = Input(
            name="volume",
            type=TomwerVolumeBase,
            doc="volume to be process",
            default=False,
            multiple=False,
        )
        cluster_in = Input(
            name="cluster_config",
            type=SlurmClusterConfiguration,
            doc="slurm cluster to be used",
            multiple=False,
        )

    class Outputs:
        data = Output(name="data", type=TomwerScanBase, doc="one scan to be process")
        volume = Output(name="volume", type=TomwerVolumeBase, doc="raw volume")
        cast_volume = Output(
            name="cast volume", type=TomwerVolumeBase, doc="cast volume"
        )
        future_tomo_obj = Output(
            name="future_tomo_obj",
            type=FutureTomwerObject,
            doc="future object (process remotely)",
        )

    def __init__(self, parent=None):
        """ """
        SuperviseOW.__init__(self, parent)
        WidgetLongProcessing.__init__(self)
        self._slurmCluster = None
        # processing tool
        self._processingStack = CastVolumeProcessStack(process_id=self.process_id)
        self._window = CastVolumeWidget(parent=self)

        self._layout = gui.vBox(self.mainArea, self.name).layout()
        self._layout.setContentsMargins(0, 0, 0, 0)

        self._layout.addWidget(self._window)

        cast_volume_params = self._ewoks_default_inputs.get("cast_volume_params", {})
        self.setConfiguration(cast_volume_params)

        # connect signal / slot
        self._window.sigConfigChanged.connect(self._updateConfig)
        self._processingStack.sigComputationStarted.connect(self._startProcessing)
        self._processingStack.sigComputationEnded.connect(self._endProcessing)

    def __new__(cls, *args, **kwargs):
        # ensure backward compatibility with 'static_input'
        static_input = kwargs.get("stored_settings", {}).get("static_input", None)
        if static_input not in (None, {}):
            _logger.warning(
                "static_input has been deprecated. Will be replaced by _ewoks_default_inputs in the workflow file. Please save the workflow to apply modifications"
            )
            kwargs["stored_settings"]["_ewoks_default_inputs"] = static_input
        return super().__new__(cls, *args, **kwargs)

    @Inputs.data
    def process_data(self, scan: Optional[TomwerScanBase]):
        self._process_data(scan)

    def _process_data(self, scan: Optional[TomwerScanBase]):
        if scan is None:
            return
        if not isinstance(scan, TomwerScanBase):
            raise TypeError(
                f"scan is expected to be an instance of {TomwerScanBase} not {type(scan)}"
            )
        if (
            settings.isOnLbsram(scan)
            and is_low_on_memory(settings.get_lbsram_path()) is True
        ):
            ProcessManager().notify_dataset_state(
                dataset=scan,
                process=self,
                state=DatasetState.SKIPPED,
            )
            _logger.processSkipped(
                f"skip volume cast for {str(scan)} because lbsram is almost full. Try to free it"
            )
            self.Outputs.data.send(scan)
        else:
            self._processingStack.add(scan, configuration=self.getConfiguration())

    @docstring
    def reprocess(self, dataset):
        if isinstance(dataset, TomwerScanBase):
            self._process_data(dataset)
        elif isinstance(dataset, TomwerVolumeBase):
            self._process_volume(dataset)
        else:
            raise TypeError("dataset is expected to be an instance of ''")

    @Inputs.cluster_in
    def setCluster(self, slurm_cluster: Optional[SlurmClusterConfiguration]):
        assert isinstance(
            slurm_cluster, (type(None), SlurmClusterConfiguration)
        ), f"Expect None of SlurmClusterConfiguration. Not {type(slurm_cluster)}"
        self._slurmCluster = slurm_cluster

    @Inputs.volume
    def process_volume(self, volume: Optional[TomwerVolumeBase]):
        self._process_volume(volume)

    def _process_volume(self, volume: Optional[TomwerVolumeBase]):
        if volume is None:
            return
        if not isinstance(volume, TomwerVolumeBase):
            raise TypeError(
                f"volume is expected to be an instance of {TomwerVolumeBase} not {type(volume)}"
            )
        else:
            self._processingStack.add(volume, configuration=self.getConfiguration())

    def getConfiguration(self) -> dict:
        config = self._window.getConfiguration()
        config["cluster_config"] = self._slurmCluster
        return config

    def setConfiguration(self, configuration: dict) -> None:
        self._window.setConfiguration(configuration)

    def _updateConfig(self):
        self._ewoks_default_inputs = {
            "data": None,
            "cast_volume_params": self.getConfiguration(),
        }

    def _endProcessing(self, obj, future_tomo_obj):
        WidgetLongProcessing._endProcessing(self, obj)
        if future_tomo_obj is not None:
            self.Outputs.future_tomo_obj.send(future_tomo_obj)
        if obj is not None:
            if isinstance(obj, TomwerScanBase):
                self.Outputs.data.send(obj)
            elif isinstance(obj, TomwerVolumeBase):
                self.Outputs.volume.send(obj)
            # for now we store a cast_volume to the object but this is not very well design.
            # I guess this will be removed once we move to ewoks or we need to redesign the stack approach
            if obj.cast_volume is not None:
                self.Outputs.cast_volume.send(obj.cast_volume)
