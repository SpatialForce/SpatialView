#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkArcSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, CheckBox


@withModel(capStr="Vtk Arc Source", category="Sources")
class VtkArcSourceModel(NodeModelTemplate):
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
        self._renderer.interactorRender()

    @property
    def resolutionMax(self):
        return self._source.GetResolutionMaxValue()

    @property
    def resolutionMin(self):
        return self._source.GetResolutionMinValue()

    @property
    def resolution(self):
        return self._source.GetResolution()

    @withProperty(DoubleSpinBox("resolutionMin", "resolutionMax", 0.1))
    @resolution.setter
    def resolution(self, value):
        self._source.SetResolution(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def geo(self):
        return self._source.GetOutputPort()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkArcSource()
