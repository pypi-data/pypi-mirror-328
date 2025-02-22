import enum
import logging
import os
from bisect import bisect_left
from typing import Optional, Union

import numpy
import scipy.signal
from silx.gui import qt
from silx.io.url import DataUrl
from silx.utils.deprecation import deprecated

from tomwer.core.process.reconstruction.axis import mode as axis_mode
from tomwer.core.process.reconstruction.axis.anglemode import CorAngleMode
from tomwer.core.process.reconstruction.axis.params import (
    DEFAULT_CMP_N_SUBSAMPLING_Y,
    DEFAULT_CMP_OVERSAMPLING,
    DEFAULT_CMP_TAKE_LOG,
    DEFAULT_CMP_THETA,
    AxisCalculationInput,
)
from tomwer.core.scan.scanbase import TomwerScanBase
from tomwer.core.scan.scanfactory import ScanFactory
from tomwer.core.utils import image
from tomwer.gui.utils.buttons import PadlockButton
from tomwer.gui.utils.qt_utils import block_signals
from tomwer.gui.settings import EDITING_BACKGROUND_COLOR
from tomwer.gui.utils.step import StepSizeSelectorWidget
from tomwer.synctools.axis import QAxisRP

from .CompareImages import CompareImages

_logger = logging.getLogger(__name__)


class RadioAxisWindow(qt.QMainWindow):
    """
    QMainWindow for defining the rotation axis

    :raises ValueError: given axis is not an instance of _QAxisRP
    """

    sigAxisEditionLocked = qt.Signal(bool)
    """Signal emitted when the status of the reconstruction parameters edition
    change"""

    sigLockModeChanged = qt.Signal(bool)
    """signal emitted when the lock on the mode change"""

    sigPositionChanged = qt.Signal(tuple)
    """signal emitted when the center of rotation center change"""

    def __init__(self, axis, parent=None, backend=None):
        super().__init__(parent)
        if isinstance(axis, QAxisRP):
            self.__recons_params = axis
        else:
            raise TypeError("axis should be an instance of _QAxisRP")

        self._imgA = None
        self._imgB = None
        self._shiftedImgA = None
        self._flipB = True
        """Option if we want to flip the image B"""
        self._scan = None
        self._axis_params = None
        self._lastManualFlip = None
        """Cache for the last user entry for manual flip"""
        self._lastXShift = None
        # cache to know if the x shift has changed since
        self._lastYShift = None
        # cache to know if the y shift has changed
        self._lastXOrigin = None
        # cache to know if the x origin has changed since
        self._lastYOrigin = None
        # cache to know if the y origin has changed since

        self.setWindowFlags(qt.Qt.Widget)
        self._plot = CompareImages(parent=self, backend=backend)
        self._plot.setAutoResetZoom(False)
        _mode = CompareImages.VisualizationMode.COMPOSITE_A_MINUS_B
        self._plot.setVisualizationMode(_mode)
        self._plot.setAlignmentMode(CompareImages.AlignmentMode.STRETCH)
        self.setCentralWidget(self._plot)

        self._dockWidgetCtrl = qt.QDockWidget(parent=self)
        self._dockWidgetCtrl.layout().setContentsMargins(0, 0, 0, 0)
        self._dockWidgetCtrl.setFeatures(qt.QDockWidget.DockWidgetMovable)
        self._controlWidget = _AxisManual(
            parent=self, reconsParams=self.__recons_params
        )
        self._controlWidgetScrollArea = qt.QScrollArea(self)
        self._controlWidgetScrollArea.setWidgetResizable(True)
        self._controlWidgetScrollArea.setWidget(self._controlWidget)
        self._dockWidgetCtrl.setWidget(self._controlWidgetScrollArea)
        self.addDockWidget(qt.Qt.RightDockWidgetArea, self._dockWidgetCtrl)

        # expose API
        self.getXShift = self._controlWidget.getXShift
        self.getYShift = self._controlWidget.getYShift
        self._setShift = self._controlWidget.setShift
        self.setXShift = self._controlWidget.setXShift
        self.setYShift = self._controlWidget.setYShift
        self.getShiftStep = self._controlWidget.getShiftStep
        self.setShiftStep = self._controlWidget.setShiftStep
        self.getAxis = self._controlWidget.getAxis
        self.getMode = self._controlWidget.getMode
        self.setModeLock = self._controlWidget.setModeLock

        # signal / slot connection
        self._controlWidget.sigShiftChanged.connect(self._updateShift)
        self._controlWidget.sigShiftChanged.connect(self._corChanged)
        self._controlWidget.sigRoiChanged.connect(self._updateShift)
        self._controlWidget.sigAuto.connect(self._updateAuto)
        self._controlWidget.sigModeChanged.connect(self.setMode)
        self._controlWidget.sigModeLockChanged.connect(self._modeLockChanged)
        self._controlWidget.sigResetZoomRequested.connect(self._resetZoomPlot)
        self._controlWidget.sigSubsamplingChanged.connect(self._updateSubSampling)
        self._controlWidget.sigUrlChanged.connect(self._urlChanged)
        self._plot.sigCropImagesChanged.connect(self._updateShift)

        # adapt gui to the axis value
        self.setReconsParams(axis=self.__recons_params)
        self.getPlot().getPlot().setAxesDisplayed(True)

    def manual_uses_full_image(self, value):
        self._controlWidget.manual_uses_full_image(value)

    def _modeLockChanged(self, lock):
        self.sigLockModeChanged.emit(lock)

    def _corChanged(self):
        self.sigPositionChanged.emit((self.getXShift(), self.getYShift()))

    def getPlot(self):
        return self._plot

    def _resetZoomPlot(self):
        self._plot.getPlot().resetZoom()

    def getSettingsWidget(self):
        return self._controlWidgetScrollArea

    def getSettingsWidgetDocker(self):
        return self._dockWidgetCtrl

    def setMode(self, mode):
        """
        Define the mode to use for radio axis

        :param mode:
        :return:
        """
        mode = axis_mode.AxisMode.from_value(mode)
        with block_signals(self._controlWidget):
            with block_signals(self._axis_params):
                self._controlWidget.setMode(mode)
                if mode is axis_mode.AxisMode.manual:
                    self._setModeLockFrmSettings(False)

    def updateAutomaticallyEstimatedCor(self):
        return self._controlWidget.updateAutomaticallyEstimatedCor()

    def setUpdateAutomaticallyEstimatedCor(self, value):
        self._controlWidget.setUpdateAutomaticallyEstimatedCor(value)

    def setEstimatedCor(self, value):
        self._controlWidget.setEstimatedCor(value=value)

    def getEstimatedCor(self):
        return self._controlWidget.getEstimatedCor()

    def _setModeLockFrmSettings(self, lock: bool):
        # only lock the push button
        with block_signals(self):
            self._controlWidget._mainWidget._calculationWidget._lockMethodPB.setLock(
                lock
            )

    def getROIDims(self):
        if self.getMode() == axis_mode.AxisMode.manual:
            return self._controlWidget.getROIDims()
        else:
            return None

    def getROIOrigin(self):
        if self.getMode() == axis_mode.AxisMode.manual:
            return self._controlWidget.getROIOrigin()
        else:
            return None

    def getImgSubsampling(self):
        return self._controlWidget.getImgSubsampling()

    def _computationRequested(self):
        self.sigComputationRequested.emit()

    def setLocked(self, locked):
        with block_signals(self):
            if self._axis_params.mode not in (
                axis_mode.AxisMode.read,
                axis_mode.AxisMode.manual,
            ):
                self._axis_params.mode = axis_mode.AxisMode.manual
            self._controlWidget.setLocked(locked)

        self.sigAxisEditionLocked.emit(locked)

    def isModeLock(self):
        return self._controlWidget.isModeLock()

    def _validated(self):
        """callback when the validate button is activated"""
        self.sigApply.emit()

    def _setRadio2Flip(self, checked):
        self._plot.setRadio2Flip(checked)

    def _flipChanged(self, checked):
        if self.getMode() == axis_mode.AxisMode.manual:
            self._lastManualFlip = self._plot.isRadio2Flip()

        if checked == self._flipB:
            return
        else:
            self._flipB = checked
            self._updatePlot()

    def setReconsParams(self, axis):
        """

        :param AxisRP axis: axis to edit
        :return:
        """
        assert isinstance(axis, QAxisRP)
        self._axis_params = axis
        with block_signals(self):
            self.resetShift()
            self._controlWidget.setAxis(axis)

    def setScan(self, scan):
        """
        Update the interface concerning the given scan. Try to display the
        radios for angle 0 and 180.

        :param scan: scan for which we want the axis updated.
        :type scan: Union[str, tomwer.core.scan.TomoBase]
        """
        self.clear()
        _scan = scan
        if type(scan) is str:
            try:
                _scan = ScanFactory.create_scan_object(scan)
            except ValueError:
                raise ValueError("Fail to discover a valid scan in %s" % scan)
        elif not isinstance(_scan, TomwerScanBase):
            raise ValueError(
                f"type of {scan} ({type(scan)}) is invalid, scan should be a file/dir path or an instance of ScanBase"
            )
        assert isinstance(_scan, TomwerScanBase)

        if _scan.axis_params is None:
            _scan.axis_params = QAxisRP()

        if self._scan is not None:
            self._scan.axis_params.sigAxisUrlChanged.disconnect(self._updatePlot)
        if (
            scan.estimated_cor_frm_motor is not None
            and self.updateAutomaticallyEstimatedCor()
        ):
            self.setEstimatedCor(scan.estimated_cor_frm_motor)

        # update visualization
        self._scan = _scan
        self._scan.axis_params.sigAxisUrlChanged.connect(self._updatePlot)
        self._controlWidget.setScan(scan=self._scan)
        self._updatePlot()
        self.getPlot().getPlot().resetZoom()

    def _updatePlot(self):
        if self._scan is None:
            return
        self._urlChanged()

    def _urlChanged(self):
        with block_signals(self):
            coreAngleMode = CorAngleMode.from_value(self.__recons_params.angle_mode)
            if self._scan is None:
                return
            axis_rp = self._scan.axis_params
            if coreAngleMode is CorAngleMode.manual_selection:
                manual_sel_widget = (
                    self._controlWidget._mainWidget._inputWidget._angleModeWidget._manualFrameSelection
                )
                urls = manual_sel_widget.getFramesUrl(as_txt=False)
                axis_rp.axis_url_1, axis_rp.axis_url_2 = urls
                axis_rp.flip_lr = manual_sel_widget.isFrame2LRFLip()
            else:
                axis_rp.flip_lr = True
                res = self._scan.get_opposite_projections(mode=coreAngleMode)
                axis_rp.axis_url_1 = res[0]
                axis_rp.axis_url_2 = res[1]

            if axis_rp.n_url() < 2:
                _logger.error("Fail to detect radio for axis calculation")
            elif axis_rp.axis_url_1.url:
                # if necessary normalize data
                axis_rp.axis_url_1.normalize_data(self._scan, log_=False)
                axis_rp.axis_url_2.normalize_data(self._scan, log_=False)

                paganin = self.__recons_params.paganin_preproc
                # check if normed
                if paganin:
                    imgA = axis_rp.axis_url_1.normalized_data_paganin
                    imgB = axis_rp.axis_url_2.normalized_data_paganin
                else:
                    imgA = axis_rp.axis_url_1.normalized_data
                    imgB = axis_rp.axis_url_2.normalized_data
                assert imgA is not None
                assert imgB is not None
                self.setImages(imgA=imgA, imgB=imgB, flipB=axis_rp.flip_lr)
            else:
                _logger.error(
                    "fail to find radios for angle 0 and 180. Unable to update axis gui"
                )

    def clear(self):
        if self._scan is not None:
            self._scan.axis_params.sigAxisUrlChanged.disconnect(self._updatePlot)
        self._scan = None

    def setImages(self, imgA, imgB, flipB):
        """

        :warning: does not reset the shift when change images

        :param numpy.array imgA: first image to compare. Will be the one shifted
        :param numpy.array imgB: second image to compare
        :param bool flipB: True if the image B has to be flipped
        :param bool paganin: True to apply paganin phase retrieval
        """
        assert imgA is not None
        assert imgB is not None
        _imgA = imgA
        _imgB = imgB

        if _imgA.shape != _imgB.shape:
            _logger.error(
                "The two provided images have incoherent shapes "
                f"({_imgA.shape} vs {_imgB.shape})"
            )
        elif _imgA.ndim != 2:
            _logger.error("Image shape are not 2 dimensional")
        else:
            self._imgA = _imgA
            self._imgB = _imgB
            self._flipB = flipB

            self._controlWidget._roiControl.setLimits(
                width=self._imgA.shape[1], height=self._imgA.shape[0]
            )
            self._updateShift()

    def _updateSubSampling(self):
        self._updateShift()
        self.getPlot().getPlot().resetZoom()

    def _updateShift(self, xShift=None, yShift=None):
        if self._imgA is None or self._imgB is None:
            return
        xShift = xShift or self.getXShift()
        yShift = yShift or self.getYShift()

        # TODO: we might avoid flipping image at each new x_shift...
        _imgA, _imgB = self._getRawImages()
        # apply shift
        if xShift == 0.0 and yShift == 0.0:
            self._shiftedImgA = _imgA
            self._shiftedImgB = _imgB
        else:
            try:
                cval_imgA = _imgA.min()
                cval_imgB = _imgB.min()
            except ValueError:
                _logger.warning("enable to retrieve imgA.min() and / or" "imgB.min().")
                cval_imgA = 0
                cval_imgB = 0
            try:
                x_shift = self.getXShift() / self.getImgSubsampling()
                y_shift = self.getYShift() / self.getImgSubsampling()
                self._shiftedImgA = image.shift_img(
                    data=_imgA,
                    dx=-x_shift,
                    dy=y_shift,
                    cval=cval_imgA,
                )
                self._shiftedImgB = image.shift_img(
                    data=_imgB,
                    dx=x_shift,
                    dy=y_shift,
                    cval=cval_imgB,
                )
                crop = self.getPlot().cropComparedImages()

                if not crop:
                    # handling of the crop:
                    # 1. we will concatenate the shifted array with the unshifted to avoid crop
                    # 2. in order to handled properly the shift and overlaps we need to add an empty array
                    abs_x_shift = abs(int(x_shift))
                    buffer_array_img_A = numpy.full(
                        shape=(self._shiftedImgA.shape[0], abs_x_shift),
                        fill_value=cval_imgA,
                    )
                    buffer_array_img_B = numpy.full(
                        shape=(self._shiftedImgB.shape[0], abs_x_shift),
                        fill_value=cval_imgB,
                    )
                    if x_shift == 0:
                        pass
                    elif x_shift > 0:
                        self._shiftedImgA = numpy.concatenate(
                            (
                                _imgA[:, :abs_x_shift],
                                self._shiftedImgA,
                                buffer_array_img_A,
                            ),
                            axis=1,
                        )
                        self._shiftedImgB = numpy.concatenate(
                            (
                                buffer_array_img_B,
                                self._shiftedImgB,
                                _imgB[:, -abs_x_shift:],
                            ),
                            axis=1,
                        )
                    else:
                        self._shiftedImgA = numpy.concatenate(
                            (
                                buffer_array_img_A,
                                self._shiftedImgA,
                                _imgA[:, :abs_x_shift],
                            ),
                            axis=1,
                        )
                        self._shiftedImgB = numpy.concatenate(
                            (
                                _imgB[:, :abs_x_shift],
                                self._shiftedImgB,
                                buffer_array_img_B,
                            ),
                            axis=1,
                        )
            except ValueError as e:
                _logger.error(e)
                self._shiftedImgA = _imgA
                self._shiftedImgB = _imgB

        with block_signals(self):
            try:
                self._plot.setData(
                    image1=self._shiftedImgA,
                    image2=self._shiftedImgB,
                )
            except ValueError:
                _logger.warning(
                    "Unable to set images. Maybe there is some "
                    "incomplete dataset or an issue with "
                    "normalization."
                )
            roi_origin = self.getROIOrigin()
            if roi_origin is not None:
                x_origin, y_origin = roi_origin
            else:
                x_origin = y_origin = None
            self._lastXShift = xShift
            self._lastYShift = yShift
            self._lastXOrigin = x_origin
            self._lastYOrigin = y_origin

    def _getRawImages(self):
        def selectROI(data, width, height, x_origin, y_origin, subsampling):
            assert subsampling > 0
            x_min = x_origin - width // 2
            x_max = x_origin + width // 2
            y_min = y_origin - height // 2
            y_max = y_origin + height // 2
            return data[y_min:y_max:subsampling, x_min:x_max:subsampling]

        # get images and apply ROI if any
        _roi_dims = self.getROIDims()
        _origin = self.getROIOrigin()
        subsampling = self.getImgSubsampling()
        _imgA = self._imgA
        _imgB = self._imgB
        # flip image B
        _imgB = numpy.fliplr(_imgB) if self._flipB else _imgB
        if _roi_dims is not None:
            assert type(_roi_dims) is tuple, f"invalide roi value {_roi_dims}"
            _imgA = selectROI(
                _imgA,
                width=_roi_dims[0],
                height=_roi_dims[1],
                x_origin=_origin[0],
                y_origin=_origin[1],
                subsampling=subsampling,
            )
            _imgB = selectROI(
                _imgB,
                width=_roi_dims[0],
                height=_roi_dims[1],
                x_origin=_origin[0],
                y_origin=_origin[1],
                subsampling=subsampling,
            )
        return _imgA, _imgB

    def _updateAuto(self):
        _imgA, _imgB = self._getRawImages()
        correlation = scipy.signal.correlate2d(in1=_imgA, in2=_imgB)
        y, x = numpy.unravel_index(numpy.argmax(correlation), correlation.shape)
        self._setShift(x=x, y=y)

    def resetShift(self):
        with block_signals(self._controlWidget):
            self._controlWidget.reset()
        if self._imgA is not None and self._imgB is not None:
            self.setImages(imgA=self._imgA, imgB=self._imgB, flipB=self._flipB)


class _AxisRead(qt.QWidget):
    """Widget to select a position value from a file"""

    sigFileChanged = qt.Signal(str)

    def __init__(self, parent, axis=None):
        qt.QWidget.__init__(self, parent)
        self._axis = None
        if axis:
            self.setAxis(axis)
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(qt.QLabel("File", parent=self))
        self._filePathQLE = qt.QLineEdit("", parent=self)
        self.layout().addWidget(self._filePathQLE)
        self._fileSelPB = qt.QPushButton("select", parent=self)
        self.layout().addWidget(self._fileSelPB)

        # connect signal / slot
        self._fileSelPB.pressed.connect(self._selectFile)
        self._filePathQLE.textChanged.connect(self._fileChanged)

    def setAxis(self, axis):
        assert isinstance(axis, QAxisRP)
        self._axis = axis

    def _selectFile(self):  # pragma: no cover
        dialog = qt.QFileDialog(self)
        dialog.setFileMode(qt.QFileDialog.ExistingFile)

        if not dialog.exec_():
            dialog.close()
            return

        _file_path = dialog.selectedFiles()[0]
        _logger.info("user select file %s for reading position value" % _file_path)
        self._filePathQLE.setText(dialog.selectedFiles()[0])

    def _fileChanged(self, file_path):
        """callback when the line edit (containing the file path) changed"""
        if self._axis and os.path.isfile(file_path):
            self._axis.set_position_frm_par_file(file_path, force=True)


class _AxisManual(qt.QWidget):
    """
    Widget to define the shift to apply on an image
    """

    sigShiftChanged = qt.Signal(float, float)
    """Signal emitted when requested shift changed. Parameter is x, y"""

    sigModeLockChanged = qt.Signal(bool)
    """Signal emitted when the mode is lock or unlock"""

    sigResetZoomRequested = qt.Signal()
    """Signal emitted when request a zoom reset from the plot"""

    sigSubsamplingChanged = qt.Signal()
    """Signal emitted when subsampling change"""

    sigUrlChanged = qt.Signal()
    """Signal emit when frames urls changed"""

    def __init__(self, parent, reconsParams):
        assert isinstance(reconsParams, QAxisRP)
        qt.QWidget.__init__(self, parent)
        self._xShift = 0
        self._yShift = 0
        self._recons_params = reconsParams or QAxisRP()
        self._axis = None

        self.setLayout(qt.QVBoxLayout())

        self._manualSelectionWidget = _AxisManualSelection(
            parent=self, shift_mode=ShiftMode.x_only
        )
        self._manualSelectionWidget.layout().setContentsMargins(0, 0, 0, 0)

        self._readFileSelWidget = _AxisRead(parent=self)
        self._readFileSelWidget.layout().setContentsMargins(0, 0, 0, 0)

        self._displacementSelector = self._manualSelectionWidget._displacementSelector
        self._shiftControl = self._manualSelectionWidget._shiftControl
        self._roiControl = self._manualSelectionWidget._roiControl
        self._imgOpts = self._manualSelectionWidget._imgOpts

        self._mainWidget = AxisTabWidget(
            parent=self,
            mode_dependant_widget=self._manualSelectionWidget,
            read_file_sel_widget=self._readFileSelWidget,
            recons_params=self._recons_params,
        )

        self.layout().addWidget(self._mainWidget)

        # signal / slot connection
        self._shiftControl.sigShiftLeft.connect(self._incrementLeftShift)
        self._shiftControl.sigShiftRight.connect(self._incrementRightShift)
        self._shiftControl.sigShiftTop.connect(self._incrementTopShift)
        self._shiftControl.sigShiftBottom.connect(self._incrementBottomShift)
        self._shiftControl.sigReset.connect(self._resetShift)
        self._shiftControl.sigShiftChanged.connect(self._setShiftAndSignal)
        self._mainWidget.sigLockModeChanged.connect(self._modeLockChanged)
        self._manualSelectionWidget.sigResetZoomRequested.connect(
            self._requestZoomReset
        )
        self._imgOpts.sigSubsamplingChanged.connect(self.sigSubsamplingChanged)
        self._mainWidget.sigUrlChanged.connect(self.sigUrlChanged)

        # expose API
        self.getShiftStep = self._displacementSelector.getStepSize
        self.setShiftStep = self._displacementSelector.setStepSize
        self.sigRoiChanged = self._roiControl.sigRoiChanged
        self.sigAuto = self._shiftControl.sigAuto
        self.getROIOrigin = self._roiControl.getROIOrigin
        self.getImgSubsampling = self._imgOpts.getSubsampling
        self.getMode = self._mainWidget.getMode
        self.sigModeChanged = self._mainWidget.sigModeChanged
        self.isModeLock = self._mainWidget.isModeLock
        self.setModeLock = self._mainWidget.setModeLock

        # set up interface
        self.setAxis(self._recons_params)

    def setScan(self, scan):
        self._mainWidget.setScan(scan=scan)
        self._roiControl.setScan(scan=scan)

    def manual_uses_full_image(self, value):
        self._roiControl.manual_uses_full_image(value)

    def _incrementLeftShift(self):
        self._incrementShift("left")

    def _incrementRightShift(self):
        self._incrementShift("right")

    def _incrementTopShift(self):
        self._incrementShift("top")

    def _incrementBottomShift(self):
        self._incrementShift("bottom")

    def _setShiftAndSignal(self, x, y):
        if x == self._xShift and y == self._yShift:
            return
        self.setShift(x, y)
        self._shiftControl._updateShiftInfo(x=x, y=y)
        self.sigShiftChanged.emit(x, y)

    def setAxis(self, axis):
        if axis == self._axis:
            return
        assert isinstance(axis, QAxisRP)
        with block_signals(self):
            if self._axis:
                self._axis.sigChanged.disconnect(self._updateAxisView)
            self._axis = axis
            self.setXShift(self._axis.relative_cor_value)
            self._mainWidget.setAxisParams(self._axis)
            self._readFileSelWidget.setAxis(self._axis)
            self._updateAxisView()
            self._axis.sigChanged.connect(self._updateAxisView)

    def _modeLockChanged(self, lock):
        self.sigModeLockChanged.emit(lock)

    def setMode(self, mode):
        with block_signals(self._axis):
            self._axis.mode = mode
            self._mainWidget._calculationWidget.setMode(mode)
            self._updateAxisView()
        self._axis.sigChanged.emit()

    def updateAutomaticallyEstimatedCor(self):
        return self._mainWidget.updateAutomaticallyEstimatedCor()

    def setUpdateAutomaticallyEstimatedCor(self, value):
        self._mainWidget.setUpdateAutomaticallyEstimatedCor(value)

    def setEstimatedCor(self, value):
        self._mainWidget.setEstimatedCorValue(value=value)

    def getEstimatedCor(self):
        return self._mainWidget.getEstimatedCor()

    def _updateAxisView(self):
        with block_signals(self._axis):
            if self._axis.relative_cor_value not in (None, "..."):
                self.setXShift(self._axis.relative_cor_value)

        self._manualSelectionWidget.setVisible(
            self._axis.mode is axis_mode.AxisMode.manual
        )
        self._readFileSelWidget.setVisible(self._axis.mode is axis_mode.AxisMode.read)

    def getAxis(self):
        return self._axis

    def _incrementShift(self, direction):
        assert direction in ("left", "right", "top", "bottom")
        if direction == "left":
            self.setXShift(self._xShift - self.getShiftStep())
        elif direction == "right":
            self.setXShift(self._xShift + self.getShiftStep())
        elif direction == "top":
            self.setYShift(self._yShift + self.getShiftStep())
        else:
            self.setYShift(self._yShift - self.getShiftStep())

        self._shiftControl._updateShiftInfo(x=self._xShift, y=self._yShift)

    def _resetShift(self):
        with block_signals(self._axis):
            self.setXShift(0)
            self.setYShift(0)
            self._shiftControl._updateShiftInfo(x=self._xShift, y=self._yShift)

        self.sigShiftChanged.emit(self._xShift, self._yShift)

    def getXShift(self):
        if self._xShift == "...":
            return 0
        return self._xShift

    def getYShift(self):
        if self._yShift == "...":
            return 0
        return self._yShift

    def setXShift(self, x: float):
        self.setShift(x=x, y=self._yShift)

    def setYShift(self, y):
        self.setShift(x=self._xShift, y=y)

    def setShift(self, x, y):
        if x == self._xShift and y == self._yShift:
            return
        self._xShift = x if x is not None else 0.0
        self._yShift = y if y is not None else 0.0
        if self._axis:
            with block_signals(self._axis):
                self._axis.set_relative_value(x)
        self._shiftControl._updateShiftInfo(x=self._xShift, y=self._yShift)
        if not isinstance(self._xShift, str):
            # filter `...` and `?` values (used for issues or processing)
            self.sigShiftChanged.emit(self._xShift, self._yShift)

    def reset(self):
        with block_signals(self):
            self.setShift(0, 0)
        self.sigShiftChanged.emit(self._xShift, self._yShift)

    def setLocked(self, locked):
        self._mainWidget.setEnabled(not locked)

    def _requestZoomReset(self):
        self.sigResetZoomRequested.emit()

    def getROIDims(self):
        return self._roiControl.getROIDims()


class _AxisManualSelection(qt.QWidget):
    sigResetZoomRequested = qt.Signal()
    """Signal emitted when a zoom request is necessary (when change to full
    image)"""

    def __init__(self, parent, shift_mode):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QVBoxLayout())
        self._displacementSelector = StepSizeSelectorWidget(
            parent=self,
            fine_value=0.1,
            medium_value=1.0,
            rough_value=None,
            dtype=float,
        )
        self.layout().addWidget(self._displacementSelector)

        self._shiftControl = _ShiftControl(parent=self, shift_mode=shift_mode)
        self.layout().addWidget(self._shiftControl)

        self._roiControl = _ROIControl(parent=self)
        self.layout().addWidget(self._roiControl)

        self._imgOpts = _ImgOpts(parent=self)
        self.layout().addWidget(self._imgOpts)

        # connect signal / slot
        self._roiControl.sigResetZoomRequested.connect(self.sigResetZoomRequested)


class _ROIControl(qt.QGroupBox):
    """
    Widget used to define the ROI on images to compare
    """

    sigRoiChanged = qt.Signal(object)
    """Signal emitted when the ROI changed"""
    sigResetZoomRequested = qt.Signal()
    """Signal emitted when a zoom request is necessary (when change to full
    image)"""

    def __init__(self, parent):
        qt.QGroupBox.__init__(self, "ROI selection", parent)
        self.setLayout(qt.QVBoxLayout())

        self._buttonGrp = qt.QButtonGroup(parent=self)
        self._buttonGrp.setExclusive(True)

        self._roiWidget = qt.QWidget(parent=self)
        self._roiWidget.setLayout(qt.QHBoxLayout())
        self._roiWidget.layout().setContentsMargins(0, 0, 0, 0)
        self._fullImgButton = qt.QRadioButton("full image", parent=self)
        self._buttonGrp.addButton(self._fullImgButton)
        self.layout().addWidget(self._fullImgButton)
        self._roiButton = qt.QRadioButton("ROI", parent=self._roiWidget)
        self._roiWidget.layout().addWidget(self._roiButton)
        self._buttonGrp.addButton(self._roiButton)
        self._roiDefinition = _ROIDefinition(parent=self)
        self._roiWidget.layout().addWidget(self._roiDefinition)
        self.layout().addWidget(self._roiWidget)

        # connect signal / Slot
        self._roiButton.toggled.connect(self._roiDefinition.setEnabled)
        self._fullImgButton.toggled.connect(self.sigResetZoomRequested)
        self._roiButton.toggled.connect(self.sigResetZoomRequested)

        # expose API
        self.sigRoiChanged = self._roiDefinition.sigRoiChanged
        self.getROIOrigin = self._roiDefinition.getROIOrigin
        self.setLimits = self._roiDefinition.setLimits
        self.setScan = self._roiDefinition.setScan

        # setup for full image
        self._fullImgButton.setChecked(True)

    def getROIDims(self):
        if self._roiButton.isChecked():
            return self._roiDefinition.getROIDims()
        else:
            return None

    def manual_uses_full_image(self, activate):
        if activate:
            self._fullImgButton.setChecked(True)
        else:
            self._roiButton.setChecked(True)


class _ROIDefinition(qt.QWidget):
    """
    Widget used to define ROI width and height.

    :note: emit ROI == None if setDisabled
    """

    sigRoiChanged = qt.Signal(object)
    """Signal emitted when the ROI changed"""

    def __init__(self, parent):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QGridLayout())
        self._already_set = False

        # width & height
        self.layout().addWidget(qt.QLabel("dims", self), 0, 0)
        self._widthSB = qt.QSpinBox(parent=self)
        self._widthSB.setSingleStep(2)
        self._widthSB.setMaximum(10000)
        self._widthSB.setSuffix(" px")
        self._widthSB.setPrefix("w: ")
        self._widthSB.setToolTip("ROI width")
        self.layout().addWidget(self._widthSB, 0, 1)
        self._heightSB = qt.QSpinBox(parent=self)
        self._heightSB.setSingleStep(2)
        self._heightSB.setSuffix(" px")
        self._heightSB.setPrefix("h: ")
        self._heightSB.setToolTip("ROI height")
        self._heightSB.setMaximum(10000)
        self.layout().addWidget(self._heightSB, 0, 2)

        # origin x and y position
        self.layout().addWidget(qt.QLabel("origin", self), 1, 0)
        self._xOriginSB = qt.QSpinBox(parent=self)
        self._xOriginSB.setSingleStep(10)
        self._xOriginSB.setMaximum(10000)
        self._xOriginSB.setPrefix("x: ")
        self.layout().addWidget(self._xOriginSB, 1, 1)
        self._yOriginSB = qt.QSpinBox(parent=self)
        self._yOriginSB.setSingleStep(10)
        self._yOriginSB.setPrefix("y: ")
        self._yOriginSB.setMaximum(10000)
        self.layout().addWidget(self._yOriginSB, 1, 2)

        # Signal / Slot connection
        self._widthSB.editingFinished.connect(self.__roiChanged)
        self._heightSB.editingFinished.connect(self.__roiChanged)
        self._xOriginSB.editingFinished.connect(self.__roiChanged)
        self._yOriginSB.editingFinished.connect(self.__roiChanged)

    def __roiChanged(self, *args, **kwargs):
        self.sigRoiChanged.emit((self.getROIDims(), self.getROIOrigin()))

    def setLimits(self, width, height):
        """

        :param int x: width maximum value
        :param int height: height maximum value
        """
        for spinButton in (self._widthSB, self._heightSB):
            spinButton.blockSignals(True)
        assert type(width) is int
        assert type(height) is int
        valueChanged = False
        if self._widthSB.value() > width:
            self._widthSB.setValue(width)
            valueChanged = True
        if self._heightSB.value() > height:
            self._heightSB.setValue(height)
            valueChanged = True

        # if this is the first limit definition, propose default width and
        # height
        if self._widthSB.value() == 0:
            self._widthSB.setValue(min(256, width))
            valueChanged = True
        if self._heightSB.value() == 0:
            self._heightSB.setValue(min(256, height))
            valueChanged = True

        # define minimum / maximum
        self._widthSB.setRange(1, width)
        self._heightSB.setRange(1, height)
        for spinButton in (self._widthSB, self._heightSB):
            spinButton.blockSignals(False)
        if valueChanged is True:
            self.__roiChanged()

    def getROIDims(self):
        """

        :return: (width, height) or None
        :rtype: Union[None, tuple]
        """
        if self.isEnabled():
            return (self._widthSB.value(), self._heightSB.value())
        else:
            return None

    def getROIOrigin(self):
        return (self._xOriginSB.value(), self._yOriginSB.value())

    def setEnabled(self, *arg, **kwargs):
        qt.QWidget.setEnabled(self, *arg, **kwargs)
        self.__roiChanged()

    def setScan(self, scan):
        if not self._already_set:
            self._already_set = True
            try:
                x_origin = scan.dim_1 // 2
                y_origin = scan.dim_2 // 2
                self._xOriginSB.setValue(x_origin)
                self._yOriginSB.setValue(y_origin)
            except Exception:
                _logger.warning(f"unable to determine origin for {scan}")


@enum.unique
class ShiftMode(enum.Enum):
    x_only = 0
    y_only = 1
    x_and_y = 2


class _ShiftControl(qt.QWidget):
    """
    Widget to control the shift step we want to apply
    """

    sigShiftLeft = qt.Signal()
    """Signal emitted when the left button is activated"""
    sigShiftRight = qt.Signal()
    """Signal emitted when the right button is activated"""
    sigShiftTop = qt.Signal()
    """Signal emitted when the top button is activated"""
    sigShiftBottom = qt.Signal()
    """Signal emitted when the bottom button is activated"""
    sigReset = qt.Signal()
    """Signal emitted when the reset button is activated"""
    sigAuto = qt.Signal()
    """Signal emitted when the auto button is activated"""
    sigShiftChanged = qt.Signal(float, float)
    """Signal emitted ony when xLE and yLE edition is finished"""

    def __init__(self, parent, shift_mode):
        """

        :param parent: qt.QWidget
        :param ShiftMode shift_mode: what are the shift we want to control
        """
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self._leftButton = qt.QPushButton("left", parent=self)
        self.layout().addWidget(self._leftButton, 1, 0)

        self._rightButton = qt.QPushButton("right", parent=self)
        self.layout().addWidget(self._rightButton, 1, 3)

        self._shiftInfo = _ShiftInformation(parent=self)
        self.layout().addWidget(self._shiftInfo, 1, 1)
        self._shiftInfo._updateShiftInfo(x=0.0, y=0.0)

        self._topButton = qt.QPushButton("top", parent=self)
        self.layout().addWidget(self._topButton, 0, 1)

        self._bottomButton = qt.QPushButton("bottom", parent=self)
        self.layout().addWidget(self._bottomButton, 2, 1)

        self._resetButton = qt.QPushButton("reset", parent=self)
        self.layout().addWidget(self._resetButton, 3, 2, 3, 4)

        self._autoButton = qt.QPushButton("auto", parent=self)
        self.layout().addWidget(self._autoButton, 3, 0, 3, 2)
        self._autoButton.hide()

        # Signal / Slot connection
        self._leftButton.pressed.connect(self.sigShiftLeft.emit)
        self._rightButton.pressed.connect(self.sigShiftRight.emit)
        self._topButton.pressed.connect(self.sigShiftTop.emit)
        self._bottomButton.pressed.connect(self.sigShiftBottom.emit)
        self._resetButton.pressed.connect(self.sigReset.emit)
        self._autoButton.pressed.connect(self.sigAuto.emit)
        self._shiftInfo.sigShiftChanged.connect(self.sigShiftChanged.emit)

        # expose API
        self._updateShiftInfo = self._shiftInfo._updateShiftInfo

        self.setShiftMode(shift_mode)

    def setShiftMode(self, shift_mode):
        show_x_shift = shift_mode in (ShiftMode.x_only, ShiftMode.x_and_y)
        show_y_shift = shift_mode in (ShiftMode.y_only, ShiftMode.x_and_y)
        self._leftButton.setVisible(show_x_shift)
        self._rightButton.setVisible(show_x_shift)
        self._topButton.setVisible(show_y_shift)
        self._bottomButton.setVisible(show_y_shift)
        self._shiftInfo._xLE.setVisible(show_x_shift)
        self._shiftInfo._xLabel.setVisible(show_x_shift)
        self._shiftInfo._yLE.setVisible(show_y_shift)
        self._shiftInfo._yLabel.setVisible(show_y_shift)


class _ImgOpts(qt.QGroupBox):
    sigSubsamplingChanged = qt.Signal()
    """Signal emitted when the subsampling change"""

    def __init__(self, parent, title="Image Option"):
        super().__init__(title, parent)
        self.setLayout(qt.QFormLayout())
        self._subsamplingQSpinBox = qt.QSpinBox(self)
        self.layout().addRow("subsampling:", self._subsamplingQSpinBox)
        self._subsamplingQSpinBox.setMinimum(1)

        # set up
        self._subsamplingQSpinBox.setValue(1)

        # connect signal / slot
        self._subsamplingQSpinBox.valueChanged.connect(self._subsamplingChanged)

    def _subsamplingChanged(self):
        self.sigSubsamplingChanged.emit()

    def getSubsampling(self):
        return self._subsamplingQSpinBox.value()

    def setSubsampling(self, value):
        return self._subsamplingQSpinBox.setValue(int(value))


class _ShiftInformation(qt.QWidget):
    """
    Widget displaying information about the current x and y shift.
    Both x shift and y shift are editable.
    """

    class _ShiftLineEdit(qt.QLineEdit):
        def __init__(self, *args, **kwargs):
            qt.QLineEdit.__init__(self, *args, **kwargs)
            self._defaultBackgroundColor = None
            # validator
            validator = qt.QDoubleValidator(parent=self, decimals=2)
            self.setValidator(validator)
            self._getDefaultBackgroundColor()
            # connect signal / slot
            self.textEdited.connect(self._userEditing)
            self.editingFinished.connect(self._userEndEditing)

        def sizeHint(self):
            return qt.QSize(40, 10)

        def _getDefaultBackgroundColor(self):
            if self._defaultBackgroundColor is None:
                self._defaultBackgroundColor = self.palette().color(
                    self.backgroundRole()
                )
            return self._defaultBackgroundColor

        def _userEditing(self, *args, **kwargs):
            palette = self.palette()
            palette.setColor(self.backgroundRole(), EDITING_BACKGROUND_COLOR)
            self.setPalette(palette)

        def _userEndEditing(self, *args, **kwargs):
            palette = self.palette()
            palette.setColor(
                self.backgroundRole(),
                self._getDefaultBackgroundColor(),
            )
            self.setPalette(palette)

    sigShiftChanged = qt.Signal(float, float)
    """Signal emitted ony when xLE and yLE edition is finished"""

    def __init__(self, parent):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self._xLabel = qt.QLabel("x=", parent=self)
        self.layout().addWidget(self._xLabel)
        self._xLE = _ShiftInformation._ShiftLineEdit("", parent=self)
        self.layout().addWidget(self._xLE)

        self._yLabel = qt.QLabel("y=", parent=self)
        self.layout().addWidget(self._yLabel)
        self._yLE = _ShiftInformation._ShiftLineEdit("", parent=self)
        self.layout().addWidget(self._yLE)

        # connect Signal / Slot
        self._xLE.editingFinished.connect(self._shiftChanged)
        self._yLE.editingFinished.connect(self._shiftChanged)

    def _updateShiftInfo(self, x, y):
        with block_signals(self):
            if x is None:
                x = 0.0
            if y is None:
                y = 0.0
            x_text = x
            if x_text != "...":
                x_text = "%.1f" % float(x)
            y_text = y
            if y_text != "...":
                y_text = "%.1f" % float(y)
            self._xLE.setText(x_text)
            self._yLE.setText(y_text)

    def _shiftChanged(self, *args, **kwargs):
        self.sigShiftChanged.emit(float(self._xLE.text()), float(self._yLE.text()))


class _AxisOptionsWidget(qt.QWidget):
    """GUI to tune the axis algorithm"""

    def __init__(self, parent, axis):
        qt.QWidget.__init__(self, parent=parent)
        assert isinstance(axis, QAxisRP)
        self._axis = axis
        self.setLayout(qt.QVBoxLayout())

        # define common options
        self._commonOpts = qt.QWidget(parent=self)
        self._commonOpts.setLayout(qt.QFormLayout())

        self._qcbDataMode = qt.QComboBox(parent=self)
        for data_mode in AxisCalculationInput:
            # paganin is not managed for sinogram
            self._qcbDataMode.addItem(data_mode.name(), data_mode)
        # for now not handle
        # self._commonOpts.layout().addRow('data mode', self._qcbDataMode)
        self._qcbDataMode.hide()

        # add scale option
        self._scaleOpt = qt.QCheckBox(parent=self)
        self._commonOpts.layout().addRow("scale the two images", self._scaleOpt)
        self.layout().addWidget(self._commonOpts)

        # add option for computing min-max
        # TODO
        pass

        # add near options
        self._nearOpts = _AxisNearOptsWidget(parent=self, axis=self._axis)
        self.layout().addWidget(self._nearOpts)

        # set up
        self.setCalculationInputType(self._axis.calculation_input_type)

        # connect signal / slot
        self._scaleOpt.toggled.connect(self._updateScaleOpt)
        self._qcbDataMode.currentIndexChanged.connect(self._updateInputType)
        self._axis.sigChanged.connect(self._updateMode)

    def setMode(self, mode):
        pass

    def _updateMode(self):
        with block_signals(self):
            index = self._qcbDataMode.findText(self._axis.calculation_input_type.name())
            if index >= 0:
                self._qcbDataMode.setCurrentIndex(index)

    def _updateScaleOpt(self, *arg, **kwargs):
        self._axis.scale_img2_to_img1 = self.isImageScaled()

    def isImageScaled(self):
        return self._scaleOpt.isChecked()

    def _updateInputType(self, *arg, **kwargs):
        self._axis.calculation_input_type = self.getCalulationInputType()

    def getCalulationInputType(self, *arg, **kwargs):
        return AxisCalculationInput.from_value(self._qcbDataMode.currentText())

    def setCalculationInputType(self, calculation_type):
        calculation_type = AxisCalculationInput.from_value(calculation_type)
        index_dm = self._qcbDataMode.findText(calculation_type.name())
        self._qcbDataMode.setCurrentIndex(index_dm)

    def setAxisParams(self, axis):
        self._nearOpts.setAxisParams(axis=axis)
        self._axis = axis
        with block_signals(self):
            self._scaleOpt.setChecked(axis.scale_img2_to_img1)
            index = self._qcbDataMode.findText(axis.calculation_input_type.name())
            self._qcbDataMode.setCurrentIndex(index)


class _AxisNearOptsWidget(qt.QWidget):
    """GUI dedicated to the neat option"""

    def __init__(self, parent, axis):
        qt.QWidget.__init__(self, parent=parent)
        assert isinstance(axis, QAxisRP)
        self._axis = axis

        self.setLayout(qt.QFormLayout())

        self._stdMaxOpt = qt.QCheckBox(parent=self)
        self.layout().addRow("look at max standard deviation", self._stdMaxOpt)

        self._nearWX = qt.QSpinBox(parent=self)
        self._nearWX.setMinimum(1)
        self._nearWX.setValue(5)
        self.layout().addRow("window size", self._nearWX)

        self._fineStepX = qt.QDoubleSpinBox(parent=self)
        self._fineStepX.setMinimum(0.05)
        self._fineStepX.setSingleStep(0.05)
        self._fineStepX.setMaximum(1.0)
        self.layout().addRow("fine step x", self._fineStepX)

        # connect signal / Slot
        self._stdMaxOpt.toggled.connect(self._lookforStxMaxChanged)
        self._nearWX.valueChanged.connect(self._windowSizeChanged)
        self._fineStepX.valueChanged.connect(self._fineStepXChanged)

    def _lookforStxMaxChanged(self, *args, **kwargs):
        self._axis.look_at_stdmax = self.isLookAtStdMax()

    def isLookAtStdMax(self):
        """

        :return: is the option for looking at max standard deviation is
                 activated
        :rtype: bool
        """
        return self._stdMaxOpt.isChecked()

    def _windowSizeChanged(self, *args, **kwargs):
        self._axis.near_wx = self.getWindowSize()

    def getWindowSize(self):
        """

        :return: window size for near search
        :rtype: int
        """
        return self._nearWX.value()

    def _fineStepXChanged(self, *args, **kwargs):
        self._axis.fine_step_x = self.getFineStepX()

    def getFineStepX(self):
        """

        :return: fine step x for near calculation
        :rtype: float
        """
        return self._fineStepX.value()

    def setAxisParams(self, axis):
        """

        :param axis: axis to edit
        :type: AxisRP
        """
        with block_signals(self):
            self._axis = axis
            self._stdMaxOpt.setChecked(axis.look_at_stdmax)
            self._nearWX.setValue(axis.near_wx)
            self._fineStepX.setValue(axis.fine_step_x)


class AxisTabWidget(qt.QTabWidget):
    """
    TabWidget containing all the information to edit the AXIS parameters
    """

    sigLockModeChanged = qt.Signal(bool)
    """signal emitted when the mode lock change"""

    sigUrlChanged = qt.Signal()
    """Signal emit when frames urls changed"""

    def __init__(
        self,
        recons_params,
        parent=None,
        mode_dependant_widget=None,
        read_file_sel_widget=None,
    ):
        """

        :param recons_params: reconstruction parameters edited by the widget
        :type: QAxisRP
        :param mode_dependant_widget: widget used for manual selection of the
                                      axis
        :type mode_dependant_widget: Union[None, `._AxisManualSelection`]
        :param read_file_sel_widget: widget used to select a par file containing
                                     the axis position
        :type read_file_sel_widget: Union[None, `._AxisRead`]
        """
        qt.QTabWidget.__init__(self, parent)
        assert recons_params is not None
        # first tab 'calculation widget'
        self._calculationWidget = _CalculationWidget(
            parent=self, axis_params=recons_params
        )

        # second tab: options
        self._optionsWidget = _AxisOptionsWidget(parent=self, axis=recons_params)
        self._inputWidget = _InputWidget(parent=self, axis_params=recons_params)

        if mode_dependant_widget:
            self._calculationWidget.layout().addWidget(mode_dependant_widget)

        if read_file_sel_widget:
            self._calculationWidget.layout().addWidget(read_file_sel_widget)

        for widget in self._calculationWidget, self._optionsWidget:
            spacer = qt.QWidget(self)
            spacer.setSizePolicy(qt.QSizePolicy.Minimum, qt.QSizePolicy.Expanding)
            widget.layout().addWidget(spacer)

        self._optionsSA = qt.QScrollArea(parent=self)
        self._optionsSA.setWidget(self._optionsWidget)
        self.addTab(self._calculationWidget, "calculation")
        self.addTab(self._optionsSA, "options")
        # simplify set up. Hide options
        self._optionsSA.hide()
        self.addTab(self._inputWidget, "input")

        # set up
        self.setAxisParams(recons_params)
        self._optionsWidget.setMode(self.getMode())
        self._updatePossibleInput()

        # expose API
        self.sigModeChanged = self._calculationWidget.sigModeChanged
        self.isModeLock = self._calculationWidget.isModeLock
        self.setModeLock = self._calculationWidget.setModeLock
        self.setEstimatedCorValue = self._calculationWidget.setEstimatedCorValue
        self.getEstimatedCor = self._calculationWidget.getEstimatedCor

        # connect signal / slot
        self._calculationWidget.sigLockModeChanged.connect(self.sigLockModeChanged)
        self.sigModeChanged.connect(self._updatePossibleInput)
        self._inputWidget._sigUrlChanged.connect(self._urlChanged)
        # not very nice but very convenient to have the setting near at the same level
        self._calculationWidget._qleNearPosQLE.textChanged.connect(
            self._inputWidget._changed
        )

    def getNearPos(self):
        return self._calculationWidget.getNearPosition()

    def setNearPos(self, position):
        return self._calculationWidget.setNearPosition(position=position)

    def updateAutomaticallyEstimatedCor(self):
        return self._calculationWidget.updateAutomaticallyEstimatedCor()

    def setUpdateAutomaticallyEstimatedCor(self, value):
        self._calculationWidget.setUpdateAutomaticallyEstimatedCor(value)

    def _urlChanged(self):
        self.sigUrlChanged.emit()

    def getMode(self):
        """Return algorithm to use for axis calculation"""
        return self._calculationWidget.getMode()

    def setScan(self, scan):
        if scan is not None:
            self._inputWidget.setScan(scan)

    def setAxisParams(self, axis):
        with block_signals(self):
            self._calculationWidget.setAxisParams(axis)
            self._optionsWidget.setAxisParams(axis)
            self._inputWidget.setAxisParams(axis)

    def _updatePossibleInput(self):
        """Update Input tab according to the current mode"""
        current_mode = self.getMode()
        valid_inputs = axis_mode.AXIS_MODE_METADATAS[current_mode].valid_inputs
        if valid_inputs is None:
            self._inputWidget.setEnabled(False)
        else:
            self._inputWidget.setEnabled(True)
            self._inputWidget.setValidInputs(valid_inputs)


class _CalculationWidget(qt.QWidget):
    """Main widget to select the algorithm to use for COR calculation"""

    sigModeChanged = qt.Signal(str)
    """signal emitted when the algorithm for computing COR changed"""

    sigLockModeChanged = qt.Signal(bool)
    """signal emitted when the mode has been lock or unlock"""

    def __init__(self, parent, axis_params):
        assert isinstance(axis_params, QAxisRP)
        qt.QWidget.__init__(self, parent)
        self._axis_params = None
        self.setLayout(qt.QVBoxLayout())

        self._modeWidget = qt.QWidget(parent=self)
        self._modeWidget.setLayout(qt.QHBoxLayout())
        self.layout().addWidget(self._modeWidget)

        self.__rotAxisSelLabel = qt.QLabel("algorithm to compute cor")
        self._modeWidget.layout().addWidget(self.__rotAxisSelLabel)
        self._qcbPosition = qt.QComboBox(self)

        algorithm_groups = (
            # radio group
            (
                axis_mode.AxisMode.centered,
                axis_mode.AxisMode.global_,
                axis_mode.AxisMode.growing_window_radios,
                axis_mode.AxisMode.sliding_window_radios,
                axis_mode.AxisMode.octave_accurate_radios,
            ),
            # sino group
            (
                axis_mode.AxisMode.growing_window_sinogram,
                axis_mode.AxisMode.sino_coarse_to_fine,
                axis_mode.AxisMode.sliding_window_sinogram,
                axis_mode.AxisMode.sino_fourier_angles,
            ),
            # composite corase to fine
            (
                axis_mode.AxisMode.composite_coarse_to_fine,
                axis_mode.AxisMode.near,
            ),
            # manual
            (axis_mode.AxisMode.manual,),
            # read
            (axis_mode.AxisMode.read,),
        )
        current_pos = 0
        for i_grp, algorithm_group in enumerate(algorithm_groups):
            if i_grp != 0:
                self._qcbPosition.insertSeparator(current_pos)
                current_pos += 1
            for cor_algorithm in algorithm_group:
                self._qcbPosition.addItem(cor_algorithm.value)
                idx = self._qcbPosition.findText(cor_algorithm.value)
                self._qcbPosition.setItemData(
                    idx,
                    axis_mode.AXIS_MODE_METADATAS[cor_algorithm].tooltip,
                    qt.Qt.ToolTipRole,
                )
                current_pos += 1

        self._modeWidget.layout().addWidget(self._qcbPosition)

        # method lock button
        self._lockMethodPB = PadlockButton(parent=self._modeWidget)
        self._lockMethodPB.setToolTip(
            "Lock the method to compute the cor. \n"
            "This will automatically call the "
            "defined algorithm each time a scan is received."
        )
        self._modeWidget.layout().addWidget(self._lockMethodPB)

        self._optsWidget = qt.QWidget(self)
        self._optsWidget.setLayout(qt.QVBoxLayout())
        self.layout().addWidget(self._optsWidget)

        # padding option
        self._padding_widget = qt.QGroupBox("padding mode")
        self._padding_widget.setCheckable(True)
        self._optsWidget.layout().addWidget(self._padding_widget)
        self._padding_widget.setLayout(qt.QHBoxLayout())

        self._qbPaddingMode = qt.QComboBox(self._padding_widget)
        for _mode in (
            "constant",
            "edge",
            "linear_ramp",
            "maximum",
            "mean",
            "median",
            "minimum",
            "reflect",
            "symmetric",
            "wrap",
        ):
            self._qbPaddingMode.addItem(_mode)
        def_index = self._qbPaddingMode.findText("edge")
        self._qbPaddingMode.setCurrentIndex(def_index)
        self._padding_widget.layout().addWidget(self._qbPaddingMode)

        # side option
        self._sideWidget = qt.QWidget(self)
        self._sideWidget.setLayout(qt.QHBoxLayout())
        self._optsWidget.layout().addWidget(self._sideWidget)
        self._sideWidget.layout().addWidget(qt.QLabel("side:", self))
        self._sideCB = qt.QComboBox(self._optsWidget)
        self._sideWidget.layout().addWidget(self._sideCB)
        self._sideCB.setToolTip(
            "Define a side for the sliding and growing" "window algorithms"
        )

        # near mode options
        self._nearOptsWidget = qt.QWidget(parent=self)
        self._nearOptsWidget.setLayout(qt.QVBoxLayout())
        self._optsWidget.layout().addWidget(self._nearOptsWidget)

        #    near value lock button
        self._nearValueCB = qt.QCheckBox(
            "Update automatically if `estimated_cor_from_motor` found"
        )
        self._nearValueCB.setToolTip(
            "If the acquisition contains an "
            "estimation of the COR value then "
            "will set it automatically as estimated "
            "value."
        )
        self._nearOptsWidget.layout().addWidget(self._nearValueCB)

        #    LineEdit position value
        self._qleValueW = qt.QWidget(self._nearOptsWidget)
        self._qleValueW.setLayout(qt.QFormLayout())
        self._nearOptsWidget.layout().addWidget(self._qleValueW)

        self._qleNearPosQLE = qt.QLineEdit("0", self._nearOptsWidget)
        validator = qt.QDoubleValidator(self._qleNearPosQLE)
        self._qleNearPosQLE.setValidator(validator)
        self._qleValueW.layout().addRow(
            "estimated value (in relative):", self._qleNearPosQLE
        )

        # cor_options
        self._corOptsWidget = qt.QWidget(self)
        self._corOptsWidget.setLayout(qt.QHBoxLayout())
        self._corOpts = qt.QLineEdit(self)
        self._corOpts.setToolTip(
            "Options for methods finding automatically the rotation axis position. 'side', 'near_pos' and 'near_width' are already provided by dedicated interface. The parameters are separated by commas and passed as 'name=value'. Mind the semicolon separator (;)."
        )
        self._corOpts.setPlaceholderText("low_pass=1; high_pass=20")
        self._corOptsWidget.layout().addWidget(qt.QLabel("cor advanced options"))
        self._corOptsWidget.layout().addWidget(self._corOpts)
        self._optsWidget.layout().addWidget(self._corOptsWidget)

        # connect signal / slot
        self._qcbPosition.currentIndexChanged.connect(self._modeChanged)
        self._qleNearPosQLE.editingFinished.connect(self._nearValueChanged)
        self._sideCB.currentTextChanged.connect(self._sideChanged)
        self._lockMethodPB.sigLockChanged.connect(self.lockMode)
        self._qbPaddingMode.currentIndexChanged.connect(self._paddingModeChanged)
        self._padding_widget.toggled.connect(self._paddingModeChanged)
        self._corOpts.editingFinished.connect(self._corOptsChanged)

        # set up interface
        self._sideWidget.setVisible(False)
        self.setAxisParams(axis_params)
        self._nearValueCB.setChecked(True)
        self._nearOptsWidget.setHidden(True)

    def getMethodLockPB(self) -> qt.QPushButton:
        return self._lockMethodPB

    def setEstimatedCorValue(self, value):
        if value is not None:
            self._qleNearPosQLE.setText(str(value))
            # note: keep self._axis_params up to date.
            if self._axis_params:
                self._axis_params.estimated_cor = value

    def getEstimatedCor(self):
        try:
            return float(self._qleNearPosQLE.text())
        except ValueError:
            return 0

    def updateAutomaticallyEstimatedCor(self):
        return self._nearValueCB.isChecked()

    def setUpdateAutomaticallyEstimatedCor(self, checked):
        self._nearValueCB.setChecked(checked)

    def setSide(self, side):
        if side is not None:
            idx = self._sideCB.findText(side)
            if idx >= 0:
                self._sideCB.setCurrentIndex(idx)

    def getSide(self):
        return self._sideCB.currentText()

    def _modeChanged(self, *args, **kwargs):
        mode = self.getMode()
        with block_signals(self._qcbPosition):
            with block_signals(self._axis_params):
                self._corOptsWidget.setVisible(
                    mode
                    not in (
                        axis_mode.AxisMode.manual,
                        axis_mode.AxisMode.read,
                    )
                )

                self._padding_widget.setVisible(
                    axis_mode.AXIS_MODE_METADATAS[mode].allows_padding
                )
                if axis_mode.AXIS_MODE_METADATAS[mode].is_lockable:
                    self._lockMethodPB.setVisible(True)
                else:
                    self._lockMethodPB.setVisible(False)
                    self.lockMode(False)

                sides_visible = len(axis_mode.AXIS_MODE_METADATAS[mode].valid_sides) > 0
                self._sideWidget.setVisible(sides_visible)
                if sides_visible is True:
                    self._updateSideVisible(mode)
                self._nearOptsWidget.setVisible(self.getSide() == "near")
                self._axis_params.mode = mode.value
            self._axis_params.changed()
            self.sigModeChanged.emit(mode.value)

    def _updateSideVisible(self, mode: axis_mode.AxisMode):
        mode = axis_mode.AxisMode.from_value(mode)
        if len(axis_mode.AXIS_MODE_METADATAS[mode].valid_sides) == 0:
            return
        else:
            current_value = self._axis_params.side
            with block_signals(self._sideCB):
                self._sideCB.clear()
                values = axis_mode.AXIS_MODE_METADATAS[mode].valid_sides
                for value in values:
                    self._sideCB.addItem(value)
                idx = self._sideCB.findText(current_value)
                if idx == -1:
                    # if side doesn't exists, propose right as default when possible
                    idx = self._sideCB.findText("right")
                if idx >= 0:
                    self._sideCB.setCurrentIndex(idx)
            self._axis_params.side = self.getSide()

    def isModeLock(self):
        return self._lockMethodPB.isLocked()

    def setModeLock(self, mode=None):
        """set a specific mode and lock it.

        :param mode: mode to lock. If None then keep the current mode
        """
        if mode is not None:
            mode = axis_mode.AxisMode.from_value(mode)
        if mode is None and axis_mode.AXIS_MODE_METADATAS[self.getMode()].is_lockable():
            raise ValueError(
                "Unable to lock the current mode is not an automatic algorithm"
            )
        elif (
            mode != self.getMode() and axis_mode.AXIS_MODE_METADATAS[mode].is_lockable()
        ):
            raise ValueError("Unable to lock %s this is not a lockable mode")

        if mode is not None:
            self.setMode(mode)
        if not self._lockMethodPB.isLocked():
            with block_signals(self._lockMethodPB):
                self._lockMethodPB.setLock(True)
        self.lockMode(True)

    def lockMode(self, lock):
        with block_signals(self._lockMethodPB):
            self._lockMethodPB.setLock(lock)
            self._qcbPosition.setEnabled(not lock)

        self.sigLockModeChanged.emit(lock)

    def getMode(self):
        """Return algorithm to use for axis calculation"""
        return axis_mode.AxisMode.from_value(self._qcbPosition.currentText())

    def setMode(self, mode):
        with block_signals(self._qcbPosition):
            index = self._qcbPosition.findText(mode.value)
            if index >= 0:
                self._qcbPosition.setCurrentIndex(index)
            else:
                raise ValueError("Unagle to find mode", mode)
            self._lockMethodPB.setVisible(
                mode not in (axis_mode.AxisMode.manual, axis_mode.AxisMode.read)
            )

    def _nearValueChanged(self, *args, **kwargs):
        self._axis_params.estimated_cor = self.getEstimatedCor()

    @deprecated(replacement="getEstimatedCor", since_version="0.6")
    def getNearPosition(self):
        return self.getEstimatedCor()

    @deprecated(replacement="setEstimatedCorValue", since_version="0.6")
    def setNearPosition(self, position):
        self.setEstimatedCorValue(position)

    def _paddingModeChanged(self, *args, **kwargs):
        self._axis_params.padding_mode = self.getPaddingMode()

    def _corOptsChanged(self, *args, **kwargs):
        self._axis_params.extra_cor_options = self.getCorOptions()

    def _sideChanged(self, *args, **kwargs):
        side = self.getSide()
        if side not in ("", None):
            self._axis_params.side = side
        self._nearOptsWidget.setVisible(side == "near")

    def getCorOptions(self):
        return self._corOpts.text()

    def setCorOptions(self, opts: Optional[str]):
        with block_signals(self._axis_params):
            self._corOpts.clear()
            if opts:
                self._corOpts.setText(opts)
                self._corOptsChanged()

    def getPaddingMode(self):
        if self._padding_widget.isChecked():
            return self._qbPaddingMode.currentText()
        else:
            return None

    def setPaddingMode(self, mode):
        index = self._qbPaddingMode.findText(mode)
        if index >= 0:
            self._qbPaddingMode.setCurrentIndex(index)
        self._paddingModeChanged()

    def setAxisParams(self, axis):
        with block_signals(self):
            if self._axis_params is not None:
                self._axis_params.sigChanged.disconnect(self._axis_params_changed)
            self._axis_params = axis
            if self._axis_params.mode in (
                axis_mode.AxisMode.manual,
                axis_mode.AxisMode.read,
            ):
                # those mode cannot be handled by the auto calculation dialog
                self._axis_params.mode = axis_mode.AxisMode.growing_window_radios
            self._axis_params.sigChanged.connect(self._axis_params_changed)
            self._axis_params_changed()
            self._sideChanged()

    def _axis_params_changed(self, *args, **kwargs):
        self.setMode(self._axis_params.mode)
        self.setEstimatedCorValue(self._axis_params.estimated_cor)
        self.setSide(self._axis_params.side)
        sides_visible = (
            len(axis_mode.AXIS_MODE_METADATAS[self._axis_params.mode].valid_sides) > 0
        )
        self._sideWidget.setVisible(sides_visible)
        self._updateSideVisible(mode=self._axis_params.mode)
        self.setPaddingMode(self._axis_params.padding_mode)
        self.setCorOptions(self._axis_params.extra_cor_options)


class _SliceSelector(qt.QWidget):
    sigChanged = qt.Signal()
    """signal emit when the selected slice change"""

    def __init__(self, parent):
        qt.QWidget.__init__(self, parent)
        self.setLayout(qt.QHBoxLayout())
        self.setContentsMargins(0, 0, 0, 0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self._modeCB = qt.QComboBox(self)
        self._modeCB.addItem("middle")
        self._modeCB.addItem("other")
        self.layout().addWidget(self._modeCB)
        self._otherSB = qt.QSpinBox(self)
        self._otherSB.setRange(0, 10000)
        self.layout().addWidget(self._otherSB)

        # connect signal / slot
        self._otherSB.valueChanged.connect(self._valueChanged)
        self._modeCB.currentIndexChanged.connect(self._modeChanged)
        # set up
        self._modeChanged()

    def getSlice(self) -> Union[int, str]:
        "return a specific slice index or 'middle'"
        if self.getMode() == "middle":
            return "middle"
        else:
            return self._otherSB.value()

    def setSlice(self, slice_):
        if slice_ is None:
            return
        if slice_ == "middle":
            idx = self._modeCB.findText("middle")
            self._modeCB.setCurrentIndex(idx)
        else:
            idx = self._modeCB.findText("other")
            self._modeCB.setCurrentIndex(idx)
            self._otherSB.setValue(slice_)
        self.sigChanged.emit()

    def getMode(self):
        return self._modeCB.currentText()

    def _valueChanged(self):
        self.sigChanged.emit()

    def _modeChanged(self, *args, **kwargs):
        self._otherSB.setVisible(self.getMode() == "other")
        self._valueChanged()


class _InputWidget(qt.QWidget):
    """Widget used to define the radio to use for axis calculation from
    radios"""

    sigChanged = qt.Signal()
    """Signal emitted when input changed"""

    _sigUrlChanged = qt.Signal()
    """Signal emit when url to be used changed"""

    def __init__(self, parent=None, axis_params=None):
        assert isinstance(axis_params, QAxisRP)
        self._blockUpdateAxisParams = False
        super().__init__(parent)
        self.setLayout(qt.QVBoxLayout())

        # radio input
        self._radioGB = qt.QGroupBox(self)
        self._radioGB.setTitle("radios")
        self._radioGB.setLayout(qt.QVBoxLayout())
        self._radioGB.setCheckable(True)
        self.layout().addWidget(self._radioGB)
        ## angle mode
        self._angleModeWidget = _AngleSelectionWidget(
            parent=self, axis_params=axis_params
        )
        self._radioGB.layout().addWidget(self._angleModeWidget)
        self._axis_params = axis_params

        # sinogram input
        self._sinogramGB = qt.QGroupBox(self)
        self._sinogramGB.setLayout(qt.QVBoxLayout())
        self._standardSinogramOpts = qt.QGroupBox(self)
        self._sinogramGB.layout().addWidget(self._standardSinogramOpts)
        self._standardSinogramOpts.setLayout(qt.QFormLayout())
        self._standardSinogramOpts.layout().setContentsMargins(0, 0, 0, 0)
        self._standardSinogramOpts.setTitle("standard options")

        self._sinogramGB.setTitle("sinogram")
        self._sinogramGB.setCheckable(True)
        self.layout().addWidget(self._sinogramGB)
        ##  sinogram line
        self._sinogramLineSB = _SliceSelector(self)
        self._standardSinogramOpts.layout().addRow("line", self._sinogramLineSB)
        ##  sinogram subsampling
        self._sinogramSubsampling = qt.QSpinBox(self)
        self._sinogramSubsampling.setRange(1, 1000)
        self._sinogramSubsampling.setValue(10)
        self._standardSinogramOpts.layout().addRow(
            "subsampling", self._sinogramSubsampling
        )

        self._spacer = qt.QWidget(self)
        self._spacer.setSizePolicy(qt.QSizePolicy.Minimum, qt.QSizePolicy.Expanding)
        self.layout().addWidget(self._spacer)

        ## options for the composite mode
        self._compositeOpts = qt.QGroupBox(self)
        self._compositeOpts.setTitle("composite options")
        self._sinogramGB.layout().addWidget(self._compositeOpts)
        self._compositeOpts.setLayout(qt.QFormLayout())
        self._compositeOpts.layout().setContentsMargins(0, 0, 0, 0)
        self._thetaSB = qt.QSpinBox(self)
        self._thetaSB.setRange(0, 360)
        self._thetaSB.setValue(DEFAULT_CMP_THETA)
        self._thetaSB.setToolTip("a radio will be picked each theta degres")
        self._thetaLabel = qt.QLabel("angle interval (in degree)", self)
        self._thetaLabel.setToolTip(
            "algorithm will take one projection each 'angle interval'. Also know as 'theta'"
        )
        self._compositeOpts.layout().addRow(self._thetaLabel, self._thetaSB)

        self._oversamplingSB = qt.QSpinBox(self)
        self._oversamplingSB.setValue(DEFAULT_CMP_OVERSAMPLING)
        self._oversamplingSB.setToolTip("sinogram oversampling")
        self._compositeOpts.layout().addRow("oversampling", self._oversamplingSB)

        self._nearwidthSB = qt.QSpinBox(self)
        self._nearwidthSB.setRange(-40000, 40000)
        self._nearwidthSB.setValue(0)
        self._nearwidthSB.setToolTip("position to be used with near option")
        self._nearwidthLabel = qt.QLabel("near width", self)
        self._nearwidthLabel.setToolTip("position to be used with near option")
        self._compositeOpts.layout().addRow(self._nearwidthLabel, self._nearwidthSB)

        self._subsamplingYSB = qt.QSpinBox(self)
        self._subsamplingYSB.setValue(DEFAULT_CMP_N_SUBSAMPLING_Y)
        self._subsamplingYSB.setToolTip("sinogram number of subsampling along y")
        self._compositeOpts.layout().addRow("n_subsampling_y", self._subsamplingYSB)

        self._takeLogCB = qt.QCheckBox(self)
        self._takeLogCB.setToolTip("Take logarithm")
        self._takeLogCB.setChecked(DEFAULT_CMP_TAKE_LOG)
        self._takeTheLogLabel = qt.QLabel("linearisation (-log(I/I0))")
        self._takeTheLogLabel.setToolTip(
            "take (-log(I/I0)) as input. Also know as 'take_log' option"
        )
        self._compositeOpts.layout().addRow(self._takeTheLogLabel, self._takeLogCB)

        # set up
        self._sinogramGB.setChecked(False)

        # connect signal / slot
        self._sinogramGB.toggled.connect(self._sinogramChecked)
        self._radioGB.toggled.connect(self._radiosChecked)
        self._sinogramSubsampling.valueChanged.connect(self._changed)
        self._sinogramLineSB.sigChanged.connect(self._changed)
        self._thetaSB.valueChanged.connect(self._changed)
        self._oversamplingSB.valueChanged.connect(self._changed)
        self._subsamplingYSB.valueChanged.connect(self._changed)
        self._nearwidthSB.valueChanged.connect(self._changed)
        self._takeLogCB.toggled.connect(self._changed)
        self._angleModeWidget.sigChanged.connect(self._sigUrlChanged)

    def setScan(self, scan: TomwerScanBase):
        if scan is not None:
            self._angleModeWidget.setScan(scan)
            self._angleModeWidget.setScanRange(scan.scan_range)

    def setAxisParams(self, axis_params):
        with block_signals(axis_params):
            with block_signals(self._axis_params):
                self._blockUpdateAxisParams = True

                if axis_params is not None:
                    assert isinstance(axis_params, QAxisRP)
                    with block_signals(self._sinogramGB):
                        self._sinogramChecked(axis_params.use_sinogram, on_load=True)
                    self._sinogramLineSB.setSlice(axis_params.sinogram_line)
                    self._sinogramSubsampling.setValue(axis_params.sinogram_subsampling)
                    self.setCompositeOptions(axis_params.composite_options)
                self._angleModeWidget.setAxisParams(axis_params)
                self._axis_params = axis_params

        self._blockUpdateAxisParams = False

    def getSinogramLine(self) -> Union[str, int]:
        return self._sinogramLineSB.getSlice()

    def getSinogramSubsampling(self) -> int:
        return self._sinogramSubsampling.value()

    def _sinogramChecked(self, checked, on_load=False):
        with block_signals(self._radioGB):
            with block_signals(self._sinogramGB):
                if checked:
                    self._radioGB.setChecked(False)
                    self._sinogramGB.setChecked(True)
                elif self._radioGB.isEnabled():
                    self._radioGB.setChecked(not checked)
                elif on_load:
                    self._sinogramGB.setChecked(checked)
                else:
                    # ignore it if radio disabled
                    self._sinogramGB.setChecked(True)
        self._changed()

    def _radiosChecked(self, checked, on_load=False):
        with block_signals(self._radioGB):
            with block_signals(self._sinogramGB):
                if checked:
                    self._sinogramGB.setChecked(False)
                    self._radioGB.setChecked(True)
                elif self._sinogramGB.isEnabled():
                    self._sinogramGB.setChecked(not checked)
                elif on_load:
                    self._radioGB.setChecked(checked)
                else:
                    # ignore it if sinogram disabled
                    self._radioGB.setChecked(True)
        self._changed()

    def _changed(self, *args, **kwargs):
        self._updateAxisParams()
        self.sigChanged.emit()

    def _updateAxisParams(self):
        if not self._blockUpdateAxisParams:
            self._axis_params.use_sinogram = self._sinogramGB.isChecked()
            self._axis_params.sinogram_line = self.getSinogramLine()
            self._axis_params.sinogram_subsampling = self.getSinogramSubsampling()
            self._axis_params.composite_options = self.getCompositeOptions()

    def setValidInputs(self, modes: Union[list, tuple]):
        """
        Define possible inputs.

        :param Union[list,tuple] modes:
        :raises: ValueError if modes are invalid
        """
        modes = set(modes)
        for mode in modes:
            try:
                axis_mode._InputType.from_value(mode)
            except Exception:
                raise ValueError(
                    f"mode {mode} should be an instance of {axis_mode._InputType}"
                )
        if len(modes) == 2:
            self._sinogramGB.setEnabled(True)
            self._radioGB.setEnabled(True)
        elif len(modes) > 2:
            raise ValueError(f"invalid input {modes}")
        elif len(modes) < 0:
            raise ValueError("modes is empty")
        else:
            mode = axis_mode._InputType.from_value(modes.pop())
            if mode in (axis_mode._InputType.SINOGRAM, axis_mode._InputType.COMPOSITE):
                self._sinogramGB.setEnabled(True)
                self._radioGB.setEnabled(False)
                self._sinogramGB.setChecked(True)
                self._compositeOpts.setEnabled(mode is axis_mode._InputType.COMPOSITE)
                self._standardSinogramOpts.setEnabled(
                    mode is not axis_mode._InputType.COMPOSITE
                )
            elif mode is axis_mode._InputType.RADIOS_X2:
                self._radioGB.setEnabled(True)
                self._sinogramGB.setEnabled(False)
                self._radioGB.setChecked(True)
            else:
                raise ValueError(f"Nothing implemented for {mode.value}")

    def getCompositeOptions(self) -> dict:
        return {
            "theta": self.getTheta(),
            "oversampling": self.getOversampling(),
            "n_subsampling_y": self.getSubsamplingY(),
            "take_log": self.getTakeLog(),
            "near_pos": self.getNearpos(),
            "near_width": self.getNearwidth(),
        }

    def setCompositeOptions(self, opts: dict) -> None:
        if not isinstance(opts, dict):
            raise TypeError("opts should be an instance of dict")
        for key in opts.keys():
            if key not in (
                "theta",
                "oversampling",
                "n_subsampling_y",
                "take_log",
                "near_pos",
                "near_width",
            ):
                raise KeyError(f"{key} is not recogized")
            theta = opts.get("theta", None)
            if theta is not None:
                self.setTheta(theta=theta)
            oversampling = opts.get("oversampling", None)
            if oversampling is not None:
                self.setOversampling(oversampling)
            n_subsampling_y = opts.get("n_subsampling_y", None)
            if n_subsampling_y is not None:
                self.setSubsamplingY(n_subsampling_y)

            near_width = opts.get("near_width", None)
            if near_width is not None:
                self.setNearwidth(near_width)

            take_log = opts.get("take_log", None)
            if take_log is not None:
                self.setTakeLog(take_log)

    def getTheta(self) -> int:
        return self._thetaSB.value()

    def setTheta(self, theta: int) -> None:
        self._thetaSB.setValue(theta)

    def getOversampling(self) -> int:
        return self._oversamplingSB.value()

    def setOversampling(self, oversampling: int) -> None:
        self._oversamplingSB.setValue(oversampling)

    def getNearpos(self) -> int:
        cal_widget = self.parentWidget().widget(0)
        assert isinstance(cal_widget, _CalculationWidget)
        return cal_widget.getEstimatedCor()

    def setNearpos(self, value) -> int:
        cal_widget = self.parentWidget().widget(0)
        assert isinstance(cal_widget, _CalculationWidget)
        cal_widget.setNearPosition(value)

    def getNearwidth(self) -> int:
        return self._nearwidthSB.value()

    def setNearwidth(self, value) -> int:
        return self._nearwidthSB.setValue(value)

    def getSubsamplingY(self) -> int:
        return self._subsamplingYSB.value()

    def setSubsamplingY(self, subsampling: int) -> None:
        self._subsamplingYSB.setValue(subsampling)

    def getTakeLog(self) -> bool:
        return self._takeLogCB.isChecked()

    def setTakeLog(self, log: bool) -> None:
        self._takeLogCB.setChecked(log)


class _AngleSelectionWidget(qt.QWidget):
    """Group box to select the angle to used for cor calculation
    (0-180, 90-270 or manual)"""

    sigChanged = qt.Signal()
    """signal emitted when the selected angle changed"""

    def __init__(self, parent=None, axis_params=None):
        assert isinstance(axis_params, QAxisRP)
        qt.QWidget.__init__(
            self,
            parent=parent,
        )
        self.setLayout(qt.QVBoxLayout())
        self._groupBoxMode = qt.QGroupBox(
            self, title="Angles to use for axis calculation"
        )
        self._groupBoxMode.setLayout(qt.QHBoxLayout())
        self.layout().addWidget(self._groupBoxMode)

        self._corButtonsGps = qt.QButtonGroup(parent=self)
        self._corButtonsGps.setExclusive(True)
        self._qrbCOR_0_180 = qt.QRadioButton("0-180", parent=self)
        self._groupBoxMode.layout().addWidget(self._qrbCOR_0_180)
        self._qrbCOR_90_270 = qt.QRadioButton("90-270", parent=self)
        self._qrbCOR_90_270.setToolTip(
            "pick radio closest to angles 90° and "
            "270°. If disable mean that the scan "
            "range is 180°"
        )
        self._groupBoxMode.layout().addWidget(self._qrbCOR_90_270)
        self._qrbCOR_manual = qt.QRadioButton("other", parent=self)
        self._qrbCOR_manual.setVisible(True)
        self._groupBoxMode.layout().addWidget(self._qrbCOR_manual)
        # add all button to the button group
        for b in (self._qrbCOR_0_180, self._qrbCOR_90_270, self._qrbCOR_manual):
            self._corButtonsGps.addButton(b)

        self.setAxisParams(axis_params)

        self._manualFrameSelection = _ManualFramesSelection(self)
        self.layout().addWidget(self._manualFrameSelection)
        self._manualFrameSelection.setVisible(False)

        # connect signal / Slot
        self._corButtonsGps.buttonClicked.connect(self._angleModeChanged)
        self._manualFrameSelection.sigChanged.connect(self._changed)

    def setScan(self, scan: TomwerScanBase):
        if scan is not None:
            self.setScanRange(scan.scan_range)
        self._manualFrameSelection.setScan(scan=scan)

    def setScanRange(self, scanRange):
        if scanRange == 180:
            self._qrbCOR_90_270.setEnabled(False)
            # force using 0-180 if was using 90-270
            if self._qrbCOR_90_270.isChecked():
                self._qrbCOR_0_180.setChecked(True)
                self._axis_params.angle_mode = CorAngleMode.use_0_180
        else:
            self._qrbCOR_90_270.setEnabled(True)

    def setAngleMode(self, mode):
        """

        :param mode: mode to use (can be manual , 90-270 or 0-180)
        """
        assert isinstance(mode, CorAngleMode)
        if mode == CorAngleMode.use_0_180:
            self._qrbCOR_0_180.setChecked(True)
        elif mode == CorAngleMode.use_90_270:
            self._qrbCOR_90_270.setChecked(True)
        else:
            self._qrbCOR_manual.setChecked(True)

    def getAngleMode(self):
        """

        :return: the angle to use for the axis calculation
        :rtype: CorAngleMode
        """
        if self._qrbCOR_90_270.isChecked():
            return CorAngleMode.use_90_270
        elif self._qrbCOR_0_180.isChecked():
            return CorAngleMode.use_0_180
        else:
            return CorAngleMode.manual_selection

    def setAxisParams(self, axis_params):
        with block_signals(self):
            self._axis_params = axis_params
            # set up
            self.setAngleMode(axis_params.angle_mode)

    def _angleModeChanged(self, *args, **kwargs):
        self._axis_params.angle_mode = self.getAngleMode()
        if self.getAngleMode() is CorAngleMode.manual_selection:
            self._axis_params.angle_mode_extra = (
                self._manualFrameSelection.getFramesUrl()
            )
        else:
            self._axis_params.angle_mode_extra = None
        self._manualFrameSelection.setVisible(
            self.getAngleMode() is CorAngleMode.manual_selection
        )
        self._changed()

    def _changed(self):
        self.sigChanged.emit()


class _ManualFramesSelection(qt.QWidget):
    """Allows to select frame - angle to be used."""

    sigChanged = qt.Signal()
    """Signal emit when the frame selection changes"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._anglesAvailable = []
        # cache of the angles availables from the current defined frames. Must be sorted !!!
        self.setLayout(qt.QGridLayout())
        self.layout().addWidget(qt.QLabel("frame 1", self), 0, 0, 1, 1)
        self._frame1CB = qt.QComboBox(self)
        self._frame1CB.setEditable(True)
        self.layout().addWidget(self._frame1CB, 0, 1, 1, 1)

        self.layout().addWidget(qt.QLabel("frame 2", self), 1, 0, 1, 1)
        self._frame2CB = qt.QComboBox(self)
        self._frame2CB.setEditable(True)
        self.layout().addWidget(self._frame2CB, 1, 1, 1, 1)
        self._findAssociatedAnglePB = qt.QPushButton("+180°", self)
        button_180_font = self.font()
        button_180_font.setPixelSize(10)
        self._findAssociatedAnglePB.setFont(button_180_font)
        self._findAssociatedAnglePB.setFixedWidth(30)
        self._findAssociatedAnglePB.setSizePolicy(
            qt.QSizePolicy.Minimum, qt.QSizePolicy.Minimum
        )
        self.layout().addWidget(self._findAssociatedAnglePB, 1, 2, 1, 1)
        self._flipLRCB = qt.QCheckBox("flip L-R")
        self._flipLRCB.setChecked(True)
        self.layout().addWidget(self._flipLRCB, 1, 3, 1, 1)

        self._flipLRCB.toggled.connect(self._changed)
        self._frame1CB.currentIndexChanged.connect(self._changed)
        self._frame2CB.currentIndexChanged.connect(self._changed)
        self._findAssociatedAnglePB.released.connect(self._findAssociatedAngle)

    def _findAssociatedAngle(self):
        if self._frame1CB.count() == 0 or len(self._anglesAvailable) == 0:
            _logger.warning("no angles available, unable to get '+180°' frame")
        else:
            angle = float(self._frame1CB.currentText())
            # look for the closest 'associated' angle.
            # as the angles are not limited to [0-360] we need to check for any value.
            # if the angle is on the first part of the acquisition we expect to find it near angle +180
            # if it is on the second part (for 360 degree) we expect to find it on the first part (0-180)
            closest_pls_180_angle = self._getClosestAssociatedAngle(
                angle + 180.0, self._anglesAvailable
            )
            score_add = abs(closest_pls_180_angle - angle)
            closest_minus_180_angle = self._getClosestAssociatedAngle(
                angle - 180.0, self._anglesAvailable
            )
            score_sub = abs(closest_minus_180_angle - angle)
            if score_add >= score_sub:
                closest_180_angle = closest_pls_180_angle
            else:
                closest_180_angle = closest_minus_180_angle
            item_idx = self._frame2CB.findText(self._angleToStr(closest_180_angle))
            if item_idx < 0:
                _logger.error(f"Unable to find item for angle {closest_180_angle}")
            else:
                self._frame2CB.setCurrentIndex(item_idx)

    @staticmethod
    def _getClosestAssociatedAngle(angle: float, angles: tuple) -> float:
        """
        return the angle closest angle to 'angle' from 'angles'

        :warning: angles should be already sorted !!!
        """
        if angles is None or len(angles) == 0:
            return None
        if angle in angles:
            return angle
        pos = bisect_left(angles, angle)
        if pos == 0:
            return angles[0]
        elif pos > len(angles) - 1:
            return angles[-1]
        else:
            left_angle = angles[pos - 1]
            right_angle = angles[pos]
            if abs(right_angle - angle) > abs(left_angle - angle):
                return left_angle
            else:
                return right_angle

    def _changed(self):
        self.sigChanged.emit()

    @staticmethod
    def _angleToStr(angle: float) -> str:
        return f"{float(angle):0.3f}"

    def setScan(self, scan: Union[TomwerScanBase, None]) -> None:
        self._anglesAvailable.clear()
        self._frame1CB.clear()
        self._frame2CB.clear()
        if scan is None:
            return
        current_angle1 = self._getFrame1Angle()
        current_angle2 = self._getFrame2Angle()
        for proj_angle, proj_url in scan.get_proj_angle_url().items():
            try:
                angle = self._angleToStr(proj_angle)
            except Exception:
                angle = proj_angle
            else:
                self._anglesAvailable.append(float(proj_angle))
            self._frame1CB.addItem(angle, proj_url)
            self._frame2CB.addItem(angle, proj_url)

        self._anglesAvailable.sort()

        idx = self._frame1CB.findText(current_angle1)
        if idx >= 0:
            self._frame1CB.setCurrentIndex(idx)
        if current_angle1 == current_angle2:
            # if the two current angle are close then we consider it is better to look for angleX - angleX + 180 angles
            # instead of finding back angles
            self._findAssociatedAngle()
        else:
            idx = self._frame1CB.findText(current_angle1)
            if idx >= 0:
                self._frame1CB.setCurrentIndex(idx)

            idx = self._frame2CB.findText(current_angle2)
            if idx >= 0:
                self._frame2CB.setCurrentIndex(idx)

    def getFramesUrl(self, as_txt=False) -> tuple:
        """
        Return a tuple of (frame 1 url, frame 2 url). Url can be None
        """
        if as_txt:
            return self.getFrame1Url().path(), self.getFrame2Url().path()
        else:
            return self.getFrame1Url(), self.getFrame2Url()

    def getFrame1Url(self) -> Optional[DataUrl]:
        return self._frame1CB.currentData()

    def getFrame2Url(self) -> Optional[DataUrl]:
        return self._frame2CB.currentData()

    def _getFrame1Angle(self) -> Optional[str]:
        return self._frame1CB.currentText()

    def _getFrame2Angle(self) -> Optional[str]:
        return self._frame2CB.currentText()

    def isFrame2LRFLip(self):
        return self._flipLRCB.isChecked()
