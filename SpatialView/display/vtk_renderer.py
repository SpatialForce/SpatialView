#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionStyle import (
    vtkInteractorStyleTerrain,
    vtkInteractorStyleDrawPolygon,
    vtkInteractorStyleFlight,
    vtkInteractorStyleJoystickActor,
    vtkInteractorStyleJoystickCamera,
    vtkInteractorStyleRubberBand2D,
    vtkInteractorStyleRubberBandZoom,
    vtkInteractorStyleTrackballActor,
)
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLRenderer

from SpatialView.node_model_template import withProperty
from SpatialView.ui.combo_box import ComboBox


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
        self._cameraOrientationWidget: vtkCameraOrientationWidget | None = None
        self._interactorStyle = 0

    @property
    def interactor(self) -> vtkRenderWindowInteractor:
        return self._interactor

    @interactor.setter
    def interactor(self, value: vtkRenderWindowInteractor):
        self._interactor = value
        self.interactorStyle = 6

        self._cameraOrientationWidget = vtkCameraOrientationWidget()
        self._cameraOrientationWidget.SetParentRenderer(self.handle)
        # Enable the widget.
        self._cameraOrientationWidget.On()

    def interactorRender(self):
        self._interactor.Render()

    @staticmethod
    def interactorStyleObj(value):
        match value:
            case 0:
                return vtkInteractorStyleDrawPolygon()
            case 1:
                return vtkInteractorStyleFlight()
            case 2:
                return vtkInteractorStyleJoystickActor()
            case 3:
                return vtkInteractorStyleJoystickCamera()
            case 4:
                return vtkInteractorStyleRubberBand2D()
            case 5:
                return vtkInteractorStyleRubberBandZoom()
            case 6:
                return vtkInteractorStyleTerrain()
            case 7:
                return vtkInteractorStyleTrackballActor()

    @property
    def interactorStyle(self):
        return self._interactorStyle

    @interactorStyle.setter
    def interactorStyle(self, value):
        self._interactorStyle = value
        self._interactor.SetInteractorStyle(self.interactorStyleObj(value))

    # ================== Renderer =============================================

    def resetCamera(self):
        self.handle.ResetCamera()
        self.handle.ResetCameraClippingRange()

    @property
    def useImageBasedLighting(self):
        return self.handle.GetUseImageBasedLighting()

    @useImageBasedLighting.setter
    def useImageBasedLighting(self, value):
        self.handle.SetUseImageBasedLighting(value)
        self.resetCamera()
        # self.interactorRender() will be black

    @property
    def useSphericalHarmonics(self):
        return self.handle.GetUseSphericalHarmonics()

    @useSphericalHarmonics.setter
    def useSphericalHarmonics(self, value):
        self.handle.SetUseSphericalHarmonics(value)
        # self.interactorRender() will be black

    @property
    def environmentTexture(self):
        return self.handle.GetEnvironmentTexture()

    @environmentTexture.setter
    def environmentTexture(self, value):
        self.useImageBasedLighting = True
        self.useSphericalHarmonics = True
        self.handle.SetEnvironmentTexture(value, False)
        # self.interactorRender() will be black

    @property
    def useFXAA(self):
        return self.handle.GetUseFXAA()

    @useFXAA.setter
    def useFXAA(self, value):
        self.handle.SetUseFXAA(value)
        self.interactorRender()

    @property
    def useShadows(self):
        return self.handle.GetUseShadows()

    @useShadows.setter
    def useShadows(self, value):
        self.handle.SetUseShadows(value)
        self.interactorRender()

    # =========== SSAO ======================================================

    @property
    def useSSAO(self):
        return self.handle.GetUseSSAO()

    @useSSAO.setter
    def useSSAO(self, value):
        self.handle.SetUseSSAO(value)
        self.interactorRender()

    @property
    def ssaoBlur(self):
        return self.handle.GetSSAOBlur()

    @ssaoBlur.setter
    def ssaoBlur(self, value):
        self.handle.SetSSAOBlur(value)
        self.interactorRender()

    @property
    def ssaoBias(self):
        return self.handle.GetSSAOBias()

    @ssaoBias.setter
    def ssaoBias(self, value):
        self.handle.SetSSAOBias(value)
        self.interactorRender()

    @property
    def ssaoRadius(self):
        return self.handle.GetSSAORadius()

    @ssaoRadius.setter
    def ssaoRadius(self, value):
        self.handle.SetSSAORadius(value)
        self.interactorRender()

    @property
    def ssaoKernelSize(self):
        return self.handle.GetSSAOKernelSize()

    @ssaoKernelSize.setter
    def ssaoKernelSize(self, value):
        self.handle.SetSSAOKernelSize(value)
        self.interactorRender()

    # =========== Irradiance ======================================================

    @property
    def irradianceSize(self):
        return self.handle.GetEnvMapIrradiance().GetIrradianceSize()

    @irradianceSize.setter
    def irradianceSize(self, value):
        self.handle.GetEnvMapIrradiance().SetIrradianceSize(value)
        self.interactorRender()

    @property
    def irradianceStep(self):
        return self.handle.GetEnvMapIrradiance().GetIrradianceStep()

    @irradianceStep.setter
    def irradianceStep(self, value):
        self.handle.GetEnvMapIrradiance().SetIrradianceStep(value)
        self.interactorRender()
