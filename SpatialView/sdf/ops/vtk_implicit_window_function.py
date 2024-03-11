#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import (
    vtkImplicitWindowFunction,
)

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Window Function",
    category="SDF/Ops",
)
class VtkImplicitWindowFunctionModel(NodeModelTemplate):
    @property
    def windowRange(self):
        return self._ops.GetWindowRange()

    @windowRange.setter
    def windowRange(self, value):
        self._ops.SetWindowRange(value)
        self._renderer.interactorRender()

    @property
    def windowValues(self):
        return self._ops.GetWindowValues()

    @windowValues.setter
    def windowValues(self, value):
        self._ops.SetWindowValues(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def outPort(self):
        return self._ops

    @property
    def inPort(self):
        return self._ops.GetFunction()

    @withPort(0, sNode.PortType.In, TypeID.ALGORITHM)
    @inPort.setter
    def inPort(self, value):
        if value:
            self._ops.AddFunction(value)
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create a mapper
        self._ops = vtkImplicitWindowFunction()
