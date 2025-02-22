import logging
import os
import shutil
import tempfile
import functools

from typing import Optional

from nabu.stitching import config as stitching_config
from nabu.stitching.config import StitchingType, dict_to_config_obj
from nabu.stitching.z_stitching import (
    PostProcessZStitcher,
    PreProcessZStitcher,
)
from nabu.pipeline.config import generate_nabu_configfile, parse_nabu_config_file
from nabu.stitching.alignment import AlignmentAxis1, AlignmentAxis2
from nabu.stitching.config import (
    get_default_stitching_config,
    identifiers_as_str_to_instances,
    KEY_RESCALE_MAX_PERCENTILES,
    KEY_RESCALE_MIN_PERCENTILES,
    RESCALE_FRAMES,
    RESCALE_PARAMS,
    SECTIONS_COMMENTS as _SECTIONS_COMMENTS,
    STITCHING_SECTION,
)

from nxtomomill.io.utils import (
    convert_str_to_tuple as _convert_str_to_tuple,
    convert_str_to_bool as _convert_str_to_bool,
)
from silx.gui import qt
from tomoscan.serie import Serie
from tomoscan.scanbase import TomoScanBase as _TomoScanBase
from tomoscan.volumebase import VolumeBase as _VolumeBase

from tomwer.core.scan.nxtomoscan import NXtomoScan, NXtomoScanIdentifier
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.volume.volumefactory import VolumeFactory
from tomwer.core.volume.volumebase import TomwerVolumeBase
from tomwer.core.tomwer_object import TomwerObject
from tomwer.core.volume.hdf5volume import HDF5Volume, HDF5VolumeIdentifier
from tomwer.io.utils.utils import str_to_dict
from tomwer.gui.qconfigfile import QConfigFileDialog
from tomwer.gui.stitching.config.axisparams import StitcherAxisParams
from tomwer.gui.stitching.config.positionoveraxis import PosEditorOverOneAxis
from tomwer.gui.stitching.config.output import StitchingOutput
from tomwer.gui.stitching.config.stitchingstrategies import StitchingStrategies
from tomwer.gui.stitching.stitching_preview import PreviewStitchingPlot
from tomwer.gui.stitching.stitching_raw import RawStitchingPlot
from tomwer.gui.stitching.axisorderedlist import EditableZOrderedTomoObjWidget
from tomwer.gui.stitching.z_stitching.fineestimation import _SliceGetter
from tomwer.gui.configuration.action import (
    BasicConfigurationAction,
    ExpertConfigurationAction,
    MinimalisticConfigurationAction,
)
from tomwer.gui.configuration.level import ConfigurationLevel
from tomwer.gui.stitching import action as stitching_action
from tomwer.gui.stitching.normalization import NormalizationBySampleGroupBox


_logger = logging.getLogger(__name__)


def convert_str_to_tuple(input_str, none_if_empty):
    if input_str is None:
        return None
    elif isinstance(input_str, (tuple, list)):
        return tuple(input_str)
    else:
        return _convert_str_to_tuple(input_str=input_str, none_if_empty=none_if_empty)


class ZStitchingCentralWidget(qt.QWidget):
    sigStitchingTypeChanged = qt.Signal(str)
    """emit when stitching type changes"""
    sigTomoObjsLoaded = qt.Signal(tuple)
    """Signal emit when during setting a configuration this trigger some addition of tomo object"""

    class _ZStitchingCentralTabWidget(qt.QTabWidget):
        def __init__(self, parent=None) -> None:
            super().__init__(parent)
            self._serieName = None
            self._zOrderedList = EditableZOrderedTomoObjWidget(parent=self)
            self.addTab(self._zOrderedList, "axis 0 ordered list")
            self._previewPlot = PreviewStitchingPlot(parent=self)
            self.addTab(self._previewPlot, "stitching preview")
            # TODO: add a raw display to print frame from raw position z positions ...
            self._rawDisplayPlot = RawStitchingPlot(
                parent=self,
                aspectRatio=True,
                logScale=False,
                copy=False,
                save=False,
                print_=False,
                grid=False,
                curveStyle=False,
                mask=False,
                alpha_values=True,
            )
            self._rawDisplayPlot.setKeepDataAspectRatio(True)
            self._rawDisplayPlot.setAxesDisplayed(False)
            self.addTab(self._rawDisplayPlot, "raw display")
            # add an option to activate / deactivate auto update of the raw display as it can be time consuming.
            raw_display_idx = self.indexOf(self._rawDisplayPlot)
            self._rawDisplayCB = qt.QCheckBox(self)
            self.tabBar().setTabButton(
                raw_display_idx,
                qt.QTabBar.LeftSide,
                self._rawDisplayCB,
            )
            self.setTabToolTip(
                raw_display_idx,
                "If toggled will keep the raw display up to date from axis 0 modifications",
            )
            # set up: turn overlay one by default
            self._previewPlot._backGroundAction.setChecked(True)

        def _handleRawDisplayconnection(self, toggled: bool):
            if toggled:
                self._connectRawDisplayConnection()
            else:
                self._disconnectRawDisplayConnection()

        def setSerie(self, serie: Serie):
            for elmt in serie:
                self._zOrderedList.addTomoObj(elmt)
            self.setSerieName(serie.name)

        def addTomoObj(self, tomo_obj: TomwerObject):
            self._zOrderedList.addTomoObj(tomo_obj)

        def removeTomoObj(self, tomo_obj: TomwerObject):
            self._zOrderedList.removeTomoObj(tomo_obj=tomo_obj)

        def getSerieName(self) -> str:
            return self._serieName

        def setSerieName(self, name: str):
            self._serieName = name

        def getTomoObjs(self) -> tuple:
            return self._zOrderedList.getTomoObjsZOrdered()

        def clearTomoObjs(self):
            self._zOrderedList.clearTomoObjs()

        def clean(self) -> None:
            self.clearTomoObjs()
            self._previewPlot.clear()

        def close(self):
            self._previewPlot.close()
            # requested for the waiting plot update
            super().close()

        def setAddTomoObjCallbacks(self, *args, **kwargs):
            self._zOrderedList.setAddTomoObjCallbacks(*args, **kwargs)

        def setRemoveTomoObjCallbacks(self, *args, **kwargs):
            self._zOrderedList.setRemoveTomoObjCallbacks(*args, **kwargs)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setLayout(qt.QGridLayout())

        self._stitchingTypeCB = qt.QComboBox(parent=self)
        for mode in StitchingType.values():
            self._stitchingTypeCB.addItem(mode)
        self._stitchingTypeCB.currentIndexChanged.connect(self._stitchingTypeChanged)
        self.layout().addWidget(qt.QLabel("stitching method:"), 0, 0, 1, 1)
        self.layout().addWidget(self._stitchingTypeCB, 0, 1, 1, 1)

        self._mainWidget = self._ZStitchingCentralTabWidget(parent=self)
        self.layout().addWidget(self._mainWidget, 1, 0, 4, 4)

        # set up
        self.setStitchingType(self.getStitchingType())
        self._mainWidget.setCurrentWidget(self._mainWidget._previewPlot)

        # conenct signal / slot
        self._stitchingTypeCB.currentIndexChanged.connect(self._stitchingTypeChanged)

    def close(self):
        self._mainWidget.close()
        # requested for the waiting plot update
        super().close()

    def clean(self):
        self._mainWidget.clean()

    def _stitchingTypeChanged(self, *args, **kwargs):
        self.sigStitchingTypeChanged.emit(self.getStitchingType().value)

    def getStitchingType(self):
        return StitchingType.from_value(self._stitchingTypeCB.currentText())

    def setStitchingType(self, mode):
        mode = StitchingType.from_value(mode)
        idx = self._stitchingTypeCB.findText(mode.value)
        if idx >= 0:
            self._stitchingTypeCB.setCurrentIndex(idx)

    def addTomoObj(self, tomo_obj: TomwerObject):
        self._mainWidget.addTomoObj(tomo_obj)
        self._updatePreviewPixelSize()

    def removeTomoObj(self, tomo_obj: TomwerObject):
        self._mainWidget.removeTomoObj(tomo_obj)
        self._updatePreviewPixelSize()

    def _updatePreviewPixelSize(self):
        """update the pixel size of the preview from existing tomo obj"""

        def get_pixel_size():
            tomo_objs = self._mainWidget.getTomoObjs()
            for tomo_obj in tomo_objs:
                if (
                    isinstance(tomo_obj, NXtomoScan)
                    and tomo_obj.x_pixel_size is not None
                    and tomo_obj.y_pixel_size is not None
                ):
                    return tomo_obj.x_pixel_size, tomo_obj.y_pixel_size
                elif (
                    isinstance(tomo_obj, TomwerVolumeBase)
                    and tomo_obj.voxel_size is not None
                ):
                    return tomo_obj.voxel_size[1], tomo_obj.voxel_size[2]
            return None, None

        pixel_size = get_pixel_size()
        self._mainWidget._previewPlot.setPixelSize(pixel_size=pixel_size)

    def getConfiguration(self) -> dict:
        # missing parameters:
        # * overwrite
        # * slices
        # * slurm stuff...

        tomo_objs = self._mainWidget.getTomoObjs()

        def filter_empty_list_and_cast_as_int(elmts):
            new_list = [int(elmt) for elmt in elmts if elmt is not None]
            if len(new_list) == 0:
                return None
            else:
                return elmts

        axis_0_pos_px = filter_empty_list_and_cast_as_int(
            [
                obj.stitching_metadata.get_abs_position_px(axis=0) or 0
                for obj in tomo_objs
            ]
        )
        axis_2_pos_px = filter_empty_list_and_cast_as_int(
            [
                obj.stitching_metadata.get_abs_position_px(axis=2) or 0
                for obj in tomo_objs
            ]
        )
        return {
            "stitching": {
                "type": self.getStitchingType().value,
                "axis_0_pos_px": "" if axis_0_pos_px is None else axis_0_pos_px,
                "axis_2_pos_px": "" if axis_2_pos_px is None else axis_2_pos_px,
            },
            "inputs": {
                "input_datasets": [obj.get_identifier().to_str() for obj in tomo_objs],
            },
        }

    def setConfiguration(self, config: dict) -> None:
        stitching_type = config.get("stitching", {}).get("type", None)
        if stitching_type is not None:
            self.setStitchingType(stitching_type)
        tomo_obj_ids = config.get("inputs", {}).get("input_datasets", None)
        tomo_obj_ids = identifiers_as_str_to_instances(tomo_obj_ids)
        axis_0_pos = convert_str_to_tuple(
            config.get("stitching", {}).get("axis_0_pos_px", None),
            none_if_empty=True,
        )
        axis_2_pos = convert_str_to_tuple(
            config.get("stitching", {}).get("axis_2_pos_px", None),
            none_if_empty=True,
        )
        if tomo_obj_ids is not None:
            self._mainWidget.clearTomoObjs()
            if axis_0_pos is None:
                axis_0_pos = [None] * len(tomo_obj_ids)
            if axis_2_pos is None:
                axis_2_pos = [None] * len(tomo_obj_ids)
            if len(axis_0_pos) != len(tomo_obj_ids):
                _logger.error(
                    "incoherent axis 0 position compared to the number of input datasets. Will ignore those"
                )
                axis_0_pos = [None] * len(tomo_obj_ids)
            if len(axis_2_pos) != len(tomo_obj_ids):
                _logger.error(
                    "incoherent axis 2 position compared to the number of input datasets. Will ignore those"
                )
                axis_2_pos = [None] * len(tomo_obj_ids)

            new_tomo_objs = []
            for tomo_obj_id, axis_0_v, axis_2_v in zip(
                tomo_obj_ids, axis_0_pos, axis_2_pos
            ):
                if isinstance(tomo_obj_id, TomwerObject):
                    tomo_obj = tomo_obj_id
                elif isinstance(tomo_obj_id, _TomoScanBase):
                    # for now we need to convert it back because object are not the same
                    tomo_obj = ScanFactory.create_tomo_object_from_identifier(
                        tomo_obj_id.get_identifier().to_str()
                    )
                elif isinstance(tomo_obj_id, _VolumeBase):
                    tomo_obj = VolumeFactory.create_tomo_object_from_identifier(
                        tomo_obj_id.get_identifier().to_str()
                    )
                else:
                    tomo_obj = ScanFactory.create_tomo_object_from_identifier(
                        tomo_obj_id
                    )
                self.addTomoObj(tomo_obj=tomo_obj)
                # set metadata information if any
                for axis, axis_value in zip((0, 2), (axis_0_v, axis_2_v)):
                    if axis_value is not None:
                        tomo_obj.stitching_metadata.setPxPos(int(axis_value), axis=axis)
                new_tomo_objs.append(tomo_obj)
            self.sigTomoObjsLoaded.emit(tuple(new_tomo_objs))

    # expose API
    def setAddTomoObjCallbacks(self, *args, **kwargs):
        self._mainWidget.setAddTomoObjCallbacks(*args, **kwargs)

    def setRemoveTomoObjCallbacks(self, *args, **kwargs):
        self._mainWidget.setRemoveTomoObjCallbacks(*args, **kwargs)


class ZStitchingWindow(qt.QMainWindow):
    """
    Main widget containing all the options to define the stitching to be done

    :param bool with_configuration_action: if True append the load and save stitching configuration tool button.
                                           In some cases those can also be part of Menu so we want to avoid having those twice
    """

    sigChanged = qt.Signal()
    """Signal emit each time the configuration is modified"""

    def __init__(self, parent=None, with_configuration_action=True) -> None:
        super().__init__(parent)
        self._previewFolder = None
        # folder to store files (volume or NXtomo) for previews
        self._previewThread = None
        # thread to compute the stitching for preview
        self._callbackToGetSlurmConfig = None
        self._callbackToSetSlurmConfig = None
        # convenient work arounds to avoid having to redefine the n=interface for slurm and the API
        # to load and save settings
        # if it is defined upper

        toolbar = qt.QToolBar(self)
        self.addToolBar(qt.Qt.TopToolBarArea, toolbar)
        style = qt.QApplication.instance().style()

        # clean option
        self.__cleanAction = qt.QAction(self)
        self.__cleanAction.setToolTip("clear")
        clear_icon = style.standardIcon(qt.QStyle.SP_DialogResetButton)
        self.__cleanAction.setIcon(clear_icon)
        toolbar.addAction(self.__cleanAction)
        self.__cleanAction.triggered.connect(self.clean)

        # separator
        toolbar.addSeparator()

        if with_configuration_action:
            # load action
            self.__loadAction = stitching_action.LoadConfigurationAction(self)
            toolbar.addAction(self.__loadAction)
            self.__loadAction.triggered.connect(
                functools.partial(self._loadSettings, file_path=None)
            )

            # save action
            self.__saveAction = stitching_action.SaveConfigurationAction(self)
            toolbar.addAction(self.__saveAction)
            self.__saveAction.triggered.connect(
                functools.partial(self._saveSettings, file_path=None)
            )

            # separator
            toolbar.addSeparator()

        # update preview action
        self.__updatePreviewAction = stitching_action.PreviewAction(self)
        toolbar.addAction(self.__updatePreviewAction)
        self.__updatePreviewAction.triggered.connect(self._trigger_update_preview)

        # separator
        toolbar.addSeparator()

        # configuration level / mode
        self.__configurationModesAction = qt.QAction(self)
        self.__configurationModesAction.setCheckable(False)
        menu = qt.QMenu(self)
        self.__configurationModesAction.setMenu(menu)
        toolbar.addAction(self.__configurationModesAction)

        self.__configurationModesGroup = qt.QActionGroup(self)
        self.__configurationModesGroup.setExclusive(True)
        self.__configurationModesGroup.triggered.connect(self._userModeChanged)

        self._minimalisticAction = MinimalisticConfigurationAction(toolbar)
        menu.addAction(self._minimalisticAction)
        self.__configurationModesGroup.addAction(self._minimalisticAction)
        self._basicConfigAction = BasicConfigurationAction(toolbar)
        menu.addAction(self._basicConfigAction)
        self.__configurationModesGroup.addAction(self._basicConfigAction)
        self._expertConfiguration = ExpertConfigurationAction(toolbar)
        menu.addAction(self._expertConfiguration)
        self.__configurationModesGroup.addAction(self._expertConfiguration)

        # separator
        toolbar.addSeparator()

        # create central widget
        self._widget = ZStitchingCentralWidget(parent=self)
        self.setCentralWidget(self._widget)

        # create Dock widgets
        ##  output
        self._outputWidget = StitchingOutput(parent=self)
        self._outputWidget.setObjectName("outputSettingsWidget")
        self._outputDockWidget = qt.QDockWidget(parent=self)
        self._outputDockWidget.setWindowTitle("output")
        self._outputDockWidget.layout().setContentsMargins(0, 0, 0, 0)
        self._outputDockWidget.setFeatures(qt.QDockWidget.DockWidgetMovable)
        self._outputDockWidget.setWidget(self._outputWidget)
        self.addDockWidget(qt.Qt.RightDockWidgetArea, self._outputDockWidget)
        self._outputDockWidget.setToolTip(
            "options to where and how to save the stitching"
        )
        ##  stitching strategies
        self._stitchingOptsWidget = StitchingOptions(parent=self)
        self._stitchingOptsScrollArea = qt.QScrollArea(self)
        self._stitchingOptsScrollArea.setWidget(self._stitchingOptsWidget)
        self._stitchingOptsScrollArea.setWidgetResizable(True)
        self._stitchingOptsScrollArea.setHorizontalScrollBarPolicy(
            qt.Qt.ScrollBarAlwaysOff
        )
        self._stitchingOptsDockWidget = qt.QDockWidget(parent=self)
        self._stitchingOptsDockWidget.layout().setContentsMargins(0, 0, 0, 0)
        self._stitchingOptsDockWidget.setFeatures(qt.QDockWidget.DockWidgetMovable)
        self._stitchingOptsDockWidget.setWidget(self._stitchingOptsScrollArea)
        self._stitchingOptsDockWidget.setWindowTitle("processing options")
        self.addDockWidget(qt.Qt.RightDockWidgetArea, self._stitchingOptsDockWidget)

        ## all scan z positions
        self._editTomoObjAxis0PositionsWidget = PosEditorOverOneAxis(
            parent=self,
            axis_edited=0,
            axis_order=0,
        )
        self._editTomoObjAxis0PositionsDockWidget = qt.QDockWidget(parent=self)
        self._editTomoObjAxis0PositionsDockWidget.layout().setContentsMargins(
            0, 0, 0, 0
        )
        self._editTomoObjAxis0PositionsDockWidget.setFeatures(
            qt.QDockWidget.DockWidgetMovable
        )
        self._editTomoObjAxis0PositionsDockWidget.setWidget(
            self._editTomoObjAxis0PositionsWidget
        )
        self._editTomoObjAxis0PositionsDockWidget.setWindowTitle(
            "edit positions over axis 0 (px) - aka z"
        )
        self._editTomoObjAxis0PositionsDockWidget.setToolTip(
            "This allows to edit tomo objects positions along the axis 0 (also aka z)"
        )
        self.addDockWidget(
            qt.Qt.RightDockWidgetArea, self._editTomoObjAxis0PositionsDockWidget
        )
        ### add a check box to update position from preview if asked by the user
        self._updateAxis0PosFromPreviewCalc = qt.QCheckBox(
            "update position 0 from preview calc",
            self,
        )
        self._updateAxis0PosFromPreviewCalc.setToolTip(
            "When the user trigger a preview, if some shift search refined over axis 0 is done then will update the axis 0 positions",
        )
        self._updateAxis0PosFromPreviewCalc.setChecked(True)
        self._editTomoObjAxis0PositionsWidget.layout().insertWidget(
            0, self._updateAxis0PosFromPreviewCalc
        )

        ## all scan axis 2 positions
        self._editTomoObjAxis2PositionsWidget = PosEditorOverOneAxis(
            parent=self,
            axis_edited=2,
            axis_order=0,
        )
        self._editTomoObjAxis2PositionsDockWidget = qt.QDockWidget(parent=self)
        self._editTomoObjAxis2PositionsDockWidget.layout().setContentsMargins(
            0, 0, 0, 0
        )
        self._editTomoObjAxis2PositionsDockWidget.setFeatures(
            qt.QDockWidget.DockWidgetMovable
        )
        self._editTomoObjAxis2PositionsDockWidget.setWidget(
            self._editTomoObjAxis2PositionsWidget
        )
        self._editTomoObjAxis2PositionsDockWidget.setWindowTitle(
            "edit positions over axis 2 (px)"
        )
        self._editTomoObjAxis2PositionsDockWidget.setToolTip(
            "This allows to edit tomo objects positions along the axis 2"
        )
        self.addDockWidget(
            qt.Qt.RightDockWidgetArea, self._editTomoObjAxis2PositionsDockWidget
        )
        ### add a check box to update position from preview if asked by the user
        self._updateAxis2PosFromPreviewCalc = qt.QCheckBox(
            "update position 2 from preview calc", self
        )
        self._updateAxis2PosFromPreviewCalc.setToolTip(
            "When the user trigger a preview, if some shift search refined over axis 2 is done then will update the axis 2 positions"
        )
        self._updateAxis2PosFromPreviewCalc.setChecked(True)
        self._editTomoObjAxis2PositionsWidget.layout().insertWidget(
            0, self._updateAxis2PosFromPreviewCalc
        )

        self._widget.setAddTomoObjCallbacks(
            (
                self._editTomoObjAxis0PositionsWidget.addTomoObj,
                self._editTomoObjAxis2PositionsWidget.addTomoObj,
                self.getRawDisplayPlot().addTomoObj,
            )
        )
        self._widget.setRemoveTomoObjCallbacks(
            (
                self._editTomoObjAxis0PositionsWidget.removeTomoObj,
                self._editTomoObjAxis2PositionsWidget.removeTomoObj,
                self.getRawDisplayPlot().removeTomoObj,
            )
        )

        # update layout: for now lets tabify sime widget
        self.tabifyDockWidget(self._outputDockWidget, self._stitchingOptsDockWidget)
        self.tabifyDockWidget(
            self._outputDockWidget, self._editTomoObjAxis2PositionsDockWidget
        )
        self.tabifyDockWidget(
            self._outputDockWidget, self._editTomoObjAxis0PositionsDockWidget
        )

        # handle raw display plot. By display avoid displaying raw data as this can be ressource consuming
        self._widget._mainWidget._rawDisplayCB.setChecked(False)
        self._widget._mainWidget._rawDisplayPlot.setActive(False)

        # connect signal / slot
        self._widget._mainWidget._rawDisplayCB.toggled.connect(
            self._handleRawDisplayconnection
        )
        self._outputWidget.sigChanged.connect(self._changed)
        self._stitchingOptsWidget.sigChanged.connect(self._changed)
        self._widget.sigStitchingTypeChanged.connect(
            self._outputWidget._updateOutputForStitchingType
        )
        self._widget.sigStitchingTypeChanged.connect(
            self._stitchingOptsWidget._stitchingTypeChanged
        )

        ## handle raw plot preview
        self._stitchingOptsWidget.sigFlipLRChanged.connect(
            self.getRawDisplayPlot().setFlipLRFrames
        )
        self._stitchingOptsWidget.sigFlipUDChanged.connect(
            self.getRawDisplayPlot().setFlipUDFrames
        )
        self._stitchingOptsWidget.sigSliceForPreviewChanged.connect(
            self.getRawDisplayPlot().setSliceForPreview
        )

        ## handle tomo obj loading from settings
        self._widget.sigTomoObjsLoaded.connect(
            self._editTomoObjAxis0PositionsWidget.setTomoObjs
        )
        self._widget.sigTomoObjsLoaded.connect(
            self._editTomoObjAxis2PositionsWidget.setTomoObjs
        )
        self._widget.sigTomoObjsLoaded.connect(self.getRawDisplayPlot().setTomoObjs)

        # set up
        self._basicConfigAction.setChecked(True)
        self._userModeChanged(self._basicConfigAction)

    def setCallbackToGetSlurmConfig(self, callback):
        self._callbackToGetSlurmConfig = callback

    def setCallbackToSetSlurmConfig(self, callback):
        self._callbackToSetSlurmConfig = callback

    def close(self):
        # remove folder used for preview
        shutil.rmtree(self._previewFolder, ignore_errors=True)
        self._widget.close()
        # requested for the waiting plot update
        super().close()

    def getRawDisplayPlot(self):
        return self._widget._mainWidget._rawDisplayPlot

    def _handleRawDisplayconnection(self, toggled: bool):
        raw_display_plot = self.getRawDisplayPlot()
        raw_display_plot.setActive(toggled)

    def getPreviewAction(self):
        return self.__updatePreviewAction

    def getPreviewFolder(self):
        if self._previewFolder is None:
            self._previewFolder = tempfile.mkdtemp(prefix="tomwer_stitcher_preview")
        return self._previewFolder

    def getVolumeIdentifierPreview(self) -> HDF5VolumeIdentifier:
        folder = self.getPreviewFolder()
        # for now use hdf5 by default
        return HDF5VolumeIdentifier(
            object=HDF5Volume,
            hdf5_file=os.path.join(folder, "vol_stitching_preview.hdf5"),
            entry="my_volume",
        )

    def getNXtomoIdentifierForPreview(self):
        folder = self.getPreviewFolder()
        return NXtomoScanIdentifier(
            object=NXtomoScan,
            hdf5_file=os.path.join(folder, "nxtomo_stiching_preview.hdf5"),
            entry="entry0000",
        )

    def _changed(self, *args, **kwargs):
        self.sigChanged.emit()

    def _saveSettings(self, file_path=None, **kwargs):
        """
        dump current configuration into a txt file
        """
        # get a file if necessary
        if file_path is None:
            dialog = QConfigFileDialog(self)
            dialog.setAcceptMode(qt.QFileDialog.AcceptSave)
            if not dialog.exec_():
                return

            selected_file = dialog.selectedFiles()
            if len(selected_file) == 0:
                return
            file_path = selected_file[0]

        configuration = self.getConfiguration()
        if self._callbackToGetSlurmConfig is not None:
            slurm_config = {"slurm": self._callbackToGetSlurmConfig()}
            configuration = concatenate_dict(configuration, slurm_config)

        # dump configuration
        generate_nabu_configfile(
            fname=file_path,
            default_config=get_default_stitching_config(self.getStitchingType()),
            comments=True,
            sections_comments=_SECTIONS_COMMENTS,
            options_level="advanced",
            prefilled_values=configuration,
        )

    def _loadSettings(self, file_path=None, **kwargs):
        """
        load configuration from a txt file
        """
        # get a file if necessary
        if file_path is None:
            dialog = QConfigFileDialog(self)
            dialog.setAcceptMode(qt.QFileDialog.AcceptOpen)
            dialog.setFileMode(qt.QFileDialog.ExistingFiles)

            if not dialog.exec_():
                return

            selected_file = dialog.selectedFiles()
            if len(selected_file) == 0:
                return
            file_path = selected_file[0]

        # Do configuration load
        conf_dict = parse_nabu_config_file(file_path, allow_no_value=True)
        self.setConfiguration(config=conf_dict)
        if self._callbackToSetSlurmConfig is not None:
            self._callbackToSetSlurmConfig(conf_dict.get("slurm", {}))

    def _trigger_update_preview(self):
        if self._previewThread is not None:
            _logger.warning(
                "some preview is already running. Please wait before relaunching it"
            )
            return
        config = self.getConfiguration()
        # update the output file to set if from raw...
        stitching_type = config.get("stitching", {}).get("type", None)
        if stitching_type == "z-preproc":
            output_identifier = self.getNXtomoIdentifierForPreview()
            config["z-preproc"]["location"] = output_identifier.file_path
            config["z-preproc"]["data_path"] = output_identifier.data_path
            assert "z-postproc" not in config
        elif stitching_type == "z-postproc":
            config["z-postproc"][
                "output_volume"
            ] = self.getVolumeIdentifierPreview().to_str()
            assert "z-preproc" not in config
        else:
            raise NotImplementedError

        # update the slice to avoid doing the stitching on all the frames
        config["inputs"]["slices"] = self.getSlicesForPreview()

        # update to force overwrite
        config["output"]["overwrite_results"] = True

        # clean current preview to notify some calculation is going on
        preview_plot = self._widget._mainWidget._previewPlot
        preview_plot._waitingOverlay.show()

        # start sitching on a thread
        self._previewThread = PreviewThread(stitching_config=config)
        self._previewThread.finished.connect(self._previewCalculationFinished)
        self._previewThread.start()

    def getSlicesForPreview(self):
        return self._stitchingOptsWidget.getSlicesForPreview()

    def _previewCalculationFinished(self):
        sender = self.sender()
        assert isinstance(sender, PreviewThread)
        composition = sender.frame_composition
        tomo_objs_new_axis_positions = sender.final_tomo_objs_positions
        assert isinstance(
            tomo_objs_new_axis_positions, dict
        ), "final_tomo_objs_positions is expected to be a dict with obj identifier as key and the tuple of position as value"
        # expect it to be a dict with tomo obj identifier as key and a tuple of (axis_2_pos, axis_1_pos, axis_0_pos) as value
        output_obj_identifier = sender.output_identifier

        preview_plot = self._widget._mainWidget._previewPlot
        preview_plot._waitingOverlay.hide()

        self._previewThread.finished.disconnect(self._previewCalculationFinished)
        self._previewThread = None

        if output_obj_identifier is None:
            _logger.error("preview of stitching failed")
        else:
            preview_plot.setStitchedTomoObj(
                tomo_obj_id=output_obj_identifier,
                composition=composition,
            )

        # update object values if requested
        update_requested = {
            0: self._updateAxis0PosFromPreviewCalc.isChecked(),
            2: self._updateAxis2PosFromPreviewCalc.isChecked(),
        }

        if update_requested[0] or update_requested[2]:
            existing_tomo_obj = {
                tomo_obj.get_identifier().to_str(): tomo_obj
                for tomo_obj in self._widget._mainWidget.getTomoObjs()
            }

            for tomo_obj_id, value in tomo_objs_new_axis_positions.items():
                assert (
                    isinstance(value, tuple) and len(value) == 3
                ), "value is expected to be (new_pos_axis_0, new_pos_axis_1, new_pos_axis_2)"
                new_axis_0_pos, _, new_axis_2_pos = value
                tomo_obj = existing_tomo_obj.get(tomo_obj_id, None)
                if tomo_obj is None:
                    continue
                if update_requested[0]:
                    tomo_obj.stitching_metadata.setPxPos(int(new_axis_0_pos), 0)
                if update_requested[2]:
                    tomo_obj.stitching_metadata.setPxPos(int(new_axis_2_pos), 2)
            if update_requested[0]:
                self._editTomoObjAxis0PositionsWidget._orderedMightHavechanged(
                    force_sb_update=True
                )
            if update_requested[2]:
                self._editTomoObjAxis2PositionsWidget._orderedMightHavechanged(
                    force_sb_update=True
                )

    def clean(self):
        self._widget.clean()
        self._editTomoObjAxis0PositionsWidget.clean()
        self._editTomoObjAxis2PositionsWidget.clean()

    def setSerie(self, serie):
        self.clean()
        self._widget._mainWidget.setSerie(serie)
        self._editTomoObjAxis0PositionsWidget.clean()
        self._editTomoObjAxis2PositionsWidget.clean()
        for tomo_obj in serie:
            self._editTomoObjAxis0PositionsWidget.addTomoObj(tomo_obj)
            self._editTomoObjAxis2PositionsWidget.addTomoObj(tomo_obj)
        self.getRawDisplayPlot().setTomoObjs(tomo_objs=serie[:])

    def addTomoObj(self, tomo_obj):
        self._widget.addTomoObj(tomo_obj)
        self._editTomoObjAxis0PositionsWidget.addTomoObj(tomo_obj)
        self._editTomoObjAxis2PositionsWidget.addTomoObj(tomo_obj)
        self.getRawDisplayPlot().addTomoObj(tomo_obj=tomo_obj)

    def removeTomoObj(self, tomo_obj):
        self._widget.removeTomoObj(tomo_obj)
        self.getRawDisplayPlot().removeTomoObj(tomo_obj=tomo_obj)

    def getConfiguration(self) -> dict:
        # make sure the sync is fine between the two
        configs = (
            self._widget.getConfiguration(),
            self._outputWidget.getConfiguration(),
            self._stitchingOptsWidget.getConfiguration(),
        )
        result = {}
        for config in configs:
            result = concatenate_dict(result, config)
        return result

    def setConfiguration(self, config: dict):
        self._widget.setConfiguration(config)
        self._outputWidget.setConfiguration(config)
        self._stitchingOptsWidget.setConfiguration(config)

    # expose API
    def getStitchingType(self) -> StitchingType:
        return self._widget.getStitchingType()

    def setStitchingType(self, stitching_type: StitchingType):
        self._widget.setStitchingType(stitching_type)

    def _userModeChanged(self, action):
        self.__configurationModesAction.setIcon(action.icon())
        self.__configurationModesAction.setToolTip(action.tooltip())
        if action is self._basicConfigAction:
            level = ConfigurationLevel.OPTIONAL
        elif action is self._expertConfiguration:
            level = ConfigurationLevel.ADVANCED
        else:
            level = ConfigurationLevel.REQUIRED
        self._stitchingOptsWidget.setConfigurationLevel(level)
        self._editTomoObjAxis2PositionsDockWidget.setVisible(
            level >= ConfigurationLevel.ADVANCED
        )


def concatenate_dict(dict_1, dict_2) -> dict:
    """update dict which has dict as values. And we want concatenate those values to"""
    res = dict_1.copy()
    for key in dict_2:
        if key in dict_1:
            if key in [f"axis_{axis}_params" for axis in (0, 1, 2)]:
                res[key] = ";".join((dict_1[key], dict_2[key]))
            elif isinstance(dict_1[key], dict):
                res[key] = concatenate_dict(dict_1=dict_1[key], dict_2=dict_2[key])
            else:
                res[key].update(dict_2[key])
        else:
            res[key] = dict_2[key]
    return res


class PreviewThread(qt.QThread):
    """
    Thread to compute an overview of the stitching
    """

    def __init__(self, stitching_config: dict, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._stitching_config = dict_to_config_obj(stitching_config)
        self._output_identifier = None
        self._frame_composition = None
        self._final_tomo_objs_positions = None
        # store position of all the tomo objects (scan, volumes) used for the final stitching (after shift refinement)

    @property
    def stiching_config(self):
        return self._stitching_config

    @property
    def output_identifier(self):
        return self._output_identifier

    @property
    def frame_composition(self):
        return self._frame_composition

    @property
    def final_tomo_objs_positions(self) -> dict:
        """
        :return: dict with tomo object identifier (str) as key and a tuple of position in pixel (axis_0_pos, axis_1_pos, axis_2_pos)
        :rtype: dict
        """
        return self._final_tomo_objs_positions

    @property
    def final_axis_2_pos(self):
        return self._final_axis_2_pos

    def run(self):
        stitching_type = self.stiching_config.stitching_type
        if stitching_type.value == "z-preproc":
            stitcher = PreProcessZStitcher(configuration=self.stiching_config)
        elif stitching_type.value == "z-postproc":
            stitcher = PostProcessZStitcher(configuration=self.stiching_config)
        else:
            raise NotImplementedError
        self._output_identifier = stitcher.stitch()
        if self._output_identifier is not None:
            self._output_identifier = self._output_identifier.to_str()
        # store in cache the frame composition to be able to provide them to the PreviewPlot
        self._frame_composition = stitcher.frame_composition
        self._final_tomo_objs_positions = stitcher.get_final_axis_positions_in_px()


class _SlicesSelector(qt.QGroupBox):
    """
    Widget to determine the slices values (to be stitched)
    """

    def __init__(self, parent=None) -> None:
        super().__init__("slices", parent)
        # start interface
        self.setLayout(qt.QHBoxLayout())
        self._startSliceCB = qt.QCheckBox("start", self)
        self.layout().addWidget(self._startSliceCB)
        self._startSliceSB = qt.QSpinBox(self)
        self._startSliceSB.setMinimum(0)
        self._startSliceSB.setMaximum(9999999)
        self._startSliceSB.setValue(0)
        self.layout().addWidget(self._startSliceSB)
        # stop interface
        self._stopSliceCB = qt.QCheckBox("stop", self)
        self.layout().addWidget(self._stopSliceCB)
        self._stopSliceSB = qt.QSpinBox(self)
        self._stopSliceSB.setMinimum(-1)
        self._stopSliceSB.setMaximum(9999999)
        self._stopSliceSB.setValue(-1)
        self.layout().addWidget(self._stopSliceSB)
        # step interface
        self._stepSliceLabel = qt.QLabel("step", self)
        self.layout().addWidget(self._stepSliceLabel)
        self._stepSliceSB = qt.QSpinBox(self)
        self._stepSliceSB.setMinimum(1)
        self._stepSliceSB.setMaximum(9999999)
        self._stepSliceSB.setValue(1)
        self.layout().addWidget(self._stepSliceSB)

        # connect signal / slot
        self._startSliceCB.toggled.connect(self._startSliceSB.setDisabled)
        self._stopSliceCB.toggled.connect(self._stopSliceSB.setDisabled)

        self._startSliceCB.setChecked(True)
        self._stopSliceCB.setChecked(True)

    def getSlices(self) -> tuple:
        if self._startSliceCB.isChecked():
            start = 0
        else:
            start = self._startSliceSB.value()
        if self._stopSliceCB.isChecked():
            stop = -1
        else:
            stop = self._stopSliceSB.value()
        step = self._stepSliceSB.value()
        return (start, stop, step)

    def setSlices(self, start: int, stop: int, step: Optional[int] = None):
        start = int(start)
        stop = int(stop)
        if start == 0:
            self._startSliceCB.setChecked(True)
        else:
            self._startSliceCB.setChecked(False)
            self._startSliceSB.setValue(start)

        if stop == -1:
            self._stopSliceCB.setChecked(True)
        else:
            self._stopSliceCB.setChecked(False)
            self._stopSliceSB.setValue(stop)

        if step is not None:
            self._stepSliceSB.setValue(int(step))


class _AlignmentGroupBox(qt.QGroupBox):
    DEFAULT_PAD_MODE = "constant"

    ALIGNMENT_DOC = (
        "https://tomotools.gitlab-pages.esrf.fr/nabu/stitching/alignment.html"
    )

    DEFAULT_ALIGNMENT_AXIS_1 = AlignmentAxis1.CENTER
    DEFAULT_ALIGNMENT_AXIS_2 = AlignmentAxis2.CENTER

    _PAD_MODES = (
        "constant",  # Pads with a constant value.
        "edge",  # Pads with the edge values of array.
        "linear_ramp",  # Pads with the linear ramp between end_value and the array edge value.
        "maximum",  # Pads with the maximum value of all or part of the vector along each axis.
        "mean",  # Pads with the mean value of all or part of the vector along each axis.
        "median",  # Pads with the median value of all or part of the vector along each axis.
        "minimum",  # Pads with the minimum value of all or part of the vector along each axis.
        "reflect",  # Pads with the reflection of the vector mirrored on the first and last values of the vector along each axis.
        "symmetric",  # Pads with the reflection of the vector mirrored along the edge of the array.
        "wrap",  # Pads with the wrap of the vector along the axis. The first values are used to pad the end and the end values are used to pad the beginning.
    )

    def __init__(self, parent: qt.QWidget = None, title="alignment") -> None:
        super().__init__(title, parent)
        self.setLayout(qt.QFormLayout())

        # alignment axis 1
        self._alignmentAxis1CB = qt.QComboBox(self)
        for alignment in AlignmentAxis1.values():
            self._alignmentAxis1CB.addItem(alignment)
        self.layout().addRow("Axis 1 alignment", self._alignmentAxis1CB)
        self._alignmentAxis1CB.setToolTip(
            f"Alignment to do in case of volumes with different size over axis 1. Only possible for post-processing (reconstructed volume). See {self.ALIGNMENT_DOC} for details."
        )

        # alignment axis 2
        self._alignmentAxis2CB = qt.QComboBox(self)
        for alignment in AlignmentAxis2.values():
            self._alignmentAxis2CB.addItem(alignment)
        self.layout().addRow("Axis 2 alignment", self._alignmentAxis2CB)
        self._alignmentAxis2CB.setToolTip(
            f"Alignment to do in case of frames with different size over axis 2. See {self.ALIGNMENT_DOC} for details."
        )

        # pad mode
        self._padModeCB = qt.QComboBox(self)
        for pad_mode in self._PAD_MODES:
            self._padModeCB.addItem(pad_mode)
        self.layout().addRow("pad mode", self._padModeCB)
        self._padModeCB.setToolTip("padding mode to apply for alignment")

        # set up
        self.setAlignmentAxis1(self.DEFAULT_ALIGNMENT_AXIS_1)
        self.setAlignmentAxis2(self.DEFAULT_ALIGNMENT_AXIS_2)

    def getAlignmentAxis1(self) -> AlignmentAxis1:
        return AlignmentAxis1.from_value(self._alignmentAxis1CB.currentText())

    def setAlignmentAxis1(self, alignment: AlignmentAxis1):
        alignment = AlignmentAxis1.from_value(alignment)
        self._alignmentAxis1CB.setCurrentIndex(
            self._alignmentAxis1CB.findText(alignment.value)
        )

    def getAlignmentAxis2(self) -> AlignmentAxis2:
        return AlignmentAxis2.from_value(self._alignmentAxis2CB.currentText())

    def setAlignmentAxis2(self, alignment: AlignmentAxis2):
        alignment = AlignmentAxis2.from_value(alignment)
        self._alignmentAxis2CB.setCurrentIndex(
            self._alignmentAxis2CB.findText(alignment.value)
        )

    def getPadMode(self) -> str:
        return self._padModeCB.currentText()

    def setPadMode(self, pad_mode: str):
        idx = self._padModeCB.findText(pad_mode)
        if idx >= 0:
            self._padModeCB.setCurrentIndex(idx)

    def setAlignmentAxis1Enabled(self, enabled: bool):
        self._alignmentAxis1CB.setEnabled(enabled)


class StitchingOptions(qt.QWidget):
    """
    Widget to let the user define the different options for z-stitching such as which algorithm to search shift,
    which stitching strategy...
    """

    sigChanged = qt.Signal()
    """Signal emit when the options change"""
    sigSliceForPreviewChanged = qt.Signal(object)
    """Signal emit when the slice requested for the preview has changed. Parameter is a str or an int"""
    sigFlipLRChanged = qt.Signal(bool)
    """Signal emit when the request to flip LR frame has changed"""
    sigFlipUDChanged = qt.Signal(bool)
    """Signal emit when the request to flip UD frame has changed"""

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # stitching strategy (aka stitcher behavior)
        self.setLayout(qt.QFormLayout())
        self._stitchingStrategiesWidget = StitchingStrategies(parent=self)
        self._stitchingStrategiesWidget.setObjectName("strategy")
        self.layout().addRow(self._stitchingStrategiesWidget)
        # slice for preview
        self._previewSlices = _SliceGetter("middle", parent=self)
        self._previewSlices.setPlaceholderText(
            "slice index or one of ('middle', 'first', 'last')"
        )
        self._previewSlices.setToolTip(
            "expects a slice index (int > 0) or a str in ('first', 'middle', 'last')"
        )
        self.layout().addRow("slice for preview", self._previewSlices)

        # invert frame up - down
        self._flipLR_CB = qt.QCheckBox("flip frame left-right", self)
        self._flipLR_CB.setChecked(False)
        self._flipLR_CB.setToolTip(
            "Flip frame for stitching. This is mostly for volume has no metadata are existing to specify the direction of the frame"
        )
        self.layout().addRow(self._flipLR_CB)
        # invert frame left-right
        self._flipUD_CB = qt.QCheckBox("flip frame up-down", self)
        self._flipUD_CB.setChecked(False)
        self._flipUD_CB.setToolTip(
            "Flip frame for stitching. This is mostly for volume has no metadata are existing to specify the direction of the frame"
        )
        self.layout().addRow(self._flipUD_CB)

        # alignment options
        self._alignmentGroup = _AlignmentGroupBox(self)
        self.layout().addRow(self._alignmentGroup)

        # slices to be reconstructed
        self._slices = _SlicesSelector(parent=self)
        self._slices.setToolTip(
            "for pre processing stitchting those are projections and for post prcessing stitching those are volume slices"
        )
        self.layout().addRow(self._slices)

        # axis 0 params for shift search
        self._axis0Group = qt.QGroupBox("axis 0 (aka z)", self)
        self._axis0Group.setLayout(qt.QVBoxLayout())
        self.layout().addRow(self._axis0Group)
        self._axis0ShiftSearchParams = StitcherAxisParams(axis=0, parent=self)
        self._axis0ShiftSearchParams.layout().setContentsMargins(0, 0, 0, 0)
        self._axis0ShiftSearchParams.layout().setSpacing(0)
        self._axis0Group.layout().addWidget(self._axis0ShiftSearchParams)

        # axis 2 params for shift search
        self._axis2Group = qt.QGroupBox("axis 2 (aka x)", self)
        self._axis2Group.setLayout(qt.QVBoxLayout())
        self.layout().addRow(self._axis2Group)
        self._axis2ShiftSearchParams = StitcherAxisParams(axis=2, parent=self)
        self._axis2ShiftSearchParams.layout().setContentsMargins(0, 0, 0, 0)
        self._axis2ShiftSearchParams.layout().setSpacing(0)
        self._axis2Group.layout().addWidget(self._axis2ShiftSearchParams)
        # by default avoid doing x shift research
        self._axis2ShiftSearchParams.setShiftSearchMethod(None)

        # frame rescaling option
        self._rescalingWidget = RescalingWidget(parent=self)
        self.layout().addRow(self._rescalingWidget)

        # normalization by sample
        self._normalizationBySampleWidget = NormalizationBySampleGroupBox(parent=self)
        self._normalizationBySampleWidget.setChecked(False)
        self.layout().addRow(self._normalizationBySampleWidget)

        # connect signal / slot
        self._stitchingStrategiesWidget.sigChanged.connect(self._updated)
        self._previewSlices.editingFinished.connect(self._sliceForPreviewHasChanged)
        self._flipLR_CB.toggled.connect(self._flipLRHasChanged)
        self._flipUD_CB.toggled.connect(self._flipUDHasChanged)

    def _sliceForPreviewHasChanged(self):
        slice_for_preview = self.getSlicesForPreview()
        try:
            slice_for_preview = int(slice_for_preview)
        except ValueError:
            pass
        self.sigSliceForPreviewChanged.emit(slice_for_preview)
        self._updated()

    def _flipLRHasChanged(self):
        self.sigFlipLRChanged.emit(self._flipLR_CB.isChecked())

    def _flipUDHasChanged(self):
        self.sigFlipUDChanged.emit(self._flipUD_CB.isChecked())

    def _updated(self, *args, **kwargs):
        self.sigChanged.emit()

    def getSlicesForPreview(self):
        return self._previewSlices.text()

    def getSlices(self):
        slices = self._slices.getSlices()
        if slices == (0, -1, 1):
            return None
        else:
            return (str(slices[0]), str(slices[1]), str(slices[2]))

    def setSlices(self, slices: tuple):
        if isinstance(slices, str):
            slices = slices.replace(" ", "").split(":")
        if len(slices) > 2:
            step = int(slices[2])
        else:
            step = None
        self._slices.setSlices(int(slices[0]), int(slices[1]), step)

    def getConfiguration(self) -> dict:
        slices = self.getSlices()
        if slices is None:
            slices = ""
        else:
            slices = ":".join(slices)
        res = {
            stitching_config.STITCHING_SECTION: {
                stitching_config.FLIP_LR: self._flipLR_CB.isChecked(),
                stitching_config.FLIP_UD: self._flipUD_CB.isChecked(),
                stitching_config.ALIGNMENT_AXIS_1_FIELD: self._alignmentGroup.getAlignmentAxis1().value,
                stitching_config.ALIGNMENT_AXIS_2_FIELD: self._alignmentGroup.getAlignmentAxis2().value,
                stitching_config.PAD_MODE_FIELD: self._alignmentGroup.getPadMode(),
            },
            stitching_config.INPUTS_SECTION: {
                stitching_config.STITCHING_SLICES: slices,
            },
            stitching_config.NORMALIZATION_BY_SAMPLE_SECTION: self._normalizationBySampleWidget.getConfiguration(),
        }

        for ddict in (
            self._stitchingStrategiesWidget.getConfiguration(),
            self._axis0ShiftSearchParams.getConfiguration(),
            self._axis2ShiftSearchParams.getConfiguration(),
            self._rescalingWidget.getConfiguration(),
        ):
            res = concatenate_dict(res, ddict)
        return res

    def setConfiguration(self, config: dict):
        self._stitchingStrategiesWidget.setConfiguration(config)
        self._axis0ShiftSearchParams.setConfiguration(config)
        self._axis2ShiftSearchParams.setConfiguration(config)
        self._rescalingWidget.setConfiguration(config)
        slices = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.STITCHING_SLICES, ""
        )
        # slices
        if slices == "":
            slices = None
        if slices is not None:
            self.setSlices(slices)
        # flip_lr
        flip_lr = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.FLIP_LR, None
        )
        if flip_lr is not None:
            self._flipLR_CB.setChecked(flip_lr in (True, "True", 1, "1"))
        # flip_ud
        flip_ud = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.FLIP_UD, None
        )
        if flip_ud is not None:
            self._flipUD_CB.setChecked(flip_ud in (True, "True", 1, "1"))
        # alignment
        alignment_axis_1 = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.ALIGNMENT_AXIS_1_FIELD, None
        )
        if alignment_axis_1 is not None:
            self._alignmentGroup.setAlignmentAxis1(alignment_axis_1)
        alignment_axis_2 = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.ALIGNMENT_AXIS_2_FIELD, None
        )
        if alignment_axis_2 is not None:
            self._alignmentGroup.setAlignmentAxis2(alignment_axis_2)
        # pad_mode
        pad_mode = config.get(stitching_config.STITCHING_SECTION, {}).get(
            stitching_config.PAD_MODE_FIELD, None
        )
        if pad_mode is not None:
            self._alignmentGroup.setPadMode(pad_mode=pad_mode)

        # normalization by sample
        normalization_by_sample = config.get(
            stitching_config.NORMALIZATION_BY_SAMPLE_SECTION, None
        )
        if normalization_by_sample is not None:
            self._normalizationBySampleWidget.setConfiguration(normalization_by_sample)

    def _stitchingTypeChanged(self, stiching_type: str):
        stiching_type = StitchingType.from_value(stiching_type)
        self._alignmentGroup.setAlignmentAxis1Enabled(
            stiching_type is StitchingType.Z_POSTPROC
        )

    def setConfigurationLevel(self, level: ConfigurationLevel):
        self._alignmentGroup.setVisible(level >= ConfigurationLevel.ADVANCED)
        self._previewSlices.setVisible(level >= ConfigurationLevel.OPTIONAL)
        self._flipLR_CB.setVisible(level >= ConfigurationLevel.ADVANCED)
        self._flipUD_CB.setVisible(level >= ConfigurationLevel.ADVANCED)
        self._rescalingWidget.setVisible(level >= ConfigurationLevel.ADVANCED)
        self._axis0ShiftSearchParams.setConfigurationLevel(level)
        self._axis2ShiftSearchParams.setConfigurationLevel(level)
        self._normalizationBySampleWidget.setVisible(
            level >= ConfigurationLevel.ADVANCED
        )


class RescalingWidget(qt.QWidget):
    DEFAULT_MIN_PERCENTILE = 0

    DEFAULT_MAX_PERCENTILE = 100

    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setLayout(qt.QHBoxLayout())
        self._activatedCB = qt.QCheckBox("rescale frames", self)
        self.layout().addWidget(self._activatedCB)

        self._minPercentileQSB = qt.QSpinBox(self)
        self._minPercentileQSB.setRange(0, 100)
        self._minPercentileQSB.setPrefix("min:")
        self._minPercentileQSB.setSuffix("%")
        self._minPercentileQSB.setValue(self.DEFAULT_MIN_PERCENTILE)
        self.layout().addWidget(self._minPercentileQSB)

        self._maxPercentileQSB = qt.QSpinBox(self)
        self._maxPercentileQSB.setRange(0, 100)
        self._maxPercentileQSB.setPrefix("max:")
        self._maxPercentileQSB.setSuffix("%")
        self._maxPercentileQSB.setValue(self.DEFAULT_MAX_PERCENTILE)
        self.layout().addWidget(self._maxPercentileQSB)

        # set up
        self._activatedCB.setChecked(False)
        self._minPercentileQSB.setEnabled(False)
        self._maxPercentileQSB.setEnabled(False)

        # connect signal / slot
        self._activatedCB.toggled.connect(self._activationChanged)
        self._activatedCB.toggled.connect(self._activationChanged)

    def _activationChanged(self):
        self._minPercentileQSB.setEnabled(self._activatedCB.isChecked())
        self._maxPercentileQSB.setEnabled(self._activatedCB.isChecked())

    def getConfiguration(self):
        return {
            STITCHING_SECTION: {
                RESCALE_FRAMES: self._activatedCB.isChecked(),
                RESCALE_PARAMS: ";".join(
                    [
                        f"{KEY_RESCALE_MIN_PERCENTILES}={self._minPercentileQSB.value()}",
                        f"{KEY_RESCALE_MAX_PERCENTILES}={self._maxPercentileQSB.value()}",
                    ]
                ),
            }
        }

    def setConfiguration(self, config: dict):
        def cast_percentile(percentile) -> int:
            if isinstance(percentile, str):
                percentile.replace(" ", "").rstrip("%")
            return int(percentile)

        stitching_config = config.get(STITCHING_SECTION, {})
        rescale_params = str_to_dict(stitching_config.get(RESCALE_PARAMS, {}))
        rescale_min_percentile = rescale_params.get(KEY_RESCALE_MIN_PERCENTILES, None)
        if rescale_min_percentile is not None:
            rescale_min_percentile = cast_percentile(rescale_min_percentile)
            self._minPercentileQSB.setValue(rescale_min_percentile)
        rescale_max_percentile = rescale_params.get(KEY_RESCALE_MAX_PERCENTILES, None)
        if rescale_max_percentile is not None:
            rescale_max_percentile = cast_percentile(rescale_max_percentile)
            self._maxPercentileQSB.setValue(rescale_max_percentile)

        rescale = stitching_config.get(RESCALE_FRAMES, None)
        if rescale is not None:
            self._activatedCB.setChecked(_convert_str_to_bool(rescale))
