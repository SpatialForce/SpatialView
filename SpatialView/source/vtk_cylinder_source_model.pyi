#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from PySide6 import QtWidgets

from SpatialView.source.vtk_cylinder_source import VtkCylinderSource

class VtkCylinderSourceModel(sNode.NodeDelegateModel):
    def __init__(self):
        self._source: VtkCylinderSource = None
        self._label: QtWidgets.QLabel = None

    @override
    def eventFilter(self, object, event): ...
    @override
    def caption(self): ...
    @override
    def captionVisible(self): ...
    @staticmethod
    @override
    def name(): ...
    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs): ...
    @override
    def nPorts(self, portType): ...
    @override
    def dataType(self, portType, portIndex): ...
    @override
    def outData(self, port): ...
    @override
    def setInData(self, nodeData, portIndex): ...
    @override
    def embeddedWidget(self): ...
    def load(self, p): ...
    def save(self): ...
