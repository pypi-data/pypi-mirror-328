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


import functools
import io
import json
import logging
import os
import pathlib
from datetime import datetime
from typing import Optional
from urllib.parse import urlparse

import h5py
from processview.core.dataset import DatasetIdentifier
from silx.io.utils import open as open_hdf5
from tomoscan.esrf.identifier.hdf5Identifier import (
    NXtomoScanIdentifier as _NXtomoScanIdentifier,
)
from tomoscan.esrf.identifier.url_utils import UrlSettings, split_path, split_query
from tomoscan.esrf.scan.nxtomoscan import NXtomoScan as _tsNXtomoScan
from nxtomo.nxobject.nxdetector import ImageKey

from tomwer.utils import docstring
from tomwer.core.scan.helicalmetadata import HelicalMetadata

from .scanbase import TomwerScanBase

_logger = logging.getLogger(__name__)


class NXtomoScanIdentifier(_NXtomoScanIdentifier, DatasetIdentifier):
    def __init__(self, metadata=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DatasetIdentifier.__init__(
            self, data_builder=NXtomoScan.from_identifier, metadata=metadata
        )

    @staticmethod
    def from_str(identifier):
        info = urlparse(identifier)
        paths = split_path(info.path)
        if len(paths) == 1:
            hdf5_file = paths[0]
            tomo_type = None
        elif len(paths) == 2:
            tomo_type, hdf5_file = paths
        else:
            raise ValueError("Failed to parse path string:", info.path)
        if tomo_type is not None and tomo_type != NXtomoScanIdentifier.TOMO_TYPE:
            raise TypeError(
                f"provided identifier fits {tomo_type} and not {NXtomoScanIdentifier.TOMO_TYPE}"
            )

        queries = split_query(info.query)
        entry = queries.get(UrlSettings.DATA_PATH_KEY, None)
        if entry is None:
            raise ValueError(f"expects to get {UrlSettings.DATA_PATH_KEY} query")

        return NXtomoScanIdentifier(object=NXtomoScan, hdf5_file=hdf5_file, entry=entry)

    def long_description(self) -> str:
        """used for processview header tooltip for now"""
        return self.to_str()

    def short_description(self) -> str:
        return f"scan: {self.data_path.lstrip('/')}@{os.path.basename(self._file_path)}"


class NXtomoScan(_tsNXtomoScan, TomwerScanBase):
    """
    This is the implementation of a TomoBase class for an acquisition stored
    in a HDF5 file.

    For now several property of the acquisition is accessible thought a getter
    (like get_scan_range) and a property (scan_range).

    This is done to be compliant with TomoBase instanciation. But his will be
    replace progressively by properties at the 'TomoBase' level

    :param scan: scan directory or scan masterfile.h5
    :type: Union[str,None]
    """

    _TYPE = "hdf5"

    def __init__(self, scan, entry, index=None, overwrite_proc_file=False):
        TomwerScanBase.__init__(self)
        _tsNXtomoScan.__init__(self, scan=scan, entry=entry, index=index)
        # speed up for now, avoid to run check by default
        self.set_check_behavior(run_check=False)
        # register at least the 'default' working directory as a possible reconstruction path
        self.add_reconstruction_path(self.path)
        self._helical = HelicalMetadata()

        self._reconstruction_urls = None
        self._projections_with_angles = None
        self._process_file = self.get_process_file_name(self)
        self._init_index_process_file(overwrite_proc_file=overwrite_proc_file)
        try:
            reduced_darks, metadata = self.load_reduced_darks(return_info=True)
        except (KeyError, OSError, ValueError):
            # file or key does not exists
            pass
        else:
            self.set_reduced_darks(reduced_darks, darks_infos=metadata)

        try:
            reduced_flats, metadata = self.load_reduced_flats(return_info=True)
        except (KeyError, OSError, ValueError):
            pass
        else:
            self.set_reduced_flats(reduced_flats, flats_infos=metadata)

    @property
    def working_directory(self):
        if self.master_file is None:
            return None
        else:
            return os.path.abspath(os.path.dirname(self.master_file))

    @property
    def helical(self):
        return self._helical

    @staticmethod
    def from_identifier(identifier):
        """Return the Dataset from a identifier"""
        if not isinstance(identifier, NXtomoScanIdentifier):
            raise TypeError(
                f"identifier should be an instance of {NXtomoScanIdentifier}. Not {type(identifier)}"
            )
        return NXtomoScan(scan=identifier.file_path, entry=identifier.data_path)

    def get_identifier(self):
        try:
            stat = pathlib.Path(self.master_file).stat()
        except Exception:
            stat = None

        return NXtomoScanIdentifier(
            object=self,
            hdf5_file=self.master_file,
            entry=self.entry,
            metadata={
                "name": self.master_file,
                "creation_time": (
                    datetime.fromtimestamp(stat.st_ctime) if stat else None
                ),
                "modification_time": (
                    datetime.fromtimestamp(stat.st_ctime) if stat else None
                ),
            },
        )

    @staticmethod
    def get_process_file_name(scan):
        if scan.path is not None:
            basename, _ = os.path.splitext(scan.master_file)
            basename = os.path.basename(basename)
            basename = "_".join((basename, "tomwer_processes.h5"))
            return os.path.join(scan.path, basename)
        else:
            return None

    @staticmethod
    def directory_contains_scan(directory, src_pattern=None, dest_pattern=None):
        """

        Check if the given directory is holding an acquisition

        :param str directory: directory we want to check
        :param str src_pattern: buffer name pattern ('lbsram')
        :param dest_pattern: output pattern (''). Needed because some
                             acquisition can split the file produce between
                             two directories. This is the case for edf,
                             where .info file are generated in /data/dir
                             instead of /lbsram/data/dir
        :type: str
        :return: does the given directory contains any acquisition
        :rtype: bool
        """
        master_file = os.path.join(directory, os.path.basename(directory))
        if os.path.exists("master_file.hdf5"):
            return True
        else:
            return os.path.exists(master_file + ".h5")

    def clear_caches(self):
        _tsNXtomoScan.clear_caches(self)
        TomwerScanBase.clear_caches(self)

    def is_abort(self, src_pattern, dest_pattern):
        """
        Check if the acquisition have been aborted. In this case the directory
        should contain a [scan].abo file

        :param str src_pattern: buffer name pattern ('lbsram')
        :param dest_pattern: output pattern (''). Needed because some
                             acquisition can split the file produce between
                             two directories. This is the case for edf,
                             where .info file are generated in /data/dir
                             instead of /lbsram/data/dir
        :return: True if the acquisition have been abort and the directory
                 should be abort
        """
        # for now there is no abort definition in .hdf5
        return False

    @staticmethod
    def from_dict(_dict):
        path = _dict[NXtomoScan.DICT_PATH_KEY]
        entry = _dict[NXtomoScan._DICT_ENTRY_KEY]

        scan = NXtomoScan(scan=path, entry=entry)
        scan.load_from_dict(_dict=_dict)
        return scan

    @docstring(TomwerScanBase)
    def load_from_dict(self, _dict):
        """

        :param _dict:
        :return:
        """
        if isinstance(_dict, io.TextIOWrapper):
            data = json.load(_dict)
        else:
            data = _dict
        if not (self.DICT_TYPE_KEY in data and data[self.DICT_TYPE_KEY] == self._TYPE):
            raise ValueError("Description is not an EDFScan json description")

        _tsNXtomoScan.load_from_dict(self, _dict)
        TomwerScanBase.load_from_dict(self, _dict)
        return self

    @docstring(TomwerScanBase)
    def to_dict(self) -> dict:
        ddict = _tsNXtomoScan.to_dict(self)
        ddict.update(TomwerScanBase.to_dict(self))
        return ddict

    def update(self):
        """update list of radio and reconstruction by parsing the scan folder"""
        if self.master_file is None:
            return
        if not os.path.exists(self.master_file):
            return
        _tsNXtomoScan.update(self)
        self.reconstructions = self.get_reconstructions_urls()

    def _get_scheme(self):
        """

        :return: scheme to read url
        :rtype: str
        """
        return "silx"

    def is_finish(self):
        return len(self.projections) >= self.tomo_n

    @docstring(TomwerScanBase.get_sinogram)
    @functools.lru_cache(maxsize=16, typed=True)
    def get_sinogram(self, line, subsampling=1, norm_method=None, **kwargs):
        """

        extract the sinogram from projections

        :param line: which sinogram we want
        :type: int
        :param subsampling: subsampling to apply if any. Allows to skip some io
        :type: int
        :return: sinogram from the radio lines
        :rtype: numpy.array
        """
        return _tsNXtomoScan.get_sinogram(
            self,
            line=line,
            subsampling=subsampling,
            norm_method=norm_method,
            **kwargs,
        )

    @docstring(TomwerScanBase.get_proj_angle_url)
    def get_proj_angle_url(self, use_cache: bool = True, with_alignment=True):
        if not use_cache:
            self._cache_proj_urls = None

        if self._cache_proj_urls is None:
            frames = self.frames
            if frames is None:
                return {}

            self._cache_proj_urls = {}
            for frame in frames:
                if frame.image_key is ImageKey.PROJECTION:
                    if frame.is_control and with_alignment:
                        self._cache_proj_urls[f"{frame.rotation_angle} (1)"] = frame.url
                    elif frame.is_control:
                        continue
                    else:
                        self._cache_proj_urls[str(frame.rotation_angle)] = frame.url
        return self._cache_proj_urls

    @docstring(TomwerScanBase._deduce_transfert_scan)
    def _deduce_transfert_scan(self, output_dir):
        new_master_file_path = os.path.join(
            output_dir, os.path.basename(self.master_file)
        )
        return NXtomoScan(scan=new_master_file_path, entry=self.entry)

    def data_flat_field_correction(self, data, index=None):
        flats = self.reduced_flats
        flat1 = flat2 = None
        index_flat1 = index_flat2 = None
        if flats is not None:
            flat_indexes = sorted(list(flats.keys()))
            if len(flats) > 0:
                index_flat1 = flat_indexes[0]
                flat1 = flats[index_flat1]
            if len(flats) > 1:
                index_flat2 = flat_indexes[-1]
                flat2 = flats[index_flat2]
        darks = self.reduced_darks
        dark = None
        if darks is not None and len(darks) > 0:
            # take only one dark into account for now
            dark = list(darks.values())[0]
        return self._flat_field_correction(
            data=data,
            dark=dark,
            flat1=flat1,
            flat2=flat2,
            index_flat1=index_flat1,
            index_flat2=index_flat2,
            index_proj=index,
        )

    @docstring(_tsNXtomoScan.ff_interval)
    @property
    def ff_interval(self):
        """
        Make some assumption to compute the flat field interval:
        """

        def get_first_two_ff_indexes():
            if self.flats is None:
                return None, None
            else:
                self._last_flat_index = None
                self._first_serie_flat_index = None
                for flat_index in self.flats:
                    if self._last_flat_index is None:
                        self._last_flat_index = flat_index
                    elif flat_index == self._last_flat_index + 1:
                        self._last_flat_index = flat_index
                        continue
                    else:
                        return self._last_flat_index, flat_index
            return None, None

        first_serie_index, second_serie_index = get_first_two_ff_indexes()
        if first_serie_index is None:
            return 0
        elif second_serie_index is not None:
            return second_serie_index - first_serie_index - 1
        else:
            return 0

    def projections_with_angle(self):
        """projections / radio, does not include the return projections"""
        if self._projections_with_angles is None:
            if self.frames:
                proj_frames = tuple(
                    filter(
                        lambda x: x.image_key == ImageKey.PROJECTION
                        and x.is_control is False,
                        self.frames,
                    )
                )
                self._projections_with_angles = {}
                for proj_frame in proj_frames:
                    self._projections_with_angles[proj_frame.rotation_angle] = (
                        proj_frame.url
                    )
        return self._projections_with_angles

    @staticmethod
    def is_nexus_nxtomo_file(file_path: str) -> bool:
        if h5py.is_hdf5(file_path):
            return len(NXtomoScan.get_nxtomo_entries(file_path)) > 0

    @staticmethod
    def get_nxtomo_entries(file_path: str) -> tuple:
        if not h5py.is_hdf5(file_path):
            return tuple()
        else:
            res = []
            with open_hdf5(file_path) as h5s:
                for entry_name, node in h5s.items():
                    if isinstance(node, h5py.Group):
                        if NXtomoScan.entry_is_nx_tomo(node):
                            res.append(entry_name)
            return tuple(res)

    @staticmethod
    def entry_is_nx_tomo(entry: h5py.Group):
        return ("beam" in entry and "instrument" in entry and "sample" in entry) or (
            hasattr(entry, "attrs")
            and "definition" in entry.attrs
            and entry.attrs["definition"] == "NXtomo"
        )

    @staticmethod
    def is_nxdetector(grp: h5py.Group):
        """
        Check if the grp is an nx detector

        :param h5py.Group grp:
        :return: True if this is the definition of a group
        :rtype: bool
        """
        if hasattr(grp, "attrs"):
            if "NX_class" in grp.attrs and grp.attrs["NX_class"] == "NXdetector":
                return True
        return False

    # Dataset implementation

    @docstring(TomwerScanBase)
    def get_nabu_dataset_info(self, binning=1, binning_z=1, proj_subsampling=1):
        if not isinstance(binning, int):
            raise TypeError(f"binning should be an int. Not {type(binning)}")
        if not isinstance(binning_z, int):
            raise TypeError(f"binning_z should be an int. Not {type(binning_z)}")
        if not isinstance(proj_subsampling, int):
            raise TypeError(
                f"proj_subsampling should be an int. Not {type(proj_subsampling)}"
            )
        return {
            "hdf5_entry": self.entry,
            "location": os.path.basename(self.master_file),
            "binning": binning,
            "binning_z": binning_z,
            "projections_subsampling": proj_subsampling,
        }

    @docstring(TomwerScanBase)
    def to_nabu_dataset_analyser(self):
        from nabu.resources.dataset_analyzer import HDF5DatasetAnalyzer

        return HDF5DatasetAnalyzer(
            location=self.master_file, extra_options={"hdf5_entry": self.entry}
        )

    @docstring(TomwerScanBase)
    def scan_dir_name(self) -> Optional[str]:
        """for 'this/is/my/file.h5' returns 'my'"""
        if self.master_file is not None:
            return os.path.dirname(self.master_file).split(os.sep)[-1]
        else:
            return None

    @docstring(TomwerScanBase)
    def scan_basename(self):
        if self.master_file is not None:
            try:
                return os.path.dirname(self.master_file)
            except Exception:
                return None
        else:
            return None

    @docstring(TomwerScanBase)
    def scan_parent_dir_basename(self):
        if self.master_file is not None:
            try:
                return os.path.dirname(os.path.dirname(self.master_file))
            except Exception:
                return None
        else:
            return None

    def get_proposal_name(self) -> Optional[str]:
        if self._proposal_name is None and self.master_file is not None:
            bliss_raw_data_files = self.get_bliss_orginal_files() or ()
            bliss_raw_data_file = (
                bliss_raw_data_files[0] if len(bliss_raw_data_files) > 0 else None
            )
            if bliss_raw_data_file is not None:
                strips = bliss_raw_data_file.lstrip("/").split("/")
                if len(strips) > 2 and bliss_raw_data_file.startswith(
                    ("/data/visitor", "/data/visitor")
                ):
                    self._proposal_name = strips[2]
                elif (
                    bliss_raw_data_file.startswith(("/data", "data"))
                    and len(strips) > 3
                    and strips[2] == "inhouse"
                ):
                    self._proposal_name = strips[3]
                else:
                    _logger.warning(
                        "this doesn't looks like a bliss file aquired at the ESRF. Unable to find proposal name"
                    )
        return self._proposal_name
