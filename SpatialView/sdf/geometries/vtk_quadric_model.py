#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkQuadric

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk SDF Quadric", category="SDF/geometries")
class VtkQuadricModel(NodeModelTemplate):
    @property
    def coefficients(self):
        return self._source.GetCoefficients()

    @coefficients.setter
    def coefficients(self, value):
        self._source.SetCoefficients(value)

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkQuadric()
