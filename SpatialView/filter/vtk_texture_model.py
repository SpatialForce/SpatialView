#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkTexture

from SpatialView.node_data.vtk_texture_data import VtkTextureData
from SpatialView.node_model_template import NodeModelTemplate, withPort, withModel
from SpatialView.node_data.vtk_algo_data import VtkAlgoData


@withModel(
    capStr="Vtk Texture",
    category="Operators",
)
class VtkTextureModel(NodeModelTemplate):
    @withPort(0, sNode.PortType.Out, VtkTextureData)
    @property
    def outPort(self):
        return self._texture

    @property
    def inPort(self):
        return self._texture.GetInputConnection(0, 0)

    @withPort(0, sNode.PortType.In, VtkAlgoData)
    @inPort.setter
    def inPort(self, value):
        self._texture.SetInputConnection(value.algo())
        self._texture.MipmapOn()
        self._texture.InterpolateOn()
        self.dataUpdated.emit(0)

    def __init__(self):
        super().__init__()

        # Create a mapper
        self._texture = vtkTexture()
        self._texture.SetColorModeToDirectScalars()
