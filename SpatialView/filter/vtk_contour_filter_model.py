#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersCore import vtkContourFilter

from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.vtk_algo_data import VtkAlgoData


@withModel(
    capStr="Vtk Contour Filter",
    category="Operators",
)
class VtkContourFilterModel(NodeModelTemplate):
    @withPort(0, sNode.PortType.Out, VtkAlgoData)
    @property
    def outPort(self):
        return self._mapper.GetOutputPort(0)

    @property
    def inPort(self):
        return self._mapper.GetInputConnection(0, 0)

    @withPort(0, sNode.PortType.In, VtkAlgoData)
    @inPort.setter
    def inPort(self, value):
        self._mapper.SetInputConnection(value.algo())
        self.dataUpdated.emit(0)

    def __init__(self):
        super().__init__()

        # Create a mapper
        self._mapper = vtkContourFilter()
