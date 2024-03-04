#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkSphereSource

from SpatialView.vtk_algo_data import VtkAlgoData


class VtkSphereModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkSphereSource()
        self._source.SetCenter(0, 0, 0)
        self._source.SetRadius(0.5)

    @override
    def caption(self):
        return "Vtk Sphere Source"

    @override
    def captionVisible(self):
        return True

    @override
    def name(self):
        return "VtkSphereModel"

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
