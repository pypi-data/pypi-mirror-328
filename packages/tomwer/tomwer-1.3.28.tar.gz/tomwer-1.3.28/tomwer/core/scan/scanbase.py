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


__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "09/08/2018"


import io
import json
import logging
import os
import typing
from glob import glob
from typing import Optional
import functools

import numpy
from silx.io.url import DataUrl
from silx.utils.enum import Enum as _Enum
from silx.io.utils import open as open_hdf5

from tomoscan.identifier import VolumeIdentifier
from tomoscan.normalization import IntensityNormalization
from tomoscan.volumebase import VolumeBase
from tomoscan.identifier import BaseIdentifier

from tomwer.core.tomwer_object import TomwerObject
from tomwer.core.utils.ftseriesutils import orderFileByLastLastModification
from tomwer.core.utils.locker import FileLockerManager
from tomwer.core.volume.edfvolume import EDFVolume
from tomwer.core.volume.hdf5volume import HDF5Volume
from tomwer.core.volume.jp2kvolume import JP2KVolume
from tomwer.core.volume.tiffvolume import TIFFVolume

logger = logging.getLogger(__name__)


class TomwerScanBase(TomwerObject):
    """
    Simple interface to extend the tomoscan.TomwerScanBase with
    specific functions
    """

    _DICT_DARK_REF_KEYS = "dark_ref_params"

    _DICT_NABU_RP_KEY = "nabu_params"

    _DICT_AXIS_KEYS = "axis_params"

    _DICT_SA_AXIS_KEYS = "sa_axis_params"

    _DICT_SA_DELTA_BETA_KEYS = "sa_delta_beta_params"

    _DICT_PROCESS_INDEX_KEY = "next_process_index"

    _DICT_NORMALIZATION_KEY = "norm_params"

    VALID_RECONS_EXTENSION = ".edf", ".npy", ".npz", ".hdf5", ".tiff", ".jp2", ".vol"

    def __init__(self, overwrite_proc_file=False):
        super().__init__()
        self._stitching_metadata = None
        self._reconstructions = []

        self._nabu_params = None
        """nabu reconstruction parameters"""
        self._axis_params = None
        """Axis parameters"""
        self._saaxis_params = None
        """Information relative to saaxis"""
        self._sa_delta_beta_params = None
        """Information regarding sa_delta_beta_params"""
        self._dark_ref_params = None
        """Information regarding dark - ref reconstruction"""
        self._process_file = None
        """file storing processes applied on the scan, with their configuration
        and result"""
        self._cache_proj_urls = None
        """cache for the projection urls"""
        self._cache_radio_axis = {}
        """cache for the radio axis. Key is tuple (mode, nearest), value is
        (url1, url2)"""
        self._notify_ffc_rsc_missing = True
        """Should we notify the user if ffc fails because cannot find dark or
        flat. Used to avoid several warnings. Only display one"""
        self._latest_reconstructions = []
        "list of url related to latest slice reconstruction from nabu"
        self._latest_vol_reconstructions = []
        """list of url related to latest volume reconstruction from nabu"""
        self._reconstruction_paths = set()
        self._proposal_name = None

    def _clear_heavy_cache(self):
        """For scan for now we don't want to remove any information from the cache.
        Mor eusefull for volume use case
        """
        pass

    @property
    def working_directory(self) -> Optional[str]:
        """
        working directory to use for this scan (for launching reconstruction for example)
        """
        raise NotImplementedError("Base class")

    def _init_index_process_file(self, overwrite_proc_file=False):
        if (
            not overwrite_proc_file
            and self.process_file is not None
            and os.path.exists(self.process_file)
        ):
            with open_hdf5(self.process_file) as h5s:
                self._process_index = len(h5s.items())
        else:
            self._process_index = 0

    def clear_caches(self):
        self._cache_proj_urls = None
        self._notify_ffc_rsc_missing = True
        super().clear_caches()

    @staticmethod
    def get_process_file_name(scan):
        raise NotImplementedError("Base class")

    def _flat_field_correction(
        self,
        data,
        index_proj: typing.Union[int, None],
        dark,
        flat1,
        flat2,
        index_flat1: int,
        index_flat2: int,
    ):
        """
        compute flat field correction for a provided data from is index
        one dark and two flats (require also indexes)
        """
        assert type(data) is numpy.ndarray
        can_process = True

        if dark is None:
            if self._notify_ffc_rsc_missing:
                logger.warning("cannot make flat field correction, dark not found")
            can_process = False

        if dark is not None and dark.ndim != 2:
            logger.error(
                "cannot make flat field correction, dark should be of " "dimension 2"
            )
            can_process = False

        if flat1 is None:
            if self._notify_ffc_rsc_missing:
                logger.warning("cannot make flat field correction, flat not found")
            can_process = False
        else:
            if flat1.ndim != 2:
                logger.error(
                    "cannot make flat field correction, flat should be of "
                    "dimension 2"
                )
                can_process = False
            if flat2 is not None and flat1.shape != flat2.shape:
                logger.error("the tow flats provided have different shapes.")
                can_process = False

        if dark is not None and flat1 is not None and dark.shape != flat1.shape:
            logger.error("Given dark and flat have incoherent dimension")
            can_process = False

        if dark is not None and data.shape != dark.shape:
            logger.error(
                "Image has invalid shape. Cannot apply flat field" "correction it"
            )
            can_process = False

        if can_process is False:
            self._notify_ffc_rsc_missing = False
            return data

        if flat2 is None:
            flat_value = flat1
        else:
            # compute weight and clip it if necessary
            if index_proj is None:
                w = 0.5
            else:
                w = (index_proj - index_flat1) / (index_flat2 - index_flat1)
                w = min(1, w)
                w = max(0, w)
            flat_value = flat1 * w + flat2 * (1 - w)

        div = flat_value - dark
        div[div == 0] = 1
        return (data - dark) / div

    def acquire_process_file_lock(self):
        """create a FileLocker context manager to insure safe write to the
        process file"""
        if self.process_file is None:
            raise ValueError("No processing file defined")
        return FileLockerManager().get_lock(file_name=self.process_file)

    @property
    def reconstructions(self):
        """list of reconstruction files"""
        return self._reconstructions

    @reconstructions.setter
    def reconstructions(self, reconstructions):
        self._reconstructions = reconstructions

    @property
    def reconstruction_paths(self):
        return self._reconstruction_paths

    def add_reconstruction_path(self, path: str):
        self._reconstruction_paths.add(path)

    @property
    def nabu_recons_params(self):
        return self._nabu_params

    @nabu_recons_params.setter
    def nabu_recons_params(self, recons_params):
        self._nabu_params = recons_params

    @property
    def axis_params(self):
        return self._axis_params

    @axis_params.setter
    def axis_params(self, parameters):
        self._axis_params = parameters

    @property
    def saaxis_params(self):
        return self._saaxis_params

    @saaxis_params.setter
    def saaxis_params(self, saaxis_params):
        self._saaxis_params = saaxis_params

    @property
    def sa_delta_beta_params(self):
        return self._sa_delta_beta_params

    @sa_delta_beta_params.setter
    def sa_delta_beta_params(self, sa_delta_beta_params):
        self._sa_delta_beta_params = sa_delta_beta_params

    # TODO: change name. Should be generalized to return Dataurl
    def getReconstructedFilesFromParFile(self, with_index):
        raise NotImplementedError("Base class")

    def projections_with_angle(self):
        raise NotImplementedError("Base class")

    def scan_dir_name(self) -> Optional[str]:
        """return name of the directory containing the acquisition"""
        raise NotImplementedError("Base class")

    def scan_basename(self) -> Optional[str]:
        """return basename of the directory containing the acquisition"""
        raise NotImplementedError("Base class")

    def scan_parent_dir_basename(self) -> Optional[str]:
        """return parent basename of the directory containing the acquisition"""
        raise NotImplementedError("Base class")

    def pop_process_index(self) -> int:
        """Return and lock the next free process index"""
        process_index = self._process_index
        self._process_index += 1
        return process_index

    @functools.lru_cache(maxsize=3)
    def get_opposite_projections(self, mode) -> tuple:
        """
        Return the radios for axis calculation and the requested mode.

        :param: angles we want to use for COR calculation. Can be 0-180,
                 90-180 or manual. If manual will return the 'most' appropriate
        :type: CorAngleMode
        :param nearest: if True then, pick the closest angle from the requested
                        one. If False, return (None, None) if the the angles
                        does not exists.
        :type: bool
        :return: couple of `opposite` radios that can be used for axis
                 calculation.
        :rtype: tuple(Optional[AxisResource], Optional[AxisResource])
        """
        radios_with_angle = self.projections_with_angle()
        angles = numpy.array(
            tuple(
                filter(
                    lambda a: numpy.issubdtype(type(a), numpy.number),
                    radios_with_angle.keys(),
                )
            )
        )

        from ..process.reconstruction.axis.anglemode import CorAngleMode
        from ..process.reconstruction.axis.params import (
            AxisResource,
        )  # avoid cyclic import

        mode = CorAngleMode.from_value(mode)

        if len(angles) < 2:
            logger.warning("less than two angles found. Unable to get opposite angles")
            return None, None

        initial_angle = angles[0]
        if mode in (CorAngleMode.use_0_180, CorAngleMode.manual_selection):
            couples = (initial_angle, initial_angle + 180.0)
        elif mode is CorAngleMode.use_90_270:
            couples = (initial_angle + 90.0, initial_angle + 270.0)
        else:
            raise ValueError(f"{mode} is not handle")

        def find_nearest(angles: numpy.ndarray, angle: float):
            if len(angles) == 0:
                return None
            dist = numpy.abs(angles - angle)
            idx = dist.argmin()
            if isinstance(idx, numpy.ndarray):
                idx = idx[0]
            return angles[idx]

        nearest_c1 = find_nearest(angles=angles, angle=couples[0])
        nearest_c2 = find_nearest(angles=angles, angle=couples[1])
        if nearest_c1 is not None and nearest_c2 is not None:
            radio_0 = AxisResource(radios_with_angle[nearest_c1])
            radio_1 = AxisResource(radios_with_angle[nearest_c2])
            return radio_0, radio_1
        else:
            return None, None

    def data_flat_field_correction(self, data, index=None):
        """Apply flat field correction on the given data

        :param numpy.ndarray data: the data to apply correction on
        :param Uion[int, None] index: index of the data in the acquisition
                                      sequence
        :return: corrected data
        :rtype: numpy.ndarray
        """
        raise NotImplementedError("Base class")

    def getReconsParamList(self):
        """

        :return: reconstruction parameters
        :rtype: ReconsParamList
        """
        raise NotImplementedError("Base class")

    @property
    def process_file(self) -> str:
        """

        :return: file used to store the processes launch by tomwer
        """
        return self._process_file

    @property
    def process_file_url(self) -> DataUrl:
        """

        :return: DataUrl of the process file
        """
        entry = self.entry if hasattr(self, "entry") else "entry"
        return DataUrl(file_path=self._process_file, data_path=entry, scheme="silx")

    def to_dict(self):
        res = {}
        # nabu reconstruction parameters
        if self._nabu_params:
            res[self._DICT_NABU_RP_KEY] = (
                self.nabu_recons_params
                if isinstance(self.nabu_recons_params, dict)
                else self.nabu_recons_params.to_dict()
            )
        else:
            res[self._DICT_NABU_RP_KEY] = None
        # axis reconstruction parameters
        if self.axis_params is None:
            res[self._DICT_AXIS_KEYS] = None
        else:
            res[self._DICT_AXIS_KEYS] = self.axis_params.to_dict()
        # saaxis reconstruction parameters
        if self.saaxis_params is None:
            res[self._DICT_SA_AXIS_KEYS] = None
        else:
            res[self._DICT_SA_AXIS_KEYS] = self.saaxis_params.to_dict()
        # sa delta-beta reconstruction parameters
        if self._sa_delta_beta_params is None:
            res[self._DICT_SA_DELTA_BETA_KEYS] = None
        else:
            res[self._DICT_SA_DELTA_BETA_KEYS] = self.sa_delta_beta_params.to_dict()
        # dark ref
        if self._dark_ref_params is None:
            res[self._DICT_DARK_REF_KEYS] = None
        else:
            res[self._DICT_DARK_REF_KEYS] = self._dark_ref_params.to_dict()
        # normalization
        if self.intensity_normalization is None:
            res[self._DICT_NORMALIZATION_KEY] = None
        else:
            res[self._DICT_NORMALIZATION_KEY] = self.intensity_normalization.to_dict()
        # process index
        res[self._DICT_PROCESS_INDEX_KEY] = self._process_index

        return res

    def load_from_dict(self, desc):
        from tomwer.core.process.reconstruction.axis.params import (
            AxisRP,
        )  # avoid cyclic import

        if isinstance(desc, io.TextIOWrapper):
            data = json.load(desc)
        else:
            data = desc
        if not (
            self.DICT_PATH_KEY in data  # pylint: disable=E1101
            and data[self.DICT_TYPE_KEY] == self._TYPE  # pylint: disable=E1101
        ):
            raise ValueError("Description is not an EDFScan json description")

        assert self.DICT_PATH_KEY in data  # pylint: disable=E1101
        # load axis reconstruction parameters
        axis_params = data.get(self._DICT_AXIS_KEYS, None)
        if axis_params is not None:
            self.axis_params = AxisRP.from_dict(axis_params)
        # load nabu reconstruction parameters
        if self._DICT_NABU_RP_KEY in data:
            self._nabu_params = data[self._DICT_NABU_RP_KEY]
        # load dark-ref parameters
        dark_ref_params = data.get(self._DICT_DARK_REF_KEYS, None)
        if dark_ref_params is not None:
            from tomwer.core.process.reconstruction.darkref.params import DKRFRP

            self._dark_ref_params = DKRFRP.from_dict(dark_ref_params)
        # load normalization
        intensity_normalization = data.get(self._DICT_NORMALIZATION_KEY, None)
        if intensity_normalization is not None:
            self.intensity_normalization = IntensityNormalization.from_dict(
                intensity_normalization
            )
        # load saaxis parameters
        saaxis_params = data.get(self._DICT_SA_AXIS_KEYS, None)
        if saaxis_params is not None:
            from tomwer.core.process.reconstruction.saaxis.params import SAAxisParams

            self._saaxis_params = SAAxisParams.from_dict(saaxis_params)
        # load sa delta beta parameters
        sa_delta_beta_params = data.get(self._DICT_SA_DELTA_BETA_KEYS, None)
        if sa_delta_beta_params is not None:
            from tomwer.core.process.reconstruction.sadeltabeta.params import (
                SADeltaBetaParams,
            )

            self._sa_delta_beta_params = SADeltaBetaParams.from_dict(
                sa_delta_beta_params
            )

        self._process_index = data[self._DICT_PROCESS_INDEX_KEY]

    def equal(self, other):
        """

        :param :class:`.ScanBase` other: instance to compare with
        :return: True if instance are equivalent
        :note: we cannot use the __eq__ function because this object need to be
               pickable
        """
        return (
            isinstance(other, self.__class__)
            or isinstance(self, other.__class__)
            and self.type == other.type  # pylint: disable=E1101
            and self.nabu_recons_params == other.nabu_recons_params
            and self.path == other.path  # pylint: disable=E1101
        )

    def get_sinogram(self, line, subsampling=1, norm_method=None, **kwargs):
        """
        extract the sinogram from projections

        :param line: which sinogram we want
        :type: int
        :param subsampling: subsampling to apply on the sinogram
        :return: sinogram from the radio lines
        :rtype: numpy.array
        """
        raise NotImplementedError("Base class")

    def get_normed_sinogram(self, line, subsampling=1):
        """
        Util to get the sinogram normed with settings currently defined
        on the 'intensity_normalization' property

        :param line:
        :param subsampling:
        :return:
        """
        return self.get_sinogram(
            line=line,
            subsampling=subsampling,
            norm_method=self.intensity_normalization.method,
            **self.intensity_normalization.get_extra_infos(),
        )

    def __str__(self):
        raise NotImplementedError("Base class")

    @staticmethod
    def get_pyhst_recons_file(scanID):
        """Return the .par file used for the current reconstruction if any.
        Otherwise return None"""
        if scanID == "":
            return None

        if scanID is None:
            raise RuntimeError("No current acquisition to validate")
        assert type(scanID) is str
        assert os.path.isdir(scanID)
        folderID = os.path.basename(scanID)
        # look for fasttomo files ending by slice.par
        parFiles = glob(os.path.join(scanID + folderID) + "*_slice.par")
        if len(parFiles) > 0:
            return orderFileByLastLastModification(scanID, parFiles)[-1]
        else:
            return None

    def _deduce_transfert_scan(self, output_dir):
        """
        Create the scan that will be generated if this scan is
        copy to the output_dir

        :param str output_dir:
        """
        raise NotImplementedError("Base class")

    def get_proj_angle_url(self, use_cache: bool = True, *args, **kwargs):
        """
        retrieve the url for each projections (including the alignement /
        return one) and associate to each (if possible) the angle.
        Alignment angle are set as angle (1) to specify that this is an
        alignment one.
        :param bool use_cache:
        :return: dictionary with angle (str or int) as key and url as value
        :rtype: dict
        """
        raise NotImplementedError("Base class")

    def get_reconstructions_urls(self):
        """

        :return: list of urls that contains reconstruction from nabu
        :rtype: list
        """
        from tomwer.core.process.reconstruction.output import (
            PROCESS_FOLDER_NAME,
        )  # avoid cyclic import

        all_recons_urls = set()
        recons_paths = self.reconstruction_paths
        if self.working_directory:
            recons_paths.add(
                os.path.join(
                    self.working_directory,
                    PROCESS_FOLDER_NAME,
                )
            )
        for path in recons_paths:
            all_recons_urls.update(self.get_reconstructions_urls_from_path(path))
        return all_recons_urls

    def get_reconstructions_urls_from_path(self, path, check_url=False):
        if path is None or not os.path.isdir(path):
            return []
        else:

            from tomwer.core.process.reconstruction.saaxis.saaxis import (
                DEFAULT_RECONS_FOLDER as MULTI_COR_DEFAULT_FOLDER,
            )
            from tomwer.core.process.reconstruction.sadeltabeta.sadeltabeta import (
                DEFAULT_RECONS_FOLDER as MULTI_DB_DEFAULT_FOLDER,
            )
            from tomwer.core.process.reconstruction.nabu.settings import (
                NABU_CFG_FILE_FOLDER,
            )

            res = set()
            for f in os.listdir(path):
                current_path = os.path.join(path, f)
                if os.path.isfile(current_path):
                    volume = _get_reconstructed_single_file_volume(
                        current_path, scan=self
                    )
                    if volume is not None:
                        res.add(volume)
                # avoid looking deeper if this doesn't look like a folder that could contain slices
                elif (
                    f
                    in (
                        "matlab",
                        "steps_file_basename_nabu_sinogram_save_step",
                        MULTI_COR_DEFAULT_FOLDER,
                        MULTI_DB_DEFAULT_FOLDER,
                        NABU_CFG_FILE_FOLDER,
                    )
                    or f.endswith("_vol")
                    or "slice" not in f
                ):
                    pass
                else:
                    res.update(
                        self.get_reconstructions_urls_from_path(
                            path=current_path, check_url=check_url
                        )
                    )
            return res

    @property
    def latest_reconstructions(self):
        """List of latest slices reconstructions (as VolumeIdentifier) - single slice volume"""
        return self._latest_reconstructions

    @property
    def latest_vol_reconstructions(self):
        """List of latest volume reconstructions (as VolumeIdentifier)"""
        return self._latest_vol_reconstructions

    def clear_latest_reconstructions(self):
        self._latest_reconstructions = []

    def set_latest_reconstructions(self, urls: typing.Iterable):
        if urls is None:
            self._latest_reconstructions = None
        else:
            self._latest_reconstructions = list(
                [self._process_volume_url(url) for url in urls]
            )

    def add_latest_reconstructions(self, urls: typing.Iterable):
        self._latest_reconstructions.extend(urls)

    def clear_latest_vol_reconstructions(self):
        self._latest_vol_reconstructions = []

    @staticmethod
    def _process_volume_url(url):
        if isinstance(url, str):
            return VolumeIdentifier.from_str(url)
        elif isinstance(url, VolumeIdentifier):
            return url
        elif isinstance(url, VolumeBase):
            return url.get_identifier()
        else:
            raise TypeError(
                f"url should be a {VolumeIdentifier} or a string reprenseting a {VolumeIdentifier}. {type(url)} provided instead"
            )

    def set_latest_vol_reconstructions(self, volume_identifiers: typing.Iterable):
        if volume_identifiers is None:
            self._latest_vol_reconstructions = None
        else:
            self._latest_vol_reconstructions = list(
                [self._process_volume_url(url) for url in volume_identifiers]
            )

    def add_latest_vol_reconstructions(self, volume_identifiers: tuple):
        assert isinstance(
            volume_identifiers, tuple
        ), "volume_identifiers is expected to be a tuple"
        self._latest_vol_reconstructions.extend(
            self._process_volume_url(volume_identifier)
            for volume_identifier in volume_identifiers
        )

    def _update_latest_recons_identifiers(self, old_path, new_path):
        def update_identifier(identifier):
            assert isinstance(
                identifier, BaseIdentifier
            ), f"identifier is expected to be an instance of {BaseIdentifier}"
            # small hack as this is not much used: simply try to replace a path by another. this is only used by the data transfer and EDF / SPEC
            # this time is almost over
            # FIXME: correct way to do this would be to recreate the volume, modify file or folder path and
            # recreate the new identifier
            identifier.replace(old_path, new_path, 1)

        self._latest_reconstructions = [
            update_identifier(identifier=identifier)
            for identifier in self._latest_reconstructions
        ]

        self._latest_vol_reconstructions = [
            update_identifier(identifier=identifier)
            for identifier in self._latest_vol_reconstructions
        ]

    def get_url_proj_index(self, url):
        """Return the index in the acquisition from the url"""

        def invert_dict(ddict):
            res = {}
            if ddict is not None:
                for key, value in ddict.items():
                    assert isinstance(value, DataUrl)
                    res[value.path()] = key
            return res

        proj_inv_url_to_index = invert_dict(self.projections)  # pylint: disable=E1101
        alig_inv_url_to_index = invert_dict(
            self.alignment_projections  # pylint: disable=E1101
        )
        if url.path() in proj_inv_url_to_index:
            return proj_inv_url_to_index[url.path()]
        elif url.path() in alig_inv_url_to_index:
            return alig_inv_url_to_index[url.path()]
        else:
            return None

    def set_process_index_frm_tomwer_process_file(self):
        """
        Set the process_index to the last index find in the tomwer_process_file
        + 1
        """
        from tomwer.core.process.task import Task

        if os.path.exists(self.process_file):
            with open_hdf5(self.process_file) as h5s:
                if not hasattr(self, "entry"):
                    entry = "entry"
                else:
                    entry = self.entry
                if entry in h5s:
                    node = h5s[entry]
                    pn = Task._get_process_nodes(
                        root_node=node, process=None, version=None
                    )
                    indexes = pn.values()
                    if len(indexes) > 0:
                        self._process_index = max(indexes) + 1
                        logger.debug(
                            f"set process_index from tomwer process file to {self._process_index}"
                        )

    def get_nabu_dataset_info(self, binning=1, binning_z=1, proj_subsampling=1):
        """

        :return: nabu dataset descriptor
        :rtype: dict
        """
        raise NotImplementedError("Base class")

    def to_nabu_dataset_analyser(self):
        """Return the equivalent DatasetAnalyzer for nabu"""
        raise NotImplementedError("Base class")

    def get_proposal_name(self) -> Optional[str]:
        return self._proposal_name

    def set_proposal_name(self, proposal_name: str) -> None:
        self._proposal_name = proposal_name


class _TomwerBaseDock(object):
    """
    Internal class to make difference between a simple TomoBase output and
    an output for a different processing (like scanvalidator.UpdateReconsParam)
    """

    def __init__(self, tomo_instance):
        self.__instance = tomo_instance

    @property
    def instance(self):
        return self.__instance


def _containsDigits(input_):
    return any(char.isdigit() for char in input_)


def _get_reconstructed_single_file_volume(
    file_, scan: TomwerScanBase, check_url=False
) -> Optional[VolumeBase]:
    scan_basename = scan.get_process_file_name
    scan_basename = scan.get_dataset_basename()
    if scan_basename is None:
        logger.error("TODO")

    file_base_name = os.path.basename(file_)
    if file_base_name.startswith(scan_basename) and "slice_" in file_base_name:
        if file_.endswith(TomwerScanBase.VALID_RECONS_EXTENSION):
            local_str = file_

            for extension in TomwerScanBase.VALID_RECONS_EXTENSION:
                if local_str.endswith(extension):
                    local_str = local_str.rsplit(extension, 1)[0]
                    break
            if "slice_pag_" in local_str:
                indexStr = local_str.split("slice_pag_")[-1].split("_")[0]
                volume_basename = local_str.split("slice_pag_")[0] + "slice_pag_"
            else:
                indexStr = local_str.split("slice_")[-1].split("_")[0]
                volume_basename = local_str.split("slice_")[0] + "slice_"

            if _containsDigits(indexStr):
                if extension == ".edf":
                    return EDFVolume(
                        folder=os.path.dirname(file_),
                        volume_basename=volume_basename,
                    )

            if extension in (".jp2", ".jp2"):
                return JP2KVolume(
                    folder=os.path.dirname(file_),
                    volume_basename=volume_basename,
                    data_extension=extension,
                )
            elif extension in (".tiff", ".tif"):
                return TIFFVolume(
                    folder=os.path.dirname(file_),
                    volume_basename=volume_basename,
                    data_extension=extension,
                )
            elif extension in (
                (".h5", ".hdf5", ".nx", ".nxs", ".nexus", ".nx5", ".hdf")
            ):
                entry = getattr(scan, "entry", "entry")
                volume = HDF5Volume(
                    file_path=os.path.abspath(file_),
                    data_path="/".join([entry, "reconstruction"]),
                )

                if check_url is True:
                    try:
                        with open_hdf5(os.path.abspath(file_)) as h5f:
                            if entry not in h5f:
                                logger.info("{volume} does not exists")
                                return None
                    except Exception:
                        logger.info("unable to check {volume}")
                        return None
                    else:
                        logger.info("{volume} checked")
                return volume


class NormMethod(_Enum):
    MANUAL_ROI = "manual ROI"
    AUTO_ROI = "automatic ROI"
    DATASET = "from dataset"
