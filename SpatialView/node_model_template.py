#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import abc
from typing import override, Any

import SpatialNode as sNode
from PySide6 import QtWidgets
from SpatialNode import QJsonObject


class AbstractWidgetType:
    @abc.abstractmethod
    def render(self): ...

    @abc.abstractmethod
    def save(self): ...

    @abc.abstractmethod
    def load(self, p): ...


class DoubleSliderType(AbstractWidgetType):
    def __init__(self, fset, fget, min_value, max_value, step=0.2):
        self.fset = fset
        self.fget = fget
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

    def render(self):
        value_widget = QtWidgets.QDoubleSpinBox()
        value_widget.setSingleStep(self.step)
        value_widget.setMaximum(self.max_value())
        value_widget.setMinimum(self.min_value())
        value_widget.setValue(self.fget())
        value_widget.valueChanged.connect(self.fset)

    def save(self):
        source = QJsonObject()
        source[self.fget.__name__] = self.fget()

    def load(self, p):
        self.fset(p[self.fset.__name__])


class NodeModelTemplate(sNode.NodeDelegateModel):
    @staticmethod
    def makeRegistrar():
        registry = {}

        def registerParam(type: AbstractWidgetType):
            def registrar(func):
                registry[func.fget.__name__] = (func, type)
                return func  # normally a decorator returns a wrapped function,
                # but here we return func unmodified, after registering it

            return registrar

        registerParam.all = registry
        return registerParam

    reg = makeRegistrar()

    def __init__(self):
        super().__init__()

    @override
    def embeddedWidget(self):
        registry: dict[str, (Any, AbstractWidgetType)] = self.reg.all
        for name, info in registry:
            print(name)

    def save(self): ...

    def load(self, p): ...
