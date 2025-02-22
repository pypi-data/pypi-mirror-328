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
__date__ = "02/11/2020"


import logging
from typing import Optional

from orangewidget import gui
from orangewidget.settings import Setting
from orangewidget.widget import Input, Output
from silx.io.url import DataUrl

import tomwer.core.process.edit.darkflatpatch
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.gui.edit.dkrfpatch import DarkRefPatchWidget
from tomwer.synctools.stacks.edit.darkflatpatch import DarkFlatPatchProcessStack
from tomwer.utils import docstring

from ...orange.managedprocess import SuperviseOW
from ..utils import WidgetLongProcessing

_logger = logging.getLogger(__name__)


class DarkFlatPatchOW(WidgetLongProcessing, SuperviseOW):
    """
    Widget to define on the fly the image_key of a NXtomoScan
    """

    name = "dark-flat-patch"
    id = "orange.widgets.tomwer.edit.DarkFlatPatchOW.DarkFlatPatchOW"
    description = "Interface to patch dark and flat to an existing NXTomo" "entry"
    icon = "icons/patch_dark_flat.svg"
    priority = 25
    keywords = [
        "hdf5",
        "nexus",
        "tomwer",
        "file",
        "edition",
        "NXTomo",
        "editor",
        "dark",
        "patch",
        "ref",
        "flat",
    ]

    want_main_area = True
    resizing_enabled = True

    _urlsSetting = Setting(dict())

    ewokstaskclass = tomwer.core.process.edit.darkflatpatch.DarkFlatPatchTask

    class Inputs:
        data = Input(name="data", type=TomwerScanBase)
        config_in = Input(name="configuration", type=dict)

    class Outputs:
        data = Output(name="data", type=TomwerScanBase)

    def __init__(self, parent=None):
        SuperviseOW.__init__(self, parent=parent)
        WidgetLongProcessing.__init__(self)
        layout = gui.vBox(self.mainArea, self.name).layout()
        self._processingStack = DarkFlatPatchProcessStack(
            self, process_id=self.process_id
        )

        self.widget = DarkRefPatchWidget(parent=self)
        layout.addWidget(self.widget)

        self.setConfiguration(self._urlsSetting)

        # connect signal / slot
        self._processingStack.sigComputationStarted.connect(self._startProcessing)
        self._processingStack.sigComputationEnded.connect(self._endProcessing)
        self.widget.sigConfigurationChanged.connect(self._updateSettings)

    @Inputs.data
    def process(self, scan):
        if scan is None:
            return
        elif not isinstance(scan, NXtomoScan):
            _logger.error("We can only patch dark and flat for NXtomoScan")
        else:
            self._processingStack.add(scan, self.getConfiguration())

    @docstring(SuperviseOW)
    def reprocess(self, dataset):
        self.process(dataset)

    def getConfiguration(self):
        def cast_url_to_str(url: Optional[DataUrl]):
            if url is None:
                return None
            elif not isinstance(url, DataUrl):
                raise TypeError(
                    f"url is expected to be an optional DataUrl. {type(url)} provided instead"
                )
            else:
                return url.path()

        return {
            "darks_start": cast_url_to_str(self.widget.getStartDarkUrl()),
            "flats_start": cast_url_to_str(self.widget.getStartFlatUrl()),
            "darks_end": cast_url_to_str(self.widget.getEndDarkUrl()),
            "flats_end": cast_url_to_str(self.widget.getEndFlatUrl()),
        }

    @Inputs.config_in
    def setConfiguration(self, config):
        if config is None:
            return
        self.widget.clear()
        url_keys = ("darks_start", "flats_start", "darks_end", "flats_end")
        url_index_keys = (
            "darks_start_index",
            "flats_start_index",
            "darks_end_index",
            "flats_end_index",
        )
        setters = (
            self.widget.setStartDarkUrl,
            self.widget.setStartFlatUrl,
            self.widget.setEndDarkUrl,
            self.widget.setEndFlatUrl,
        )
        for url_key, url_idx_key, setter in zip(url_keys, url_index_keys, setters):
            if url_key in config:
                index = config.get(url_idx_key, 0)
                url = config[url_key]
                if url not in (None, ""):
                    try:
                        setter(url=url, serie_index=index)
                    except Exception as e:
                        _logger.error(e)

    def _endProcessing(self, scan, future_tomo_obj):
        WidgetLongProcessing._endProcessing(self, scan)
        if scan is not None:
            self.Outputs.data.send(scan)

    def _updateSettings(self):
        self._urlsSetting = self.getConfiguration()
        self._urlsSetting.update(
            {
                "darks_start_index": self.widget.getStartDarkIndex(),
                "flats_start_index": self.widget.getStartFlatIndex(),
                "darks_end_index": self.widget.getEndDarkIndex(),
                "flats_end_index": self.widget.getEndFlatIndex(),
            }
        )
