#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import (
    vtkImplicitHalo,
)

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Halo",
    category="SDF/Ops",
)
class VtkImplicitHaloModel(NodeModelTemplate):
    @property
    def center(self):
        return self._ops.GetCenter()

    @center.setter
    def center(self, value):
        self._ops.SetCenter(value)
        self._renderer.interactorRender()

    @property
    def radius(self):
        return self._ops.GetRadius()

    @radius.setter
    def radius(self, value):
        self._ops.SetRadius(value)
        self._renderer.interactorRender()

    @property
    def fadeOut(self):
        return self._ops.GetFadeOut()

    @fadeOut.setter
    def fadeOut(self, value):
        self._ops.SetFadeOut(value)
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
        self._ops = vtkImplicitHalo()
