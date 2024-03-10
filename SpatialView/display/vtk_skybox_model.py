#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import (
    vtkSkybox,
)
from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLSkybox

from SpatialView.node_model_template import (
    withModel,
    NodeModelTemplate,
    withProperty,
    withPort,
)
from .vtk_renderer import Renderer
from SpatialView.ui import CheckBox
from SpatialView.ui.combo_box import ComboBox
from ..type_id import TypeID


@withModel(
    capStr="Vtk Skybox",
    category="Displays",
)
class VtkSkyboxModel(NodeModelTemplate):
    @property
    def texture(self):
        return self._skybox.GetTexture()

    @texture.setter
    def texture(self, value):
        self._skybox.SetTexture(value)
        self._renderer.environmentTexture = value

    @property
    def inPort(self):
        return self.texture

    @withPort(0, sNode.PortType.In, TypeID.TEXTURE)
    @inPort.setter
    def inPort(self, value):
        if value:
            self.texture = value
            if not self._isAdded:
                self._renderer.handle.AddActor(self._skybox)
                self._isAdded = True
        else:
            self.texture = None
            self._renderer.handle.RemoveActor(self._skybox)
            self._isAdded = False

    @staticmethod
    def projectionName(value):
        match value:
            case 0:
                return "Cube"
            case 1:
                return "Sphere"
            case 2:
                return "Floor"
            case 3:
                return "StereoSphere"

    @property
    def projectionMax(self):
        return 3

    @property
    def projectionMin(self):
        return 0

    @property
    def projection(self):
        return self._skybox.GetProjection()

    @withProperty(ComboBox("projectionMin", "projectionMax", projectionName))
    @projection.setter
    def projection(self, value):
        self._skybox.SetProjection(value)
        self._renderer.interactorRender()

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

    @withProperty(CheckBox())
    @gammaCorrect.setter
    def gammaCorrect(self, value):
        self._skybox.SetGammaCorrect(value)
        self._renderer.interactorRender()

    def __init__(self):
        super().__init__()
        self._skybox = vtkOpenGLSkybox()
        self._skybox.SetFloorRight(0, 0, 1)
        self._skybox.SetProjection(vtkSkybox.Sphere)
        self._skybox.GammaCorrectOn()
        self._isAdded = False
        self._renderer: Renderer = Renderer()
