#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTerrain
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLRenderer


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Renderer:
    def __init__(self):
        self.handle = vtkOpenGLRenderer()
        self.handle.SetBackground(vtkNamedColors().GetColor3d("DimGray"))
        self._interactor: vtkRenderWindowInteractor | None = None

    @property
    def interactor(self) -> vtkRenderWindowInteractor:
        return self._interactor

    @interactor.setter
    def interactor(self, value: vtkRenderWindowInteractor):
        self._interactor = value
        self._interactor.SetInteractorStyle(vtkInteractorStyleTerrain())

    def reset(self):
        self.handle.ResetCamera()
        self.handle.ResetCameraClippingRange()
        self._interactor.ReInitialize()

    def modified(self):
        self.handle.Modified()

    @property
    def useImageBasedLighting(self):
        return self.handle.GetUseImageBasedLighting()

    @useImageBasedLighting.setter
    def useImageBasedLighting(self, value):
        self.handle.SetUseImageBasedLighting(value)
        self.modified()

    @property
    def useSphericalHarmonics(self):
        return self.handle.GetUseSphericalHarmonics()

    @useSphericalHarmonics.setter
    def useSphericalHarmonics(self, value):
        self.handle.SetUseSphericalHarmonics(value)
        self.modified()

    @property
    def environmentTexture(self):
        return self.handle.GetEnvironmentTexture()

    @environmentTexture.setter
    def environmentTexture(self, value):
        self.useImageBasedLighting = True
        self.useSphericalHarmonics = True
        self.handle.SetEnvironmentTexture(value, False)
        self.modified()

    @property
    def useFXAA(self):
        return self.handle.GetUseFXAA()

    @useFXAA.setter
    def useFXAA(self, value):
        self.handle.SetUseFXAA(value)
        self.modified()

    @property
    def useShadows(self):
        return self.handle.GetUseShadows()

    @useShadows.setter
    def useShadows(self, value):
        self.handle.SetUseShadows(value)
        self.modified()

    # =========== SSAO ======================================================

    @property
    def useSSAO(self):
        return self.handle.GetUseSSAO()

    @useSSAO.setter
    def useSSAO(self, value):
        self.handle.SetUseSSAO(value)
        self.modified()

    @property
    def ssaoBlur(self):
        return self.handle.GetSSAOBlur()

    @ssaoBlur.setter
    def ssaoBlur(self, value):
        self.handle.SetSSAOBlur(value)
        self.modified()

    @property
    def ssaoBias(self):
        return self.handle.GetSSAOBias()

    @ssaoBias.setter
    def ssaoBias(self, value):
        self.handle.SetSSAOBias(value)
        self.modified()

    @property
    def ssaoRadius(self):
        return self.handle.GetSSAORadius()

    @ssaoRadius.setter
    def ssaoRadius(self, value):
        self.handle.SetSSAORadius(value)
        self.modified()

    @property
    def ssaoKernelSize(self):
        return self.handle.GetSSAOKernelSize()

    @ssaoKernelSize.setter
    def ssaoKernelSize(self, value):
        self.handle.SetSSAOKernelSize(value)
        self.modified()

    # =========== Irradiance ======================================================

    @property
    def irradianceSize(self):
        return self.handle.GetEnvMapIrradiance().GetIrradianceSize()

    @irradianceSize.setter
    def irradianceSize(self, value):
        self.handle.GetEnvMapIrradiance().SetIrradianceSize(value)
        self.modified()

    @property
    def irradianceStep(self):
        return self.handle.GetEnvMapIrradiance().GetIrradianceStep()

    @irradianceStep.setter
    def irradianceStep(self, value):
        self.handle.GetEnvMapIrradiance().SetIrradianceStep(value)
        self.modified()
