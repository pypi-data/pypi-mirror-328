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

__authors__ = [
    "H. Payno",
]
__license__ = "MIT"
__date__ = "12/07/2022"

import logging

from orangewidget import gui
from orangewidget.settings import Setting
from orangewidget.widget import Input, Output, OWBaseWidget
from silx.gui import qt

import tomwer.core.process.control.volumeselector
from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.volume.volumebase import TomwerVolumeBase
from tomwer.gui.control.volumeselectorwidget import VolumeSelectorWidget

logger = logging.getLogger(__name__)


class VolumeSelectorOW(OWBaseWidget, openclass=True):
    name = "volume selector"
    id = "orange.widgets.tomwer.volumeselector"
    description = (
        "List all received volumes. Then user can select a specific"
        "volume to be passed to the next widget."
    )
    icon = "icons/volumeselector.svg"
    priority = 62
    keywords = ["tomography", "selection", "tomwer", "volume"]

    ewokstaskclass = (
        tomwer.core.process.control.volumeselector._VolumeSelectorPlaceHolder
    )

    want_main_area = True
    want_control_area = False
    resizing_enabled = True

    _scanIDs = Setting(list())

    class Inputs:
        volume = Input(name="volume", type=TomwerVolumeBase, multiple=True)

    class Outputs:
        volume = Output(name="volume", type=TomwerVolumeBase)

    def __init__(self, parent=None):
        """ """
        super().__init__(parent)

        self.widget = VolumeSelectorWidget(parent=self)
        self._loadSettings()

        self.widget.sigUpdated.connect(self._updateSettings)
        self.widget.sigSelectionChanged.connect(self.changeSelection)
        layout = gui.vBox(self.mainArea, self.name).layout()
        layout.addWidget(self.widget)
        # expose API
        self.setActiveScan = self.widget.setActiveData
        self.selectAll = self.widget.selectAll
        self.add = self.widget.add

    @Inputs.volume
    def _volumeReceived(self, volume, *args, **kwargs):
        self.addVolume(volume)

    def addVolume(self, volume):
        if volume is not None:
            self.widget.add(volume)

    def removeVolume(self, volume):
        if volume is not None:
            self.widget.remove(volume)

    def changeSelection(self, list_volume):
        if list_volume:
            for volume_id in list_volume:
                volume = self.widget.dataList.getVolume(volume_id, None)
                if volume is not None:
                    assert isinstance(volume, TomwerVolumeBase)
                    self.Outputs.volume.send(volume)
                else:
                    logger.error(f"{volume_id} not found the list")

    def send(self):
        """send output signals for each selected items"""
        sItem = self.widget.dataList.selectedItems()
        if sItem and len(sItem) >= 1:
            selection = [_item.text() for _item in sItem]
            self.changeSelection(list_volume=selection)

    def _loadSettings(self):
        for scan in self._scanIDs:
            assert isinstance(scan, str)
            # kept for backward compatibility since 0.11. To be removed on the future version.
            if "@" in scan:
                entry, file_path = scan.split("@")
                nxtomo_scan = NXtomoScan(entry=entry, scan=file_path)
                self.addVolume(nxtomo_scan)
            else:
                self.addVolume(scan)

    def _updateSettings(self):
        self._scanIDs = []
        for scan in self.widget.dataList._myitems:
            self._scanIDs.append(scan)

    def keyPressEvent(self, event):
        """
        To shortcut orange and make sure the `delete` key will be interpreted we need to overwrite this function
        """
        if event.key() == qt.Qt.Key_Delete:
            self.widget._callbackRemoveSelectedDatasets()
        else:
            super().keyPressEvent(event)
