#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from PySide6 import QtWidgets, QtCore

from SpatialView.ui.abstract_widget_type import AbstractWidgetType


class NodeModelTemplate(sNode.NodeDelegateModel):
    @staticmethod
    def makeRegistrar():
        registry: dict[str, AbstractWidgetType] = {}

        def registerParam(type: AbstractWidgetType):
            def registrar(func):
                type.property = func.fget.__name__
                registry[func.fget.__name__] = type
                return func  # normally a decorator returns a wrapped function,
                # but here we return func unmodified, after registering it

            return registrar

        registerParam.all = registry
        return registerParam

    withProperty = makeRegistrar()

    def dialog(self):
        settings = QtWidgets.QDialog()
        settings.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Popup
        )
        settings.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        settings.setWindowTitle(f"{type(self).__name__} Settings")

        layout_root = QtWidgets.QHBoxLayout(settings)
        layout_root.setContentsMargins(0, 0, 0, 0)
        layout_root.setSpacing(0)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
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
        registry: dict[str, AbstractWidgetType] = self.withProperty.all
        for name in registry:
            label_widget = QtWidgets.QLabel(name)
            label_widget.setMaximumWidth(150)
            label_widget.setTextInteractionFlags(
                QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
            )
            grid_layout.addWidget(
                label_widget, row, 0, QtCore.Qt.AlignmentFlag.AlignLeft
            )

            grid_layout.addWidget(
                registry[name].render(self), row, 1, QtCore.Qt.AlignmentFlag.AlignLeft
            )

            row += 1

        return settings

    def __init__(self):
        super().__init__()
        self._label = QtWidgets.QLabel("Settings")
        self._label.installEventFilter(self)
        self._label.setStyleSheet(
            "QLabel { background-color : transparent; color : white; }"
        )

    @override
    def eventFilter(self, object, event):
        if object == self._label:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                setting = self.dialog()
                setting.exec()
                return True
        return False

    @override
    def embeddedWidget(self):
        return self._label

    def save(self):
        modelJson = super().save()

        source = sNode.QJsonObject()
        registry: dict[str, AbstractWidgetType] = self.withProperty.all
        for name in registry:
            registry[name].save(source, self)
        modelJson["source"] = source

        return modelJson

    def load(self, p):
        source = p["source"]
        registry: dict[str, AbstractWidgetType] = self.withProperty.all
        for name in registry:
            registry[name].load(source, self)
