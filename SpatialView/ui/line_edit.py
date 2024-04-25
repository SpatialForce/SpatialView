#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets, QtGui

from SpatialView.ui.abstract_widget_type import AbstractWidgetType
from functools import partial
import json


class LineEdit(AbstractWidgetType):
    def render(self, target):
        value_widget = QtWidgets.QLineEdit()
        value_widget.setText(str(target.__getattribute__(self.property)))
        value_widget.textChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget


class IntLineEdit(AbstractWidgetType):
    def render(self, target):
        value_widget = QtWidgets.QLineEdit()
        value_widget.setValidator(QtGui.QIntValidator())
        value_widget.setText(str(target.__getattribute__(self.property)))
        value_widget.textChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget


class MultiIntLineEdit(AbstractWidgetType):
    def render(self, target):
        widget = QtWidgets.QWidget()
        layout_root = QtWidgets.QHBoxLayout(widget)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)

        tuples = list(target.__getattribute__(self.property))
        for i in range(len(tuples)):
            val = tuples[i]
            value_widget = QtWidgets.QLineEdit()
            value_widget.setValidator(QtGui.QIntValidator())
            value_widget.setText(str(val))

            def update(tuples, i, value):
                try:
                    tuples[i] = int(value)
                except:
                    pass
                type(target).__setattr__(target, self.property, tuples)

            value_widget.textEdited.connect(partial(update, tuples, i))

            layout_root.addWidget(value_widget)
        return widget

    def save(self, p, target):
        p[self.property] = json.dumps(target.__getattribute__(self.property))

    def load(self, p, target):
        data = p.get(self.property)
        if data:
            type(target).__setattr__(target, self.property, json.loads(data))


class DoubleLineEdit(AbstractWidgetType):
    def render(self, target):
        value_widget = QtWidgets.QLineEdit()
        value_widget.setValidator(QtGui.QDoubleValidator())
        value_widget.setText(str(target.__getattribute__(self.property)))
        value_widget.textChanged.connect(
            partial(type(target).__setattr__, target, self.property)
        )
        return value_widget


class MultiDoubleLineEdit(AbstractWidgetType):
    def render(self, target):
        widget = QtWidgets.QWidget()
        layout_root = QtWidgets.QHBoxLayout(widget)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)

        tuples = list(target.__getattribute__(self.property))
        for i in range(len(tuples)):
            val = tuples[i]
            value_widget = QtWidgets.QLineEdit()
            value_widget.setValidator(QtGui.QDoubleValidator())
            value_widget.setText(str(val))

            def update(tuples, i, value):
                try:
                    tuples[i] = float(value)
                except:
                    pass
                type(target).__setattr__(target, self.property, tuples)

            value_widget.textEdited.connect(partial(update, tuples, i))

            layout_root.addWidget(value_widget)
        return widget

    def save(self, p, target):
        p[self.property] = json.dumps(target.__getattribute__(self.property))

    def load(self, p, target):
        data = p.get(self.property)
        if data:
            type(target).__setattr__(target, self.property, json.loads(data))
