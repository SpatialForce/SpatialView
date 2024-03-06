#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from PySide6 import QtWidgets, QtCore
from vtkmodules.vtkFiltersSources import vtkSphereSource

from SpatialView.vtk_algo_data import VtkAlgoData


class VtkSphereSourceModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkSphereSource()
        self._source.SetCenter(0, 0, 0)
        self._source.SetRadius(0.5)

        self._label = QtWidgets.QLabel("Settings")
        self._label.installEventFilter(self)
        self._label.setStyleSheet("QLabel { background-color : transparent; color : white; }")

        self._setting = self.create_settings()

    def create_settings(self):
        settings = QtWidgets.QWidget()
        settings.setWindowTitle("VtkSphereSource Settings")

        layout = QtWidgets.QVBoxLayout(settings)
        slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        slider.setMaximum(10)
        slider.setMinimum(1)
        slider.valueChanged.connect(self.setRadius)
        layout.addWidget(slider)

        return settings

    def setRadius(self, radius: int):
        self._source.SetRadius(radius / 5)
        self.dataUpdated.emit(0)

    @override
    def eventFilter(self, object, event):
        if object == self._label:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                self._setting.raise_()
                self._setting.show()
                return True
        return False

    @override
    def caption(self):
        return "Vtk Sphere Source"

    @override
    def captionVisible(self):
        return True

    @override
    def name(self):
        return "VtkSphereSource"

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
        return VtkAlgoData(self._source.GetOutputPort())

    @override
    def setInData(self, nodeData, portIndex):
        ...

    @override
    def embeddedWidget(self):
        return self._label
