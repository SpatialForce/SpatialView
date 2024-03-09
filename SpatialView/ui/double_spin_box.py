#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial


class DoubleSpinBox(AbstractWidgetType):
    def __init__(self, minValue: str | float, maxValue: str | float, step=0.2):
        super().__init__()
        self.minValue = minValue
        self.maxValue = maxValue
        self.step = step

    def render(self, target):
        value_widget = QtWidgets.QDoubleSpinBox()
        value_widget.setSingleStep(self.step)
        if isinstance(self.maxValue, str):
            value_widget.setMaximum(target.__getattribute__(self.maxValue))
        else:
            value_widget.setMaximum(self.maxValue)
        if isinstance(self.minValue, str):
            value_widget.setMinimum(target.__getattribute__(self.minValue))
        else:
            value_widget.setMinimum(self.minValue)
        value_widget.setValue(target.__getattribute__(self.property))
        value_widget.valueChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget
