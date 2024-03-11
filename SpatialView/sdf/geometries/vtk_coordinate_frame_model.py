#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkCoordinateFrame

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk SDF Coordinate Frame", category="SDF/geometries")
class VtkCoordinateFrameModel(NodeModelTemplate):
    @property
    def origin(self):
        return self._source.GetOrigin()

    @origin.setter
    def origin(self, value):
        self._source.SetOrigin(value)

    @property
    def xAxis(self):
        return self._source.GetXAxis()

    @xAxis.setter
    def xAxis(self, value):
        self._source.SetXAxis(value)
        self._renderer.interactorRender()

    @property
    def yAxis(self):
        return self._source.GetYAxis()

    @yAxis.setter
    def yAxis(self, value):
        self._source.SetYAxis(value)
        self._renderer.interactorRender()

    @property
    def zAxis(self):
        return self._source.GetZAxis()

    @zAxis.setter
    def zAxis(self, value):
        self._source.SetZAxis(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ImplicitFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkCoordinateFrame()
