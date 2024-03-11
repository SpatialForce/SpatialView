#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkPolyPlane

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk SDF Poly Plane", category="SDF/geometries")
class VtkPolyPlaneModel(NodeModelTemplate):
    @property
    def polyLine(self):
        return self._source.GetPolyLine()

    @polyLine.setter
    def polyLine(self, value):
        self._source.SetPolyLine(value)

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkPolyPlane()
