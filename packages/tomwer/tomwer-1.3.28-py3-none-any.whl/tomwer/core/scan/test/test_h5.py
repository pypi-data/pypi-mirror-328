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
"""Unit test for the scan defined at the hdf5 format"""

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "16/09/2019"

import os
import shutil
import tempfile
import unittest

from tomwer.core.scan.nxtomoscan import NXtomoScan
from tomwer.core.utils.scanutils import MockNXtomo
from tomwer.tests.datasets import TomwerCIDatasets


class TestHDF5Scan(unittest.TestCase):
    """Basic test for the hdf5 scan"""

    def setUp(self) -> None:
        super(TestHDF5Scan, self).setUp()
        self._tmp_dir = tempfile.mkdtemp()
        self.dataset_file = os.path.join(self._tmp_dir, "frm_edftomomill_twoentries.nx")
        shutil.copyfile(
            TomwerCIDatasets.get_dataset(
                "h5_datasets/frm_edftomomill_twoentries.nx",
            ),
            self.dataset_file,
        )
        assert os.path.isfile(self.dataset_file)
        self.scan = NXtomoScan(scan=self.dataset_file, entry="entry0000")

    def test_scan_dir(self):
        assert self.scan.scan_dir_name() == self._tmp_dir.split(os.sep)[-1]

    def testFFInterval(self):
        """test the call to ff_interval"""
        scan_path = os.path.join(self._tmp_dir, "my_scan_1")
        scan_1 = MockNXtomo(
            scan_path=scan_path,
            n_ini_proj=20,
            n_proj=20,
            n_alignement_proj=2,
            create_final_flat=True,
            create_ini_dark=True,
            create_ini_flat=True,
            n_refs=5,
        ).scan
        self.assertEqual(scan_1.ff_interval, 20)

        scan_path2 = os.path.join(self._tmp_dir, "my_scan_2")
        scan_2 = MockNXtomo(
            scan_path=scan_path2,
            n_ini_proj=10,
            n_proj=10,
            n_alignement_proj=2,
            create_final_flat=False,
            create_ini_dark=True,
            create_ini_flat=True,
            n_refs=1,
        ).scan
        self.assertEqual(scan_2.ff_interval, 0)


def test_working_directory():
    """test behavior of the working directory function"""
    scan = NXtomoScan(scan=None, entry="my_entry")
    assert scan.working_directory is None
    scan = NXtomoScan(scan="/full/path/my_file.sh", entry="my_entry")
    assert scan.working_directory == os.path.abspath("/full/path")
    scan = NXtomoScan(scan="my_file.sh", entry="my_entry")
    assert scan.working_directory == os.path.abspath(".")
