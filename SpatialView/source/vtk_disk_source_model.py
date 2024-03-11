#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkDiskSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, SpinBox, MultiDoubleLineEdit


@withModel(capStr="Vtk Disk Source", category="Sources")
class VtkDiskSourceModel(NodeModelTemplate):
    @property
    def innerRadiusMax(self):
        return self._source.GetInnerRadiusMaxValue()

    @property
    def innerRadiusMin(self):
        return self._source.GetInnerRadiusMinValue()

    @property
    def innerRadius(self):
        return self._source.GetInnerRadius()

    @withProperty(DoubleSpinBox("innerRadiusMin", "innerRadiusMax", 0.1))
    @innerRadius.setter
    def innerRadius(self, value):
        self._source.SetInnerRadius(value)
        self._renderer.interactorRender()

    @property
    def outerRadiusMax(self):
        return self._source.GetOuterRadiusMaxValue()

    @property
    def outerRadiusMin(self):
        return self._source.GetOuterRadiusMinValue()

    @property
    def outerRadius(self):
        return self._source.GetOuterRadius()

    @withProperty(DoubleSpinBox("outerRadiusMin", "outerRadiusMax", 0.1))
    @outerRadius.setter
    def outerRadius(self, value):
        self._source.SetOuterRadius(value)
        self._renderer.interactorRender()

    @property
    def circumferentialResolutionMax(self):
        return self._source.GetCircumferentialResolutionMaxValue()

    @property
    def circumferentialResolutionMin(self):
        return self._source.GetCircumferentialResolutionMinValue()

    @property
    def circumferentialResolution(self):
        return self._source.GetCircumferentialResolution()

    @withProperty(
        SpinBox("circumferentialResolutionMin", "circumferentialResolutionMax")
    )
    @circumferentialResolution.setter
    def circumferentialResolution(self, value):
        self._source.SetCircumferentialResolution(value)
        self._renderer.interactorRender()

    @property
    def radialResolutionMax(self):
        return self._source.GetRadialResolutionMaxValue()

    @property
    def radialResolutionMin(self):
        return self._source.GetRadialResolutionMinValue()

    @property
    def radialResolution(self):
        return self._source.GetRadialResolution()

    @withProperty(SpinBox("radialResolutionMin", "radialResolutionMax"))
    @radialResolution.setter
    def radialResolution(self, value):
        self._source.SetRadialResolution(value)
        self._renderer.interactorRender()

    @property
    def center(self):
        return self._source.GetCenter()

    @withProperty(MultiDoubleLineEdit())
    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def geo(self):
        return self._source.GetOutputPort()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkDiskSource()
