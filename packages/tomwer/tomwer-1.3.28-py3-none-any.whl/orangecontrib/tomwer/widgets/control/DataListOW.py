# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2021 European Synchrotron Radiation Facility
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

__authors__ = ["C. Nemoz", "H. Payno"]
__license__ = "MIT"
__date__ = "01/12/2016"

import logging

from orangewidget import gui
from orangewidget.settings import Setting
from orangewidget.widget import Input, Output, OWBaseWidget
from silx.gui import qt

import tomwer.core.process.control.scanlist
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.gui.control.datalist import GenericScanListWindow

logger = logging.getLogger(__name__)


class DataListOW(OWBaseWidget, openclass=True):
    name = "scan list"
    id = "orange.widgets.tomwer.scanlist"
    description = "List path to reconstructions/scans. Those path will be send to the next box once validated."
    icon = "icons/scanlist.svg"
    priority = 50
    keywords = ["tomography", "file", "tomwer", "folder"]

    want_main_area = True
    want_control_area = False
    resizing_enabled = True

    _scanIDs = Setting(list())

    ewokstaskclass = tomwer.core.process.control.scanlist._ScanListPlaceHolder

    class Outputs:
        data = Output(name="data", type=TomwerScanBase, doc="one scan to be process")

    class Inputs:
        data = Input(name="data", type=TomwerScanBase, multiple=True)

    def __init__(self, parent=None):
        """A simple annuary which register all folder containing completed scan

        .. warning: the widget won't check for scan validity and will only
            emit the path to folders to the next widgets

        :param parent: the parent widget
        """
        super().__init__(parent)

        self.widget = GenericScanListWindow(parent=self)
        self.widget.setWindowFlags(qt.Qt.Widget)
        self.widget.sigUpdated.connect(self._updateSettings)
        self._loadSettings()
        layout = gui.vBox(self.mainArea, self.name).layout()
        layout.addWidget(self.widget)
        self.widget._widget._sendButton.clicked.connect(self._sendList)

        # expose API
        self.n_scan = self.widget.n_scan

        # alias used for the 'simple workflow' for now
        self.start = self._sendList
        self.clear = self.widget._widget.clear

    def _sendList(self):
        """Send a signal for each list to the next widget"""
        for data_id, item in self.widget.datalist._myitems.items():
            logger.debug(f"sending {data_id}")
            data_obj = item.data(qt.Qt.UserRole)
            self.Outputs.data.send(data_obj)

    @Inputs.data
    def add(self, scan, *args, **kwargs):
        if scan is None:
            return

        self.widget.add(scan)

    def _loadSettings(self):
        for scan in self._scanIDs:
            assert isinstance(scan, str)
            # kept for backward compatibility since 0.11. To be removed on the future version.
            if "@" in scan:
                entry, file_path = scan.split("@")
                nxtomo_scan = NXtomoScan(entry=entry, scan=file_path)
                self.add(nxtomo_scan)
            else:
                self.add(scan)

    def _updateSettings(self):
        self._scanIDs = []
        for scan in self.widget.datalist._myitems:
            self._scanIDs.append(scan)

    def keyPressEvent(self, event):
        """
        To shortcut orange and make sure the `delete` key will be interpreted we need to overwrite this function
        """
        if event.key() == qt.Qt.Key_Delete:
            self.widget._removeSelected()
        else:
            super().keyPressEvent(event)
