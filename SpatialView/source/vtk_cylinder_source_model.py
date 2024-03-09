#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkCylinderSource

from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.ui import DoubleSpinBox, CheckBox
from SpatialView.ui.spin_box import SpinBox
from SpatialView.node_data.vtk_algo_data import VtkAlgoData


@withModel(capStr="Vtk Cylinder Source", category="Sources")
class VtkCylinderSourceModel(NodeModelTemplate):
    @property
    def radiusMax(self):
        return self._source.GetRadiusMaxValue()

    @property
    def radiusMin(self):
        return self._source.GetRadiusMinValue()

    @property
    def radius(self):
        return self._source.GetRadius()

    @withProperty(DoubleSpinBox("radiusMin", "radiusMax", 0.1))
    @radius.setter
    def radius(self, value):
        self._source.SetRadius(value)
        self.dataUpdated.emit(0)

    @property
    def heightMax(self):
        return self._source.GetHeightMaxValue()

    @property
    def heightMin(self):
        return self._source.GetHeightMinValue()

    @property
    def height(self):
        return self._source.GetHeight()

    @withProperty(DoubleSpinBox("heightMin", "heightMax", 0.1))
    @height.setter
    def height(self, height):
        self._source.SetHeight(height)
        self.dataUpdated.emit(0)

    @property
    def resolutionMax(self):
        return self._source.GetResolutionMaxValue()

    @property
    def resolutionMin(self):
        return self._source.GetResolutionMinValue()

    @property
    def resolution(self):
        return self._source.GetResolution()

    @withProperty(SpinBox("resolutionMin", "resolutionMax"))
    @resolution.setter
    def resolution(self, value):
        self._source.SetResolution(value)
        self.dataUpdated.emit(0)

    @property
    def capping(self):
        return self._source.GetCapping()

    @withProperty(CheckBox())
    @capping.setter
    def capping(self, value):
        self._source.SetCapping(value)
        self.dataUpdated.emit(0)

    @property
    def capsuleCap(self):
        return self._source.GetCapsuleCap()

    @withProperty(CheckBox())
    @capsuleCap.setter
    def capsuleCap(self, value):
        self._source.SetCapsuleCap(value)
        self.dataUpdated.emit(0)

    @property
    def center(self):
        return self._source.GetCenter()

    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self.dataUpdated.emit(0)

    @withPort(0, sNode.PortType.Out, VtkAlgoData)
    @property
    def outPort(self):
        return self._source.GetOutputPort()

    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkCylinderSource()
        self.center = (0, 0, 0)
        self.radius = 0.5
