#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkCylinderSource

from SpatialView.vtk_algo_data import VtkAlgoData


class VtkCylinderSourceModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkCylinderSource()
        self._source.SetCenter(0, 0, 0)
        self._source.SetRadius(0.5)

    @override
    def caption(self):
        return "Vtk Cylinder Source"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkCylinderSource"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        registry.registerModel(
            VtkCylinderSourceModel, VtkCylinderSourceModel.name(), "Sources"
        )

    @override
    def nPorts(self, portType):
        result = 1
        match portType:
            case sNode.PortType.In:
                result = 0
            case sNode.PortType.Out:
                result = 1
        return result

    @override
    def dataType(self, portType, portIndex):
        return VtkAlgoData().type()

    @override
    def outData(self, port):
        return VtkAlgoData(self._source.GetOutputPort())

    @override
    def setInData(self, nodeData, portIndex): ...

    @override
    def embeddedWidget(self):
        return None
