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
__date__ = "04/11/2021"


import asyncio
import os

from tomwer.core.futureobject import FutureTomwerObject
from tomwer.core.utils.scanutils import MockNXtomo


def test_simple_future_tomo_obj(tmpdir):
    """Simple test of the FutureTomwerScan API"""
    scan = MockNXtomo(
        scan_path=os.path.join(tmpdir, "scan_test"),
        n_proj=10,
        n_ini_proj=10,
        create_ini_dark=False,
        create_ini_flat=False,
        dim=10,
    ).scan
    future = asyncio.Future()
    future.set_result(None)

    future_tomo_obj = FutureTomwerObject(
        tomo_obj=scan,
        futures=[
            future,
        ],
    )

    future_tomo_obj.results()
    assert future_tomo_obj.exceptions() is None
    assert future_tomo_obj.cancelled() is False
