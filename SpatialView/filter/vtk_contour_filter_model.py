#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkFiltersCore import vtkContourFilter

from SpatialView.vtk_algo_data import VtkAlgoData


class VtkContourFilterModel(sNode.NodeDelegateModel):
    def __init__(self):
        super().__init__()

        # Create a mapper
        self._mapper = vtkContourFilter()

    @override
    def caption(self):
        return "Vtk Contour Filter"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkContourFilterModel"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        registry.registerModel(
            VtkContourFilterModel, VtkContourFilterModel.name(), "Operators"
        )

    @override
    def nPorts(self, portType):
        return 1

    @override
    def dataType(self, portType, portIndex):
        return VtkAlgoData().type()

    @override
    def outData(self, port):
        return VtkAlgoData(self._mapper.GetOutputPort(0))

    @override
    def setInData(self, nodeData, portIndex):
        if isinstance(nodeData, VtkAlgoData):
            self._mapper.SetInputConnection(nodeData.algo())
            self.dataUpdated.emit(0)

    @override
    def embeddedWidget(self):
        return None
