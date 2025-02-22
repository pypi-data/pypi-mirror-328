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
__date__ = "02/06/2017"


import os
from silx.utils.enum import Enum as _Enum


__LBSRAM_PATH = '/lbsram'

__DEST_PATH = ''

MOCK_LBSRAM = False

MAX_MEM_USED = 80
"Maximal percentage of used memory from which we should skip some processing"

MAKE_OAR_PYST2_PATH = '/data/id19/inhouse/OAR_UTILITIES/pyhst/make_oar_pyhst2'
"""path to the make_oar_pyhst2 path"""

JSON_RPC_HOST = None
"""you specify an host name. If None is provided then will use HOSTNAME"""

JSON_RPC_PORT = 4000


def mock_lsbram(b):
    assert type(b) is bool
    global MOCK_LBSRAM
    MOCK_LBSRAM = b


def isOnLbsram(scan=None):
    if MOCK_LBSRAM:
        return True
    elif scan is None:
        return os.path.isdir(get_lbsram_path())
    else:
        if isinstance(scan, str):
            return os.path.abspath(scan).startswith(__LBSRAM_PATH)
        else:
            return os.path.abspath(scan.path).startswith(__LBSRAM_PATH)


def get_lbsram_path():
    return __LBSRAM_PATH


def get_dest_path():
    return __DEST_PATH


def _set_lbsram_path(path):
    global __LBSRAM_PATH
    __LBSRAM_PATH = path


def _set_dest_path(path):
    global __DEST_PATH
    __DEST_PATH = path


class SlurmSettingsMode(_Enum):
    MANUAL = "manual"
    GENERIC = "generic"
    CAST_VOLUME = "cast_volume"
    SLICE_RECONSTRUCTION = "slice_reconstruction"
    VOLUME_RECONSTRUCTION = "volume_reconstruction"
    STITCHING = "stitching"

    @staticmethod
    def get_settings_class(mode):
        assert isinstance(mode, SlurmSettingsMode)
        if mode is SlurmSettingsMode.MANUAL:
            return None
        elif mode is SlurmSettingsMode.GENERIC:
            return SlurmSettings
        elif mode is SlurmSettingsMode.CAST_VOLUME:
            return DefaultSlurmSettingsCastVolume
        elif mode is SlurmSettingsMode.SLICE_RECONSTRUCTION:
            return DefaultSlurmSettingsSliceReconstruction
        elif mode is SlurmSettingsMode.VOLUME_RECONSTRUCTION:
            return DefaultSlurmSettingsVolumeReconstruction
        elif mode is SlurmSettingsMode.STITCHING:
            return DefaultSlurmSettingsStitching
        else:
            raise ValueError(f"{mode} not handled")


class SlurmSettings:
    # Default slurm cluster configuration

    N_CORES_PER_TASK = 4
    """Number of CPU per worker"""

    N_TASKS = 1
    """Number of worker"""

    N_JOBS = 1
    """on how many job we want to split the EwoksTask"""

    MEMORY_PER_WORKER = 128  # memory in GB
    """Amount of memory per worker"""

    PARTITION = "p9gpu"
    """Queue / partition to use"""

    DEFAULT_WALLTIME = "01:00:00"  # None if the default wall time

    N_GPUS_PER_WORKER = 1
    """number of gpu per worker"""

    PYTHON_VENV = None
    """Python executable to take. Useful if compute nodes have a different environment from the front end.
    """

    PROJECT_NAME = "tomwer_{scan}_-_{process}_-_{info}"
    """Slurm cluster project name. `scan`, `process` and `info` will be format.
    """

    MODULES_TO_LOAD = ("tomotools/stable", )

    SBATCH_EXTRA_PARAMS = {
        "export": "NONE",  # value to provide to sbatch --export={}
    }


class DefaultSlurmSettingsCastVolume(SlurmSettings):
    """
    default proposed configuration for casting a volume remotly
    """
    N_GPUS_PER_WORKER = 0

    N_CORES_PER_TASK = 8

    MEMORY_PER_WORKER = 128  # memory in GB

    PARTITION = "nice*"


class DefaultSlurmSettingsSliceReconstruction(SlurmSettings):
    """
    default proposed configuration for reconstructing a single slice remotly
    """
    MEMORY_PER_WORKER = 256  # memory in GB

    PARTITION = None


class DefaultSlurmSettingsVolumeReconstruction(SlurmSettings):
    """
    default proposed configuration for reconstructing a full volume remotly
    """
    MEMORY_PER_WORKER = 256  # memory in GB

    PARTITION = None


class DefaultSlurmSettingsStitching(SlurmSettings):
    """*
    default proposed configuration for stitching
    """
    N_JOBS = 15

    PARTITION = "nice-long"

    N_GPUS_PER_WORKER = 0
