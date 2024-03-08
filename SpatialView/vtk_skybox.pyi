#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkRenderingCore import vtkMapper, vtkTexture
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLSkybox

class VtkSkybox:
    def __init__(self):
        self.skybox: vtkOpenGLSkybox = None

    @property
    def texture(self) -> vtkTexture: ...
    @texture.setter
    def texture(self, value: vtkTexture): ...
    @staticmethod
    def projectionName(value) -> str: ...
    @property
    def projectionMax(self) -> int: ...
    @property
    def projectionMin(self) -> int: ...
    @property
    def projection(self) -> int: ...
    @projection.setter
    def projection(self, value: int): ...
    @property
    def floorPlane(self) -> tuple[float, float, float, float]: ...
    @floorPlane.setter
    def floorPlane(self, value: tuple[float, float, float, float]): ...
    @property
    def floorRight(self) -> tuple[float, float, float]: ...
    @floorRight.setter
    def floorRight(self, value: tuple[float, float, float]): ...
    @property
    def gammaCorrect(self) -> bool: ...
    @gammaCorrect.setter
    def gammaCorrect(self, value: bool): ...