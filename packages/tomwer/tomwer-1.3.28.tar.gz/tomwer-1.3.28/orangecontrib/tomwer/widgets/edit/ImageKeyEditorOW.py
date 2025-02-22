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
__date__ = "28/10/2020"


import logging

from orangewidget import gui
from orangewidget.widget import Input, Output

import tomwer.core.process.edit.imagekeyeditor
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.gui.edit.imagekeyeditor import ImageKeyDialog
from tomwer.synctools.stacks.edit.imagekeyeditor import ImageKeyEditorProcessStack
from tomwer.utils import docstring

from ...orange.managedprocess import SuperviseOW
from ..utils import WidgetLongProcessing

_logger = logging.getLogger(__name__)


class ImageKeyEditorOW(SuperviseOW, WidgetLongProcessing):
    """
    Widget to define on the fly the image_key of a NXtomoScan
    """

    name = "image-key-editor"
    id = "orange.widgets.tomwer.control.ImageKeyEditorOW.ImageKeyEditorOW"
    description = "Interface to edit `image_key` of nexus files"
    icon = "icons/image_key_editor.svg"
    priority = 24
    keywords = [
        "hdf5",
        "nexus",
        "tomwer",
        "file",
        "edition",
        "NXTomo",
        "editor",
        "image key editor",
        "image-key-editor",
        "image_key",
        "image_key_control",
    ]

    want_main_area = True
    resizing_enabled = True

    ewokstaskclass = tomwer.core.process.edit.imagekeyeditor.ImageKeyEditorTask

    class Inputs:
        data = Input(name="data", type=TomwerScanBase)

    class Outputs:
        data = Output(name="data", type=TomwerScanBase)

    def __init__(self, parent=None):
        SuperviseOW.__init__(self, parent=parent)
        WidgetLongProcessing.__init__(self)
        self._scan = None
        self._processingStack = ImageKeyEditorProcessStack(
            self, process_id=self.process_id
        )
        layout = gui.vBox(self.mainArea, self.name).layout()

        self.widget = ImageKeyDialog(parent=self)
        layout.addWidget(self.widget)

        # connect signal / slot
        self.widget.sigValidated.connect(self._validateCallback)
        self._processingStack.sigComputationStarted.connect(self._startProcessing)
        self._processingStack.sigComputationEnded.connect(self._endProcessing)

    @Inputs.data
    def process(self, scan):
        if scan is None:
            return
        elif not isinstance(scan, NXtomoScan):
            _logger.error("You can only edit image keys for the HDF5 scans")
        else:
            self._scan = scan
            self.widget.setScan(scan)
            self.activateWindow()
            self.raise_()
            self.show()

    @docstring
    def reprocess(self, dataset):
        self.process(dataset)

    def getConfiguration(self):
        return {
            "modifications": self.widget.getModifications(),
        }

    def _validateCallback(self):
        if self._scan is None:
            return
        self._processingStack.add(self._scan, configuration=self.getConfiguration())
        self.accept()

    def _endProcessing(self, scan, future_tomo_obj):
        WidgetLongProcessing._endProcessing(self, scan)
        if scan is not None:
            self.Outputs.data.send(scan)
