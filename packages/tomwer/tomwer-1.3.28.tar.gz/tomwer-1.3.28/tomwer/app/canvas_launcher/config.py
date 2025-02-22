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
__date__ = "14/12/2021"


import pkg_resources
from orangecanvas.application.outputview import (
    TerminalTextDocument as _TerminalTextDocument,
)
from orangewidget.settings import set_widget_settings_dir_components
from orangewidget.workflow import config
from silx.gui import qt

import tomwer.version
from tomwer.gui import icons

from . import environ
from .splash import getIcon, splash_screen
from .widgetsscheme import WidgetsScheme


def version():
    return tomwer.version.version


class TomwerConfig(config.Config):
    """
    Configuration defined for tomwer
    """

    OrganizationDomain = "esrf"
    ApplicationName = "tomwer"
    ApplicationVersion = version()

    def init(self):
        super().init()
        qt.QApplication.setApplicationName(self.ApplicationName)
        qt.QApplication.setOrganizationDomain(self.OrganizationDomain)
        qt.QApplication.setApplicationVersion(self.ApplicationVersion)
        qt.QApplication.setApplicationDisplayName(self.ApplicationName)
        widget_settings_dir_cfg = environ.get_path("widget_settings_dir", "")
        if widget_settings_dir_cfg:
            # widget_settings_dir is configured via config file
            set_widget_settings_dir_components(
                widget_settings_dir_cfg, self.ApplicationVersion
            )

        canvas_settings_dir_cfg = environ.get_path("canvas_settings_dir", "")
        if canvas_settings_dir_cfg:
            # canvas_settings_dir is configured via config file
            qt.QSettings.setPath(
                qt.QSettings.IniFormat, qt.QSettings.UserScope, canvas_settings_dir_cfg
            )

    @staticmethod
    def splash_screen():
        return splash_screen()

    @staticmethod
    def core_packages():
        return super().core_packages() + ["tomwer-add-on"]

    @staticmethod
    def application_icon():
        return getIcon()

    @staticmethod
    def workflow_constructor(*args, **kwargs):
        return WidgetsScheme(*args, **kwargs)

    @staticmethod
    def widgets_entry_points():
        """
        Return an `EntryPoint` iterator for all 'orange.widget' entry
        points.
        """
        # Ensure the 'this' distribution's ep is the first. iter_entry_points
        # yields them in unspecified order.
        WIDGETS_ENTRY = "orange.widgets"

        def is_tomwer_extension(entry):
            return "tomwer" in entry.name.lower()

        all_eps = filter(
            is_tomwer_extension, pkg_resources.iter_entry_points(WIDGETS_ENTRY)
        )

        all_eps = sorted(
            all_eps,
            key=lambda ep: (
                0 if ep.dist.project_name.lower() in ("orange3", "tomwer") else 1
            ),
        )
        return iter(all_eps)

    @staticmethod
    def addon_entry_points():
        return TomwerConfig.widgets_entry_points()

    APPLICATION_URLS = {
        #: Submit a bug report action in the Help menu
        "Bug Report": "https://gitlab.esrf.fr/tomotools/tomwer/-/issues",
        #: A url quick tour/getting started url
        "Quick Start": "https://www.youtube.com/playlist?list=PLddRXwP6Z6F9KOu1V5o6H24KPH5Ikuk2f",
        #: The 'full' documentation, should be something like current /docs/
        #: but specific for 'Visual Programing' only
        "Documentation": "https://tomotools.gitlab-pages.esrf.fr/tomwer/index.html",
        #: YouTube tutorials
        "Screencasts": "https://www.youtube.com/@tomotools",
    }


class TomwerSplashScreen(qt.QSplashScreen):
    def __init__(
        self,
        parent=None,
        pixmap=None,
        textRect=None,
        textFormat=qt.Qt.PlainText,
        **kwargs,
    ):
        super(TomwerSplashScreen, self).__init__(pixmap=icons.getQPixmap("tomwer"))

    def showMessage(self, message, alignment=qt.Qt.AlignLeft, color=qt.Qt.black):
        version = f"tomwer version {tomwer.version.version}"
        super().showMessage(version, qt.Qt.AlignLeft | qt.Qt.AlignBottom, qt.Qt.white)


class TerminalTextDocument(_TerminalTextDocument):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, **kwargs)

    @staticmethod
    def get_log_level(my_str):
        if "DEBUG" in my_str:
            return qt.Qt.darkBlue
        elif "ERROR" in my_str:
            return qt.Qt.red
        elif "WARNING" in my_str:
            return qt.Qt.magenta
        elif "CRITICAL" in my_str:
            return qt.Qt.red
        elif "Info" in my_str:
            return qt.Qt.black
        elif "CRITICAL" in my_str:
            return qt.Qt.darkYellow
        elif "PROCESS_STARTED" in my_str:
            return qt.Qt.black
        elif "PROCESS_SUCCEED" in my_str:
            return qt.Qt.darkGreen
        elif "PROCESS_FAILED" in my_str:
            return qt.Qt.red
        elif "PROCESS_ENDED" in my_str:
            return qt.Qt.black
        elif "PROCESS_SKIPPED" in my_str:
            return qt.Qt.magenta
        else:
            return None

    def writeWithFormat(self, string: str, charformat) -> None:
        assert qt.QThread.currentThread() is self.thread()
        # remove linux reset sequence
        from tomwer.core.log import logger as tomwer_logger

        for sequence in (
            tomwer_logger._RESET_SEQ,
            tomwer_logger._BOLD_SEQ,
            tomwer_logger._BLACK,
            tomwer_logger._RED,
            tomwer_logger._GREEN,
            tomwer_logger._YELLOW,
            tomwer_logger._BLUE,
            tomwer_logger._MAGENTA,
        ):
            string = string.replace(sequence, "")

        color = self.get_log_level(string) or qt.Qt.red
        charformat.setForeground(color)

        # super().writelinesWithFormat(string, charformat)
        cursor = self.textCursor()
        cursor.setCharFormat(charformat)
        cursor.insertText(string)
