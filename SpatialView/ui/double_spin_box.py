#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial


class DoubleSpinBox(AbstractWidgetType):
    def __init__(self, minValue: str, maxValue: str, step=0.2):
        self.property = None
        self.minValue = minValue
        self.maxValue = maxValue
        self.step = step

    def render(self, target):
        value_widget = QtWidgets.QDoubleSpinBox()
        value_widget.setSingleStep(self.step)
        value_widget.setMaximum(target.__getattribute__(self.maxValue))
        value_widget.setMinimum(target.__getattribute__(self.minValue))
        value_widget.setValue(target.__getattribute__(self.property))
        value_widget.valueChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget

    def save(self, p, target):
        p[self.property] = target.__getattribute__(self.property)

    def load(self, p, target):
        type(target).__setattr__(target, self.property, p[self.property])
