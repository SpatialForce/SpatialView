#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.
import os

from PySide6 import QtWidgets, QtCore
from SpatialNode import QJsonObject
from vtkmodules.vtkIOImage import vtkHDRReader


class VtkHDRReader:
    def __init__(self, model):
        self._reader = vtkHDRReader()
        self._model = model

        # default file
        self.fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(
            "SpatialView/resources/meadow_2_1k.hdr"
        )

    @property
    def extensions(self):
        return self._reader.GetFileExtensions()

    @property
    def fileName(self):
        return self._reader.GetFileName()

    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self._model.dataUpdated.emit(0)

    def outputPort(self):
        return self._reader.GetOutputPort()

    def load(self, p):
        source = p["source"]
        relative = source["fileName"]
        self.fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(relative)

    def save(self):
        source = QJsonObject()

        relative = QtCore.QDir(os.getcwd()).relativeFilePath(self.fileName)
        source["fileName"] = relative
        return source

    def dialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Open Flow Scene",
            QtCore.QDir.homePath(),
            "Flow Scene Files (*.hdr *.pic)",
        )

        if not QtCore.QFileInfo.exists(fileName):
            return

        self.fileName = fileName
