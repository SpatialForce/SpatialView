#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkCapsuleSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, SpinBox, MultiDoubleLineEdit


@withModel(capStr="Vtk Capsule Source", category="Sources")
class VtkCapsuleSourceModel(NodeModelTemplate):
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
        self._renderer.interactorRender()

    @property
    def cylinderLengthMax(self):
        return self._source.GetCylinderLengthMaxValue()

    @property
    def cylinderLengthMin(self):
        return self._source.GetCylinderLengthMinValue()

    @property
    def cylinderLength(self):
        return self._source.GetCylinderLength()

    @withProperty(DoubleSpinBox("cylinderLengthMin", "cylinderLengthMax", 0.1))
    @cylinderLength.setter
    def cylinderLength(self, value):
        self._source.SetCylinderLength(value)
        self._renderer.interactorRender()

    @property
    def thetaResolutionMax(self):
        return self._source.GetThetaResolutionMaxValue()

    @property
    def thetaResolutionMin(self):
        return self._source.GetThetaResolutionMinValue()

    @property
    def thetaResolution(self):
        return self._source.GetThetaResolution()

    @withProperty(SpinBox("thetaResolutionMin", "thetaResolutionMax"))
    @thetaResolution.setter
    def thetaResolution(self, value):
        self._source.SetThetaResolution(value)
        self._renderer.interactorRender()

    @property
    def phiResolutionMax(self):
        return self._source.GetPhiResolutionMaxValue()

    @property
    def phiResolutionMin(self):
        return self._source.GetPhiResolutionMinValue()

    @property
    def phiResolution(self):
        return self._source.GetPhiResolution()

    @withProperty(SpinBox("phiResolutionMin", "phiResolutionMax"))
    @phiResolution.setter
    def phiResolution(self, value):
        self._source.SetPhiResolution(value)
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
        self._source = vtkCapsuleSource()
