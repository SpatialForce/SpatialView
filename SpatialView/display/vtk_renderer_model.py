#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from SpatialView.node_model_template import (
    withModel,
    NodeModelTemplate,
    withProperty,
)
from SpatialView.ui import CheckBox
from SpatialView.display.vtk_renderer import Renderer


@withModel(
    capStr="Vtk Renderer Settings",
    category="Displays",
)
class VtkRendererSettingsModel(NodeModelTemplate):
    @property
    def useImageBasedLighting(self):
        return self._renderer.useImageBasedLighting

    @withProperty(CheckBox())
    @useImageBasedLighting.setter
    def useImageBasedLighting(self, value):
        self._renderer.useImageBasedLighting = value

    @property
    def useSphericalHarmonics(self):
        return self._renderer.useSphericalHarmonics

    @withProperty(CheckBox())
    @useSphericalHarmonics.setter
    def useSphericalHarmonics(self, value):
        self._renderer.useSphericalHarmonics = value

    @property
    def useFXAA(self):
        return self._renderer.useFXAA

    @withProperty(CheckBox())
    @useFXAA.setter
    def useFXAA(self, value):
        self._renderer.useFXAA = value

    @property
    def useShadows(self):
        return self._renderer.useShadows

    @withProperty(CheckBox())
    @useShadows.setter
    def useShadows(self, value):
        self._renderer.useShadows = value

    def __init__(self):
        super().__init__()

        # Create a mapper
        self._renderer: Renderer = Renderer()
