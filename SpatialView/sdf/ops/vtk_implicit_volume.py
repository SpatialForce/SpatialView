#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import (
    vtkImplicitVolume,
)

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Volume",
    category="SDF/Ops",
)
class VtkImplicitVolumeModel(NodeModelTemplate):
    @property
    def outGradient(self):
        return self._ops.GetOutGradient()

    @outGradient.setter
    def outGradient(self, value):
        self._ops.SetOutGradient(value)
        self._renderer.interactorRender()

    @property
    def outValue(self):
        return self._ops.GetOutValue()

    @outValue.setter
    def outValue(self, value):
        self._ops.SetOutValue(value)
        self._renderer.interactorRender()

    @property
    def volume(self):
        return self._ops.GetVolume()

    @volume.setter
    def volume(self, value):
        self._ops.SetVolume(value)
        self._renderer.interactorRender()

    @volume.setter
    def volume(self, value):
        self._ops.SetVolume(value)
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
        self._ops = vtkImplicitVolume()
