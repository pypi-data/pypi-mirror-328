# coding: utf-8
# /*##########################################################################
# Copyright (C) 2017 European Synchrotron Radiation Facility
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
#############################################################################*/

"""
This module is used to define a set of folders to be emitted to the next box.
"""

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "05/07/2017"


import logging

from tomwer.core.process.task import Task
from tomwer.core.utils.scanutils import data_identifier_to_scan

logger = logging.getLogger(__name__)


class _ScanListPlaceHolder(
    Task, optional_input_names=("data",), output_names=("data",)
):
    """For now data can only be a single element and not a list.
    This must be looked at.
    Also when part of an ewoks graph 'data' is mandatory which is not the class
    when part of a orange workflow. Those can be added interactively"""

    def run(self):
        self.outputs.data = data_identifier_to_scan(self.inputs.data)
