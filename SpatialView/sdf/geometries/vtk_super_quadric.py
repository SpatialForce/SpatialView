#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkQuadric, vtkSuperquadric

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk Superquadric", category="SDF/geometries")
class VtkSuperquadricModel(NodeModelTemplate):
    @property
    def center(self):
        return self._source.GetCenter()

    @center.setter
    def center(self, value):
        self._source.SetCenter(value)

    @property
    def size(self):
        return self._source.GetSize()

    @size.setter
    def size(self, value):
        self._source.SetSize(value)

    @property
    def thicknessMax(self):
        return self._source.GetThicknessMaxValue()

    @property
    def thicknessMin(self):
        return self._source.GetThicknessMinValue()

    @property
    def thickness(self):
        return self._source.GetThickness()

    @thickness.setter
    def thickness(self, value):
        self._source.SetThickness(value)

    @property
    def thetaRoundness(self):
        return self._source.GetThetaRoundness()

    @thetaRoundness.setter
    def thetaRoundness(self, value):
        self._source.SetThetaRoundness(value)

    @property
    def scale(self):
        return self._source.GetScale()

    @scale.setter
    def scale(self, value):
        self._source.SetScale(value)

    @property
    def toroidal(self):
        return self._source.GetToroidal()

    @toroidal.setter
    def toroidal(self, value):
        self._source.SetToroidal(value)

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkSuperquadric()
