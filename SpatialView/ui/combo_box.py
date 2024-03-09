#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial


class ComboBox(AbstractWidgetType):
    def __init__(self, minValue: str, maxValue: str, description):
        super().__init__()
        self.minValue = minValue
        self.maxValue = maxValue
        self.description = description

    def render(self, target):
        value_widget = QtWidgets.QComboBox()
        for index in range(
            target.__getattribute__(self.minValue),
            target.__getattribute__(self.maxValue) + 1,
        ):
            value_widget.addItem(self.description(index))

        value_widget.setCurrentIndex(target.__getattribute__(self.property))
        value_widget.activated.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget
