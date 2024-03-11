#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkImplicitBoolean

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Boolean",
    category="SDF/Ops",
)
class VtkImplicitBooleanModel(NodeModelTemplate):
    @property
    def operationTypeMax(self):
        return self._ops.GetOperationTypeMaxValue()

    @property
    def operationTypeMin(self):
        return self._ops.GetOperationTypeMinValue()

    @property
    def operationType(self):
        return self._ops.GetOperationType()

    @operationType.setter
    def operationType(self, value):
        self._ops.SetOperationType(value)
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
        self._ops = vtkImplicitBoolean()
