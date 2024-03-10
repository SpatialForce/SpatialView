#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkArrowSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, SpinBox


@withModel(capStr="Vtk Arrow Source", category="Sources2D")
class VtkArrowSourceModel(NodeModelTemplate):
    @property
    def tipLengthMax(self):
        return self._source.GetTipLengthMaxValue()

    @property
    def tipLengthMin(self):
        return self._source.GetTipLengthMinValue()

    @property
    def tipLength(self):
        return self._source.GetTipLength()

    @withProperty(DoubleSpinBox("tipLengthMin", "tipLengthMax", 0.1))
    @tipLength.setter
    def tipLength(self, value):
        self._source.SetTipLength(value)
        self._renderer.interactorRender()

    @property
    def tipRadiusMax(self):
        return self._source.GetTipRadiusMaxValue()

    @property
    def tipRadiusMin(self):
        return self._source.GetTipRadiusMinValue()

    @property
    def tipRadius(self):
        return self._source.GetTipRadius()

    @withProperty(DoubleSpinBox("tipRadiusMin", "tipRadiusMax", 0.1))
    @tipRadius.setter
    def tipRadius(self, value):
        self._source.SetTipRadius(value)
        self._renderer.interactorRender()

    @property
    def tipResolutionMax(self):
        return self._source.GetTipResolutionMaxValue()

    @property
    def tipResolutionMin(self):
        return self._source.GetTipResolutionMinValue()

    @property
    def tipResolution(self):
        return self._source.GetTipResolution()

    @withProperty(SpinBox("tipResolutionMin", "tipResolutionMiax"))
    @tipResolution.setter
    def tipResolution(self, value):
        self._source.SetTipResolution(value)
        self._renderer.interactorRender()

    @property
    def shaftRadiusMax(self):
        return self._source.GetShaftRadiusMaxValue()

    @property
    def shaftRadiusMin(self):
        return self._source.GetShaftRadiusMinValue()

    @property
    def shaftRadius(self):
        return self._source.GetShaftRadius()

    @withProperty(DoubleSpinBox("shaftRadiusMin", "shaftRadiusMax", 0.1))
    @shaftRadius.setter
    def shaftRadius(self, value):
        self._source.SetShaftRadius(value)
        self._renderer.interactorRender()

    @property
    def shaftResolutionMax(self):
        return self._source.GetShaftResolutionMaxValue()

    @property
    def shaftResolutionMin(self):
        return self._source.GetShaftResolutionMinValue()

    @property
    def shaftResolution(self):
        return self._source.GetShaftResolution()

    @withProperty(SpinBox("shaftResolutionMin", "shaftResolutionMax"))
    @shaftResolution.setter
    def shaftResolution(self, value):
        self._source.SetShaftResolution(value)
        self._renderer.interactorRender()

    @property
    def center(self):
        return self._source.GetCenter()

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
        self._source = vtkArrowSource()
