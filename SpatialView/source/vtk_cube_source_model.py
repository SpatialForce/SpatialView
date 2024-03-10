#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkCubeSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, CheckBox, SpinBox


@withModel(capStr="Vtk Cube Source", category="Sources")
class VtkCubeSourceModel(NodeModelTemplate):
    @property
    def xLengthMax(self):
        return self._source.GetXLengthMaxValue()

    @property
    def xLengthMin(self):
        return self._source.GetXLengthMinValue()

    @property
    def xLength(self):
        return self._source.GetXLength()

    @withProperty(DoubleSpinBox("xLengthMin", "xLengthMax", 0.1))
    @xLength.setter
    def xLength(self, value):
        self._source.SetXLength(value)
        self._renderer.interactorRender()

    @property
    def yLengthMax(self):
        return self._source.GetYLengthMaxValue()

    @property
    def yLengthMin(self):
        return self._source.GetYLengthMinValue()

    @property
    def yLength(self):
        return self._source.GetYLength()

    @withProperty(DoubleSpinBox("yLengthMin", "yLengthMax", 0.1))
    @yLength.setter
    def yLength(self, value):
        self._source.SetYLength(value)
        self._renderer.interactorRender()

    @property
    def zLengthMax(self):
        return self._source.GetZLengthMaxValue()

    @property
    def zLengthMin(self):
        return self._source.GetZLengthMinValue()

    @property
    def zLength(self):
        return self._source.GetZLength()

    @withProperty(DoubleSpinBox("zLengthMin", "zLengthMax", 0.1))
    @zLength.setter
    def zLength(self, value):
        self._source.SetZLength(value)
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
        self._source = vtkCubeSource()
