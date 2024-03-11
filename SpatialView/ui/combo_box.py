#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial


class ComboBox(AbstractWidgetType):
    def __init__(self, minValue: str | int, maxValue: str | int, description):
        super().__init__()
        self.minValue = minValue
        self.maxValue = maxValue
        self.description = description

    def render(self, target):
        value_widget = QtWidgets.QComboBox()
        if isinstance(self.minValue, str):
            start = target.__getattribute__(self.minValue)
        else:
            start = self.minValue

        if isinstance(self.maxValue, str):
            end = target.__getattribute__(self.maxValue)
        else:
            end = self.maxValue

        for index in range(start, end + 1):
            value_widget.addItem(self.description(index))

        value_widget.setCurrentIndex(target.__getattribute__(self.property))
        value_widget.activated.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget
