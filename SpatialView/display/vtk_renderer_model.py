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
from SpatialView.ui import CheckBox, DoubleSpinBox, SpinBox
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

    # =========== SSAO ======================================================

    @property
    def useSSAO(self):
        return self._renderer.useSSAO

    @withProperty(CheckBox())
    @useSSAO.setter
    def useSSAO(self, value):
        self._renderer.useSSAO = value

    @property
    def ssaoBlur(self):
        return self._renderer.ssaoBlur

    @withProperty(CheckBox())
    @ssaoBlur.setter
    def ssaoBlur(self, value):
        self._renderer.ssaoBlur = value

    @property
    def ssaoBias(self):
        return self._renderer.ssaoBias

    @withProperty(DoubleSpinBox(0.0, 10.0, 0.1))
    @ssaoBias.setter
    def ssaoBias(self, value):
        self._renderer.ssaoBias = value

    @property
    def ssaoRadius(self):
        return self._renderer.ssaoRadius

    @withProperty(DoubleSpinBox(0.0, 10.0, 0.1))
    @ssaoRadius.setter
    def ssaoRadius(self, value):
        self._renderer.ssaoRadius = value

    @property
    def ssaoKernelSize(self):
        return self._renderer.ssaoKernelSize

    @withProperty(SpinBox(0, 10))
    @ssaoKernelSize.setter
    def ssaoKernelSize(self, value):
        self._renderer.ssaoKernelSize = value

    # =========== Irradiance ======================================================

    @property
    def irradianceSize(self):
        return self._renderer.irradianceSize

    @withProperty(SpinBox(0, 10))
    @irradianceSize.setter
    def irradianceSize(self, value):
        self._renderer.irradianceSize = value

    @property
    def irradianceStep(self):
        return self._renderer.irradianceStep

    @withProperty(DoubleSpinBox(0.0, 1.0, 0.1))
    @irradianceStep.setter
    def irradianceStep(self, value):
        self._renderer.irradianceStep = value

    def __init__(self):
        super().__init__()

        # Create a mapper
        self._renderer: Renderer = Renderer()
