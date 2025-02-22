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
__date__ = "12/12/2018"


import logging
import time

from tomwer.core.process.task import Task
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.utils.scanutils import data_identifier_to_scan
from tomwer.core.utils.deprecation import deprecated_warning, deprecated

_logger = logging.getLogger(__name__)


class TimerTask(
    Task,
    input_names=("data", "wait"),
    output_names=("data",),
    optional_input_names=("serialize_output_data",),
):
    """
    Simple timer / time out - function
    """

    def __init__(
        self, varinfo=None, inputs=None, node_id=None, node_attrs=None, execinfo=None
    ):
        Task.__init__(
            self,
            varinfo=varinfo,
            inputs=inputs,
            node_id=node_id,
            node_attrs=node_attrs,
            execinfo=execinfo,
        )
        if inputs is None:
            inputs = {}

    @property
    @deprecated(replacement="task.wait", since_version="1.2")
    def waiting_time(self):
        return self.inputs.wait

    @waiting_time.setter
    @deprecated(replacement="task.wait", since_version="1.2")
    def waiting_time(self, wait):
        self.inputs.wait = wait

    def run(self):
        scan = data_identifier_to_scan(self.inputs.data)
        if type(scan) is dict:
            scan = ScanFactory.create_scan_object_frm_dict(scan)
        else:
            scan = scan
        if not isinstance(scan, TomwerScanBase):
            raise TypeError(
                f"scan is expected to be a dict or an instance of TomwerScanBase. Not {type(scan)}"
            )
        time.sleep(self.inputs.wait)
        if self.get_input_value("serialize_output_data", True):
            self.outputs.data = scan.to_dict()
        else:
            self.outputs.data = scan


class Timer(TimerTask):
    def __init__(
        self, varinfo=None, inputs=None, node_id=None, node_attrs=None, execinfo=None
    ):
        deprecated_warning(
            name="tomwer.core.process.control.timer.Timer",
            type_="class",
            reason="improve readibility",
            since_version="1.2",
            replacement="TimerTask",
        )
        super().__init__(varinfo, inputs, node_id, node_attrs, execinfo)
