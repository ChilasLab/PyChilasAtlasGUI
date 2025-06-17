"""
Script to create a standalone binary executable for the Chilas ATLAS application.
"""

import PyInstaller.__main__
from PyInstaller.utils.hooks import copy_metadata, collect_submodules
from PyInstaller.utils.hooks import collect_data_files
from PySide2.QtWidgets import QApplication,QFileDialog
import os
import shutil
import sys

no_pop = False
if len(sys.argv) > 1: 
    no_pop = True

app = QApplication()

if no_pop:
    name: str = sys.argv[1] + ".exe"
    path: str = os.path.dirname(sys.argv[0])
else:
    path,type  = QFileDialog.getSaveFileName(caption="Where save binary?", filter="Executable (*.exe)",selectedFilter="Executable (*.exe)")
    name = os.path.basename(path)
    path = os.path.dirname(path)


PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '-iicon.ico',
    f"-n{name}",
    '--add-data',
      "*.qml;.",
    '--add-data',
      "*.png;."
])

source: str = os.path.join("dist", f"{name}")
destination: str = os.path.join(path, f"{name}")

try:
    shutil.move(src=source, dst=destination)
except Exception as e:
    print(f"Error moving file: {e}")

