#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkRenderer, vtkActor

from SpatialView.vtk_mapper_data import VtkMapperData


class VtkDisplayActorModel(sNode.NodeDelegateModel):
    def __init__(self, render: vtkRenderer):
        super().__init__()
        self._actor = vtkActor()
        render.AddActor(self._actor)

    @override
    def caption(self):
        return "Actor Display"

    @override
    def captionVisible(self):
        return False

    @override
    def name(self):
        return "VtkDisplayActorModel"

    @override
    def nPorts(self, portType):
        result = 1
        match portType:
            case sNode.PortType.In:
                result = 1
            case sNode.PortType.Out:
                result = 0
        return result

    @override
    def dataType(self, portType, portIndex):
        return VtkMapperData().type()

    @override
    def outData(self, port):
        return None

    @override
    def setInData(self, nodeData, portIndex):
        mapper = None
        if isinstance(nodeData, VtkMapperData):
            mapper = nodeData.mapper()

        self._actor.SetMapper(mapper)

    @override
    def embeddedWidget(self):
        return None
