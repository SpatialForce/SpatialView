#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkPerlinNoise

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk SDF Perlin Noise", category="SDF/geometries")
class VtkPerlinNoiseModel(NodeModelTemplate):
    @property
    def frequency(self):
        return self._source.GetFrequency()

    @frequency.setter
    def frequency(self, value):
        self._source.SetFrequency(value)

    @property
    def amplitude(self):
        return self._source.GetAmplitude()

    @amplitude.setter
    def amplitude(self, value):
        self._source.SetAmplitude(value)
        self._renderer.interactorRender()

    @property
    def phase(self):
        return self._source.GetPhase()

    @phase.setter
    def phase(self, value):
        self._source.SetPhase(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkPerlinNoise()
