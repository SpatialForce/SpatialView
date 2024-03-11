#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import json
from PySide6 import QtWidgets, QtCore, QtGui

from SpatialView.ui.abstract_widget_type import AbstractWidgetType


class ColorPickerWidget(QtWidgets.QLabel):
    def __init__(self, target, property):
        super().__init__()
        self.setText("          ")
        self.setAutoFillBackground(True)

        self._target = target
        self._property = property

        colorProperty = target.__getattribute__(self._property)
        self._pal = QtGui.QPalette()
        self._pal.setColor(
            self.backgroundRole(),
            QtGui.QColor.fromRgbF(
                colorProperty[0], colorProperty[1], colorProperty[2], 1.0
            ),
        )
        self.setPalette(self._pal)

    def mousePressEvent(self, ev):
        color = self._target.__getattribute__(self._property)
        color = QtWidgets.QColorDialog.getColor(
            QtGui.QColor.fromRgbF(color[0], color[1], color[2], 1.0),
            None,
            "Select Color",
        )

        if not color.isValid():
            return

        self._pal.setColor(self.backgroundRole(), color)
        self.setPalette(self._pal)
        type(self._target).__setattr__(
            self._target,
            self._property,
            (color.redF(), color.greenF(), color.blueF()),
        )
        ev.accept()


class ColorPicker(AbstractWidgetType):
    def render(self, target):
        return ColorPickerWidget(target, self.property)

    def save(self, p, target):
        p[self.property] = json.dumps(target.__getattribute__(self.property))

    def load(self, p, target):
        data = p.get(self.property)
        if data:
            type(target).__setattr__(target, self.property, json.loads(data))
