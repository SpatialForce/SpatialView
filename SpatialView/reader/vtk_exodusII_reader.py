#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets, QtCore
from SpatialNode import QJsonObject
from vtkmodules.vtkIOExodus import vtkExodusIIReader


class VtkExodusIIReader:
    def __init__(self, model):
        self._reader = vtkExodusIIReader()
        self._model = model

    @property
    def fileName(self):
        return self._reader.GetFileName()

    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self._reader.UpdateInformation()
        self._reader.SetTimeStep(10)
        self._reader.SetAllArrayStatus(
            vtkExodusIIReader.NODAL, 1
        )  # enables all NODAL variables
        self._reader.Update()
        self._model.dataUpdated.emit(0)

    def outputPort(self):
        return self._reader.GetOutputPort()

    def load(self, p):
        source = p["source"]
        self.fileName = source["fileName"]

    def save(self):
        source = QJsonObject()
        source["fileName"] = self.fileName
        return source

    def dialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Open Flow Scene",
            QtCore.QDir.homePath(),
            "Flow Scene Files (*.e *.exo)",
        )

        if not QtCore.QFileInfo.exists(fileName):
            return

        self.fileName = fileName
