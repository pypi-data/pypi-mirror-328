# coding: utf-8
# /*##########################################################################
# Copyright (C) 2016 European Synchrotron Radiation Facility
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
Utils for slurm
"""

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "11/10/2021"


import uuid
from datetime import datetime

from sluurp.utils import has_sbatch_available


def is_slurm_available() -> bool:
    """
    Return True if the environment knows about slurm command (sbatch)
    """
    return has_sbatch_available()


def get_slurm_script_name(prefix="") -> str:
    now_str = str(datetime.now()).replace(" ", "_")
    if prefix in ("", None):
        return str(uuid.uuid4()).split("-")[0] + f"_{now_str}.sh"
    else:
        return f"{prefix}_" + str(uuid.uuid4()).split("-")[0] + f"_{now_str}.sh"
