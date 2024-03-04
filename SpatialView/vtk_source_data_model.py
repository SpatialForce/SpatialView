#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper

from SpatialView.vtk_mapper_data import VtkMapperData


class VtkSourceDataModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create source
        source = vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(0.5)

        # Create a mapper
        self._mapper = vtkPolyDataMapper()
        self._mapper.SetInputConnection(source.GetOutputPort())

    @override
    def caption(self):
        return "Vtk Source"

    @override
    def captionVisible(self):
        return False

    @override
    def name(self):
        return "VtkSourceDataModel"

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
        return VtkMapperData().type()

    @override
    def outData(self, port):
        return VtkMapperData(self._mapper)

    @override
    def setInData(self, nodeData, portIndex): ...

    @override
    def embeddedWidget(self):
        return None
