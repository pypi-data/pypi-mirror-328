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

__authors__ = ["C. Nemoz", "H. Payno"]
__license__ = "MIT"
__date__ = "01/08/2018"

import logging

from orangewidget import gui, widget
from orangewidget.widget import Input

from silx.gui import qt

import tomwer.core.process.visualization.radiostack
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.gui.stacks import RadioStack

logger = logging.getLogger(__name__)


class RadioStackOW(widget.OWBaseWidget, openclass=True):
    """
    This widget will make stack radios incoming and allow user to browse into
    it.
    """

    name = "radio stack"
    id = "orange.widgets.tomwer.slicesstack.radiostack"
    description = (
        "This widget will save all scan path given to here "
        "and extract received radio files with there shortest"
        "unique basename to be able to browse them"
    )

    icon = "icons/radiosstack.svg"
    priority = 27
    keywords = ["tomography", "radio", "tomwer", "stack", "group"]

    ewokstaskclass = tomwer.core.process.visualization.radiostack._RadioStackPlaceHolder

    want_main_area = True
    want_control_area = False
    resizing_enabled = True

    class Inputs:
        data = Input(
            name="data",
            type=TomwerScanBase,
            multiple=True,
        )

    def __init__(self, parent=None):
        widget.OWBaseWidget.__init__(self, parent)
        self._box = gui.vBox(self.mainArea, self.name)
        self._viewer = RadioStack(parent=self)
        self._box.layout().addWidget(self._viewer)

    @Inputs.data
    def addLeafScan(self, scanID, *args, **kwargs):
        if scanID is None:
            return
        self._viewer.addLeafScan(scanID)

    def keyPressEvent(self, e):
        # TODO: fixme
        # here we want to avoid loading imageJ when enter is pressed.
        # the correct way would be to install an event filer
        # but this is ignored because the KeyPressEvent goes other it.
        # I don't really see why too annoyed at the point to look deeper
        if e.key() in (qt.Qt.Key_Enter, qt.Qt.Key_Return):
            pass
        else:
            super().keyPressEvent(e)
