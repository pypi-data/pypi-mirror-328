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
__date__ = "02/09/2020"


import shutil
import tempfile
import unittest

from tomoscan.io import HDF5File, get_swmr_mode

from tomwer.core.process.task import Task
from tomwer.core.utils.scanutils import MockNXtomo


class TestProcessRegistration(unittest.TestCase):
    """
    Make sure utils link to the process registration are
    correctly working
    """

    class DummyProcess(Task):
        @staticmethod
        def program_name():
            """Name of the program used for this processing"""
            return "dummy program"

        @staticmethod
        def program_version():
            """version of the program used for this processing"""
            return "0.0.0"

        @staticmethod
        def definition():
            """definition of the process"""
            return "no definition"

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.scan = MockNXtomo(scan_path=self.tmp_dir, n_proj=2).scan

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def testGetCorValues(self):
        from tomwer.core.process.reconstruction.axis import AxisTask

        for i in range(20):
            results = {"center_of_rotation": i}
            Task._register_process(
                self.scan.process_file,
                process=AxisTask,
                entry=self.scan.entry,
                configuration=None,
                results=results,
                process_index=i,
            )
        cor_value = AxisTask.get_cor_frm_process_file(
            self.scan.process_file, entry=self.scan.entry
        )
        self.assertEqual(cor_value, 19)

    def testGetProcessNodes(self):
        """insure it return the last dark process based on the processing index"""

        for i in range(20):
            Task._register_process(
                self.scan.process_file,
                process=self.DummyProcess,
                entry=self.scan.entry,
                configuration=None,
                results={"output": i},
                process_index=i,
            )

        with HDF5File(self.scan.process_file, "r", swmr=get_swmr_mode()) as h5f:
            nodes = Task._get_process_nodes(
                root_node=h5f[self.scan.entry], process=self.DummyProcess
            )
            self.assertEqual(len(nodes), 20)
            self.assertTrue("/entry/tomwer_process_16" in nodes)
            self.assertEqual(nodes["/entry/tomwer_process_16"], 16)
            self.assertTrue("/entry/tomwer_process_1" in nodes)
            self.assertEqual(nodes["/entry/tomwer_process_1"], 1)
