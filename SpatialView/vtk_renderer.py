#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTerrain
from vtkmodules.vtkRenderingCore import vtkRenderer, vtkRenderWindowInteractor


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
        self.handle = vtkRenderer()
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

    @property
    def environmentTexture(self):
        return self.handle.GetEnvironmentTexture()

    @environmentTexture.setter
    def environmentTexture(self, value):
        self.handle.UseSphericalHarmonicsOn()
        self.handle.SetEnvironmentTexture(value, False)
