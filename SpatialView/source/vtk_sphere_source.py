#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Property
from vtkmodules.vtkFiltersSources import vtkSphereSource
from functools import partial


class VtkSphereSource:
    def __init__(self, model):
        self._source = vtkSphereSource()
        self._model = model

    @Property(float)
    def radius(self):
        return self._source.GetRadius()

    @radius.setter
    def radius(self, value):
        self._source.SetRadius(value)
        self._model.dataUpdated.emit(0)

    @property
    def endPhi(self):
        return self._source.GetEndPhi()

    @endPhi.setter
    def endPhi(self, value):
        self._source.SetEndPhi(value)
        self._model.dataUpdated.emit(0)

    @property
    def endTheta(self):
        return self._source.GetEndTheta()

    @endTheta.setter
    def endTheta(self, value):
        self._source.SetEndTheta(value)
        self._model.dataUpdated.emit(0)

    @property
    def startPhi(self):
        return self._source.GetStartPhi()

    @startPhi.setter
    def startPhi(self, value):
        self._source.SetStartPhi(value)
        self._model.dataUpdated.emit(0)

    @property
    def startTheta(self):
        return self._source.GetStartTheta()

    @startTheta.setter
    def startTheta(self, value):
        self._source.SetStartTheta(value)
        self._model.dataUpdated.emit(0)

    @property
    def phiResolution(self):
        return self._source.GetPhiResolution()

    @phiResolution.setter
    def phiResolution(self, value):
        self._source.SetPhiResolution(value)
        self._model.dataUpdated.emit(0)

    @property
    def thetaResolution(self):
        return self._source.GetThetaResolution()

    @thetaResolution.setter
    def thetaResolution(self, value):
        self._source.SetThetaResolution(value)
        self._model.dataUpdated.emit(0)

    @property
    def center(self):
        return self._source.GetCenter()

    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self._model.dataUpdated.emit(0)

    def widget(self):
        settings = QtWidgets.QWidget()
        settings.setWindowTitle("VtkSphereSource Settings")

        layout = QtWidgets.QVBoxLayout(settings)
        slider = QtWidgets.QDoubleSpinBox()
        slider.setSingleStep(0.1)
        slider.valueChanged.connect(partial(VtkSphereSource.radius.fset, self))
        layout.addWidget(slider)

        return settings

    def outputPort(self):
        return self._source.GetOutputPort()
