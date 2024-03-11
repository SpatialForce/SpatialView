#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersCore import vtkContourFilter

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Contour Filter",
    category="SDF",
)
class VtkContourFilterModel(NodeModelTemplate):
    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def func(self):
        return self._mapper.GetOutputPort(0)

    @property
    def inPort(self):
        return self._mapper.GetInputConnection(0, 0)

    @withPort(0, sNode.PortType.In, TypeID.ALGORITHM)
    @inPort.setter
    def inPort(self, value):
        if value:
            self._mapper.SetInputConnection(value)
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create a mapper
        self._mapper = vtkContourFilter()
