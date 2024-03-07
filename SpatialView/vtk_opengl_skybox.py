#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkRenderingCore import vtkSkybox
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLSkybox


class VtkOpenGLSkybox:
    def __init__(self):
        self._skybox = vtkOpenGLSkybox()

    @property
    def texture(self):
        return self._skybox.GetTexture()

    @texture.setter
    def texture(self, value):
        self._skybox.SetTexture(value)

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
        return self._skybox.GetProjection()

    @projection.setter
    def projection(self, value):
        self._skybox.SetProjection(value)

    @property
    def floorPlane(self):
        return self._skybox.GetFloorPlane()

    @floorPlane.setter
    def floorPlane(self, value):
        self._skybox.SetFloorPlane(value)

    @property
    def floorRight(self):
        return self._skybox.GetFloorRight()

    @floorRight.setter
    def floorRight(self, value):
        self._skybox.SetFloorRight(value)

    @property
    def gammaCorrect(self):
        return self._skybox.GetGammaCorrect()

    @gammaCorrect.setter
    def gammaCorrect(self, value):
        self._skybox.SetGammaCorrect(value)

    # =========== Mapper ======================================================
    @property
    def mapper(self):
        return self._skybox.GetMapper()

    @mapper.setter
    def mapper(self, value):
        self._skybox.SetMapper(value)
