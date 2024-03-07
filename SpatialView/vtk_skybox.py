#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkRenderingCore import vtkSkybox
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLSkybox


class VtkSkybox:
    def __init__(self):
        self.skybox = vtkOpenGLSkybox()
        self.skybox.SetFloorRight(0, 0, 1)
        self.skybox.SetProjection(vtkSkybox.Sphere)
        self.skybox.GammaCorrectOn()

    @property
    def texture(self):
        return self.skybox.GetTexture()

    @texture.setter
    def texture(self, value):
        self.skybox.SetTexture(value)

    @staticmethod
    def projectionName(value):
        match value:
            case 0:
                return vtkSkybox.Cube.__repr__()
            case 1:
                return vtkSkybox.Sphere.__repr__()
            case 2:
                return vtkSkybox.Floor.__repr__()
            case 3:
                return vtkSkybox.StereoSphere.__repr__()

    @property
    def projectionMax(self):
        return 3

    @property
    def projectionMin(self):
        return 0

    @property
    def projection(self):
        return self.skybox.GetProjection()

    @projection.setter
    def projection(self, value):
        self.skybox.SetProjection(value)

    @property
    def floorPlane(self):
        return self.skybox.GetFloorPlane()

    @floorPlane.setter
    def floorPlane(self, value):
        self.skybox.SetFloorPlane(value)

    @property
    def floorRight(self):
        return self.skybox.GetFloorRight()

    @floorRight.setter
    def floorRight(self, value):
        self.skybox.SetFloorRight(value)

    @property
    def gammaCorrect(self):
        return self.skybox.GetGammaCorrect()

    @gammaCorrect.setter
    def gammaCorrect(self, value):
        self.skybox.SetGammaCorrect(value)
