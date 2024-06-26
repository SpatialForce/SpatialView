#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.
import copy
from collections import defaultdict
from typing import override

import SpatialNode as sNode
from PySide6 import QtWidgets, QtCore

from SpatialView.type_id import TypeID
from SpatialView.ui.abstract_widget_type import AbstractWidgetType


widgetRegistry: defaultdict[str, defaultdict[str, AbstractWidgetType]] = defaultdict(
    defaultdict
)


def withProperty(widgetType: AbstractWidgetType):
    def registrar(func):
        className = func.fget.__qualname__.split(".")
        widgetType.property = func.fget.__name__
        widgetRegistry[className[0]][func.fget.__name__] = widgetType
        return func

    return registrar


class PortInfo:
    def __init__(
        self, property: str, portIndex: int, portType: sNode.PortType, dataType: TypeID
    ):
        self.property = property
        self.portIndex = portIndex
        self.portType = portType
        self.dataType = dataType


portRegistry: defaultdict[str, defaultdict[str, PortInfo]] = defaultdict(defaultdict)


def withPort(portIndex: int, portType: sNode.PortType, dataType: TypeID):
    def registrar(func):
        className = func.fget.__qualname__.split(".")
        info = PortInfo(func.fget.__name__, portIndex, portType, dataType)
        portRegistry[className[0]][func.fget.__name__] = info
        return func

    return registrar


modelRegistry = sNode.NodeDelegateModelRegistry()


def withModel(capStr: str, category: str = "Nodes"):
    def caption(self):
        return capStr

    def registrar(CLS):
        CLS.caption = caption
        modelRegistry.registerModel(CLS, capStr, category)
        return CLS

    return registrar


class NodeModelTemplate(sNode.NodeDelegateModel):
    def getRegistry(self) -> defaultdict[str, AbstractWidgetType]:
        d = widgetRegistry[type(self).__name__]
        targets = type(self).__bases__
        for target in targets:
            d.update(widgetRegistry[target.__name__])
        return d

    def getPorts(self):
        d = portRegistry[type(self).__name__]
        targets = type(self).__bases__
        for target in targets:
            d.update(portRegistry[target.__name__])
        return d

    def dialog(self):
        registry = self.getRegistry()
        if len(registry) == 0:
            return

        settings = QtWidgets.QDialog()
        settings.setWindowFlags(QtCore.Qt.WindowType.Tool)
        settings.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        settings.setWindowTitle(f"{self.caption()} Settings")

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
        settings.exec()

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
                self.dialog()
                return True
        return False

    @override
    def embeddedWidget(self):
        return self._label

    def save(self):
        modelJson = sNode.QJsonObject()
        modelJson["model-name"] = self.caption()

        source = sNode.QJsonObject()
        registry = self.getRegistry()
        for name in registry:
            registry[name].save(source, self)
        modelJson["source"] = source

        return modelJson

    def load(self, p):
        source = p["source"]
        registry = self.getRegistry()
        for name in registry:
            registry[name].load(source, self)

    @override
    def nPorts(self, portType):
        ports = self.getPorts()
        outResult = 0
        inResult = 0
        for port in ports:
            if ports[port].portType == sNode.PortType.In:
                inResult += 1
            else:
                outResult += 1

        match portType:
            case sNode.PortType.In:
                return inResult
            case sNode.PortType.Out:
                return outResult

    @override
    def dataType(self, portType, portIndex):
        ports = self.getPorts()
        for port in ports:
            info = ports[port]
            if info.portType == portType and info.portIndex == portIndex:
                return sNode.NodeDataType(info.dataType.value, info.property)

    @override
    def outData(self, portIndex):
        ports = self.getPorts()
        for port in ports:
            info = ports[port]
            if info.portType == sNode.PortType.Out and info.portIndex == portIndex:
                return self.__getattribute__(info.property)

    @override
    def setInData(self, nodeData, portIndex):
        ports = self.getPorts()
        for port in ports:
            info = ports[port]
            if info.portType == sNode.PortType.In and info.portIndex == portIndex:
                type(self).__setattr__(self, info.property, nodeData)

    @override
    def captionVisible(self):
        return True
