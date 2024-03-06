#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from PySide6 import QtWidgets, QtCore

from SpatialView.source.vtk_cylinder_source import VtkCylinderSource
from SpatialView.vtk_algo_data import VtkAlgoData


class VtkCylinderSourceModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = VtkCylinderSource(self)
        self._source.center = (0, 0, 0)
        self._source.radius = 0.5

        self._label = QtWidgets.QLabel("Settings")
        self._label.installEventFilter(self)
        self._label.setStyleSheet(
            "QLabel { background-color : transparent; color : white; }"
        )

    @override
    def eventFilter(self, object, event):
        if object == self._label:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                # if not self._setting:
                setting = self._source.dialog()
                setting.exec()
                return True
        return False

    @override
    def caption(self):
        return "Vtk Cylinder Source"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkCylinderSource"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        registry.registerModel(
            VtkCylinderSourceModel, VtkCylinderSourceModel.name(), "Sources"
        )

    @override
    def nPorts(self, portType):
        result = 1
        match portType:
            case sNode.PortType.In:
                result = 0
            case sNode.PortType.Out:
                result = 1
        return result

    @override
    def dataType(self, portType, portIndex):
        return VtkAlgoData().type()

    @override
    def outData(self, port):
        return VtkAlgoData(self._source.outputPort())

    @override
    def setInData(self, nodeData, portIndex): ...

    @override
    def embeddedWidget(self):
        return self._label

    @override
    def save(self):
        modelJson = super().save()
        modelJson["source"] = self._source.save()

        return modelJson

    @override
    def load(self, p):
        self._source.load(p)
