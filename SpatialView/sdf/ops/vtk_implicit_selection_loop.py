#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import (
    vtkImplicitSelectionLoop,
)

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Selection Loop",
    category="SDF/Ops",
)
class VtkImplicitSelectionLoopModel(NodeModelTemplate):
    @property
    def loop(self):
        return self._ops.GetLoop()

    @loop.setter
    def loop(self, value):
        self._ops.SetLoop(value)
        self._renderer.interactorRender()

    @property
    def normal(self):
        return self._ops.GetNormal()

    @normal.setter
    def normal(self, value):
        self._ops.SetNormal(value)
        self._renderer.interactorRender()

    @property
    def automaticNormalGeneration(self):
        return self._ops.GetAutomaticNormalGeneration()

    @automaticNormalGeneration.setter
    def automaticNormalGeneration(self, value):
        self._ops.SetAutomaticNormalGeneration(value)
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
        self._ops = vtkImplicitSelectionLoop()
