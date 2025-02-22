# # coding: utf-8
# # /*##########################################################################
# #
# # Copyright (c) 2016-2017 European Synchrotron Radiation Facility
# #
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# #
# # The above copyright notice and this permission notice shall be included in
# # all copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# # THE SOFTWARE.
# #
# # ###########################################################################*/

# __authors__ = ["H. Payno"]
# __license__ = "MIT"
# __date__ = "16/11/2020"


# import logging
# import os

# from silx.utils.enum import Enum as _Enum
# from tomwer.core.utils.deprecation import deprecated_warning, deprecated
# from tomoscan.factory import Factory
# from tomoscan.volumebase import VolumeBase

# import tomwer.version
# from tomwer.core.process.task import Task
# from tomwer.core.scan.scanbase import TomwerScanBase
# from tomwer.core.scan.scanfactory import ScanFactory
# from tomwer.core.utils.scanutils import data_identifier_to_scan
# from tomwer.utils import docstring

# _logger = logging.getLogger(__name__)


# class OutputType(_Enum):
#     STATIC = "static"
#     ONE_LEVEL_UPPER = "../volume"


# def create_volume_symbolic_link(scan: TomwerScanBase, output_folder: str):
#     """
#     Create a symbolic link for each volume reconstructed of `scan`

#     :param TomwerScanBase scan:
#     :param str output_folder:
#     """
#     if scan.latest_vol_reconstructions is None:
#         _logger.info("No volume reconstructed found")
#         return
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#     for volume_url in scan.latest_vol_reconstructions:
#         volume = Factory.create_tomo_object_from_identifier(volume_url)
#         assert isinstance(volume, VolumeBase)
#         volume_files = set(
#             list(volume.browse_data_files()) + list(volume.browse_metadata_files()),
#         )
#         for src_file_path in volume_files:
#             if src_file_path is not None:
#                 dst_file_path = os.path.join(
#                     output_folder, os.path.basename(src_file_path)
#                 )
#                 if os.path.exists(dst_file_path):
#                     _logger.info(
#                         "{} already exists. Cannot create a symbolic link on it"
#                     )
#                 else:
#                     print(
#                         "src_file is", src_file_path, "dst_file_path is", dst_file_path
#                     )
#                     os.symlink(src=src_file_path, dst=dst_file_path)


# class VolumeSymbolicLinkTask(
#     Task,
#     input_names=("data",),
#     output_names=("data",),
#     optional_input_names=("serialize_output_data", "output_type", "output_folder"),
# ):
#     """
#     Process class for volume symbolic link
#     """

#     def __init__(
#         self, varinfo=None, inputs=None, node_id=None, node_attrs=None, execinfo=None
#     ):
#         super().__init__(
#             varinfo=varinfo,
#             inputs=inputs,
#             node_id=node_id,
#             node_attrs=node_attrs,
#             execinfo=execinfo,
#         )
#         self._output_type = OutputType.ONE_LEVEL_UPPER
#         self._output_folder = None

#     @docstring(Task.set_configuration)
#     @deprecated(
#         reason="ewoksification",
#         replacement="task.inputs.output_type and task.inputs.output_folder",
#         since_version="1.2",
#     )
#     def set_configuration(self, properties):
#         if "output_type" in properties:
#             self._output_type = OutputType.from_value(properties["output_type"])
#         if "output_folder" in properties:
#             self._output_folder = properties["output_folder"]

#     @deprecated(
#         reason="ewoksification",
#         replacement="task.inputs.output_type and task.inputs.output_folder",
#         since_version="1.2",
#     )
#     def get_configuration(self):
#         return super().get_configuration()

#     @docstring(Task.program_name)
#     @staticmethod
#     def program_name():
#         return "tomwer_volume_symlink"

#     @docstring(Task.program_version)
#     @staticmethod
#     def program_version():
#         return tomwer.version.version

#     @docstring(Task.run)
#     def run(self):
#         scan = data_identifier_to_scan(self.inputs.data)
#         if type(scan) is dict:
#             scan = ScanFactory.create_scan_object_frm_dict(scan)
#         else:
#             scan = scan
#         if scan is None:
#             return
#         if not isinstance(scan, TomwerScanBase):
#             raise TypeError(
#                 f"scan is expected to be a dict or an instance of TomwerScanBase. Not {type(scan)}"
#             )

#         output_type = OutputType.from_value(
#             self.get_input_value("output_type", self._output_type)
#         )
#         output_folder = self.get_input_value("output_folder", self._output_folder)
#         if output_type is OutputType.STATIC:
#             if output_folder is None:
#                 raise ValueError(
#                     "Manual setting of the output folder is "
#                     "requested but None is provided."
#                 )
#             else:
#                 if not os.path.isabs(output_folder):
#                     os.path.abspath(
#                         os.path.join(os.path.abspath(scan.path), output_folder)
#                     )
#         elif output_type is OutputType.ONE_LEVEL_UPPER:
#             output_folder = os.path.abspath(scan.path)
#             output_folder = os.path.abspath(
#                 os.path.join(output_folder, output_type.value)
#             )
#         else:
#             raise ValueError(f"output type {output_type.value} is not managed")
#         create_volume_symbolic_link(scan=scan, output_folder=output_folder)
#         if self.get_input_value("serialize_output_data", True):
#             self.outputs.data = scan.to_dict()
#         else:
#             self.outputs.data = scan

#     @docstring(Task.definition)
#     @staticmethod
#     def definition():
#         return "Create a symbolic link to the volume folder"


# class VolumeSymbolicLinkProcess(VolumeSymbolicLinkTask):
#     def __init__(
#         self, varinfo=None, inputs=None, node_id=None, node_attrs=None, execinfo=None
#     ):
#         deprecated_warning(
#             name="tomwer.core.process.control.volumesymlink.VolumeSymbolicLinkProcess",
#             type_="class",
#             reason="improve readibility",
#             since_version="1.2",
#             replacement="VolumeSymbolicLinkTask",
#         )
#         super().__init__(varinfo, inputs, node_id, node_attrs, execinfo)
