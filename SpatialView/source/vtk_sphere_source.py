#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets, QtCore
from vtkmodules.vtkFiltersSources import vtkSphereSource


class VtkSphereSource:
    def __init__(self, model):
        self._source = vtkSphereSource()
        self._model = model

    @property
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

        layout_root = QtWidgets.QHBoxLayout(settings)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        layout_root.addWidget(scroll_area)

        scroll_area_main_widget = QtWidgets.QWidget()
        scroll_area.setWidget(scroll_area_main_widget)
        scroll_area_main_layout = QtWidgets.QVBoxLayout()
        scroll_area_main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        scroll_area_main_widget.setLayout(scroll_area_main_layout)

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(6)
        scroll_area_main_layout.addLayout(grid_layout)

        row = 0
        for name, obj in vars(VtkSphereSource).items():
            if isinstance(obj, property):
                if isinstance(self.__getattribute__(name), float):
                    label_widget = QtWidgets.QLabel(name)
                    label_widget.setMaximumWidth(150)
                    label_widget.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
                    grid_layout.addWidget(label_widget, row, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

                    value_widget = QtWidgets.QDoubleSpinBox()
                    value_widget.setValue(self.__getattribute__(name))
                    value_widget.valueChanged.connect(lambda value: self.__setattr__(name, value))
                    grid_layout.addWidget(value_widget, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
                    row += 1
                if isinstance(self.__getattribute__(name), int):
                    label_widget = QtWidgets.QLabel(name)
                    label_widget.setMaximumWidth(150)
                    label_widget.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
                    grid_layout.addWidget(label_widget, row, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

                    value_widget = QtWidgets.QSpinBox()
                    value_widget.setValue(self.__getattribute__(name))
                    value_widget.valueChanged.connect(lambda value: self.__setattr__(name, value))
                    grid_layout.addWidget(value_widget, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
                    row += 1

        return settings

    def outputPort(self):
        return self._source.GetOutputPort()
