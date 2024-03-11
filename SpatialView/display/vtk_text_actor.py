#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import (
    vtkSkybox,
    vtkTextActor,
)

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
    capStr="Vtk Text Actor",
    category="Displays",
)
class VtkTextActorModel(NodeModelTemplate):
    @property
    def text(self):
        return self._text.GetInput()

    @text.setter
    def text(self, value):
        self._text.SetInput(value)

    @property
    def fontSizeMax(self):
        return self._text.GetTextProperty().GetFontSizeMaxValue()

    @property
    def fontSizeMin(self):
        return self._text.GetTextProperty().GetFontSizeMinValue()

    @property
    def fontSize(self):
        return self._text.GetTextProperty().GetFontSize()

    @fontSize.setter
    def fontSize(self, value):
        self._text.GetTextProperty().SetFontSize(value)

    def __init__(self):
        super().__init__()
        self._text = vtkTextActor()
        self._isAdded = False
        self._renderer: Renderer = Renderer()
