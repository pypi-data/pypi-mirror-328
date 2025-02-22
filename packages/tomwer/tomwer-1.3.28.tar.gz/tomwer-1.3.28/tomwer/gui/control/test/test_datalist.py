# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2017 European Synchrotron Radiation Facility
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
__date__ = "05/11/2018"


import tempfile

import pytest
from silx.gui import qt
from silx.gui.utils.testutils import TestCaseQt

from tomwer.core.utils.scanutils import MockEDF
from tomwer.gui.control.datalist import GenericScanListDialog, VolumeList
from tomwer.tests.utils import skip_gui_test


@pytest.mark.skipif(skip_gui_test(), reason="skip gui test")
class DataListTest(TestCaseQt):
    """Test that the datalist widget work correctly"""

    def setUp(self):
        super().setUp()
        self.widget = GenericScanListDialog(parent=None)
        self.widget._callbackRemoveAllFolders()
        self.widget.clear()
        self._folders = []
        for iFolder in range(5):
            self._folders.append(tempfile.mkdtemp())
            MockEDF.mockScan(
                scanID=self._folders[-1], nRadio=5, nRecons=5, nPagRecons=0, dim=10
            )

    def tearDown(self):
        self.widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        self.widget.close()
        self.widget = None
        self._folders = None
        super().tearDown()

    def test(self):
        """simple test adding and removing folders"""
        for _folder in self._folders:
            self.widget.add(_folder)
        self.assertEqual(self.widget.n_scan(), len(self._folders))
        self.widget.remove(self._folders[0])
        self.assertEqual(self.widget.n_scan(), len(self._folders) - 1)
        self.assertTrue(self._folders[0] not in self.widget.datalist._myitems)
        self.widget.selectAll()
        self.widget._removeSelected()
        self.assertEqual(self.widget.n_scan(), 0)


@pytest.mark.skipif(skip_gui_test(), reason="skip gui test")
def TestVolumeList(TestCaseQt):
    """Test VolumeList behave as expected"""

    def setUp(self):
        super().setUp()
        self.widget = VolumeList(parent=None)
        self.folder = tempfile.mkdtemp()

    def tearDown(self):
        self.widget.setAttribute(qt.Qt.WA_DeleteOnClose)
        self.widget.close()
        self.widget = None
        self.folder = None
        super().tearDown()

    def test(self):
        raise NotImplementedError
        self.widget.show()
        self.qapp.exec_()
