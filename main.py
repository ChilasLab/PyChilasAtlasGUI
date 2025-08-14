#****************************************************************************
#This file is part of Chilas ATLAS.
#
#Chilas ATLAS is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Chilas ATLAS is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <https://www.gnu.org/licenses/>.
#****************************************************************************

import sys
import os

from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl

import pyLaser

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setApplicationName("Chilas Atlas")
    app.setApplicationVersion("2025-v1.17")
    app.setOrganizationName("Chilas Lasers B.V.")
    app.setOrganizationDomain("chilasbv.com")
    app.setWindowIcon(QIcon("star.ico"))

    engine = QQmlApplicationEngine()

    laser = pyLaser.pyLaser()
    engine.rootContext().setContextProperty("backend", laser)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
