#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkCone

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk SDF Cone", category="SDF/geometries")
class VtkConeModel(NodeModelTemplate):
    @property
    def angleMax(self):
        return self._source.GetAngleMaxValue()

    @property
    def angleMin(self):
        return self._source.GetAngleMinValue()

    @property
    def angle(self):
        return self._source.GetAngle()

    @withProperty(DoubleSpinBox("angleMin", "angleMax", 0.1))
    @angle.setter
    def angle(self, value):
        self._source.SetAngle(value)

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkCone()
