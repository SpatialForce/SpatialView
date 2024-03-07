#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from SpatialNode import PortType
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper

from SpatialView.vtk_algo_data import VtkAlgoData
from SpatialView.filter.vtk_mapper_data import VtkMapperData


class VtkMapperDataModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create a mapper
        self._mapper = vtkPolyDataMapper()

    @override
    def caption(self):
        return "Vtk Mapper"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkMapperDataModel"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        registry.registerModel(
            VtkMapperDataModel, VtkMapperDataModel.name(), "Operators"
        )

    @override
    def nPorts(self, portType):
        return 1

    @override
    def dataType(self, portType, portIndex):
        match portType:
            case PortType.In:
                return VtkAlgoData().type()
            case PortType.Out:
                return VtkMapperData().type()

    @override
    def outData(self, port):
        return VtkMapperData(self._mapper)

    @override
    def setInData(self, nodeData, portIndex):
        if isinstance(nodeData, VtkAlgoData):
            self._mapper.SetInputConnection(nodeData.algo())
            self.dataUpdated.emit(0)

    @override
    def embeddedWidget(self):
        return None
