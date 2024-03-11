#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonComputationalGeometry import (
    vtkParametricFunction,
)

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import SpinBox


class VtkParametricFunctionModel(NodeModelTemplate):
    @property
    def joinUMax(self):
        return self._source.GetJoinUMaxValue()

    @property
    def joinUMin(self):
        return self._source.GetJoinUMinValue()

    @property
    def joinU(self):
        return self._source.GetJoinU()

    @withProperty(SpinBox("joinUMin", "joinUMax"))
    @joinU.setter
    def joinU(self, value):
        self._source.SetJoinU(value)
        self._renderer.interactorRender()

    @property
    def joinVMax(self):
        return self._source.GetJoinVMaxValue()

    @property
    def joinVMin(self):
        return self._source.GetJoinVMinValue()

    @property
    def joinV(self):
        return self._source.GetJoinV()

    @withProperty(SpinBox("joinVMin", "joinVMax"))
    @joinV.setter
    def joinV(self, value):
        self._source.SetJoinV(value)
        self._renderer.interactorRender()

    @property
    def joinWMax(self):
        return self._source.GetJoinWMaxValue()

    @property
    def joinWMin(self):
        return self._source.GetJoinWMinValue()

    @property
    def joinW(self):
        return self._source.GetJoinW()

    @withProperty(SpinBox("joinWMin", "joinWMax"))
    @joinW.setter
    def joinW(self, value):
        self._source.SetJoinW(value)
        self._renderer.interactorRender()

    @property
    def twistUMax(self):
        return self._source.GetTwistUMaxValue()

    @property
    def twistUMin(self):
        return self._source.GetTwistUMinValue()

    @property
    def twistU(self):
        return self._source.GetTwistU()

    @withProperty(SpinBox("twistUMin", "twistUMax"))
    @twistU.setter
    def twistU(self, value):
        self._source.SetTwistU(value)
        self._renderer.interactorRender()

    @property
    def twistVMax(self):
        return self._source.GetTwistVMaxValue()

    @property
    def twistVMin(self):
        return self._source.GetTwistVMinValue()

    @property
    def twistV(self):
        return self._source.GetTwistV()

    @withProperty(SpinBox("twistVMin", "twistVMax"))
    @twistV.setter
    def twistV(self, value):
        self._source.SetTwistV(value)
        self._renderer.interactorRender()

    @property
    def twistWMax(self):
        return self._source.GetTwistWMaxValue()

    @property
    def twistWMin(self):
        return self._source.GetTwistWMinValue()

    @property
    def twistW(self):
        return self._source.GetTwistW()

    @withProperty(SpinBox("twistWMin", "twistWMax"))
    @twistW.setter
    def twistW(self, value):
        self._source.SetTwistW(value)
        self._renderer.interactorRender()

    @property
    def clockwiseOrderingMax(self):
        return self._source.GetClockwiseOrderingMaxValue()

    @property
    def clockwiseOrderingMin(self):
        return self._source.GetClockwiseOrderingMinValue()

    @property
    def clockwiseOrdering(self):
        return self._source.GetClockwiseOrdering()

    @withProperty(SpinBox("clockwiseOrderingMin", "clockwiseOrderingMax"))
    @clockwiseOrdering.setter
    def clockwiseOrdering(self, value):
        self._source.SetClockwiseOrdering(value)
        self._renderer.interactorRender()

    @property
    def derivativesAvailableMax(self):
        return self._source.GetDerivativesAvailableMaxValue()

    @property
    def derivativesAvailableMin(self):
        return self._source.GetDerivativesAvailableMinValue()

    @property
    def derivativesAvailable(self):
        return self._source.GetDerivativesAvailable()

    @withProperty(SpinBox("derivativesAvailableMin", "derivativesAvailableMax"))
    @derivativesAvailable.setter
    def derivativesAvailable(self, value):
        self._source.SetDerivativesAvailable(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ParametricFunction)
    @property
    def func(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source: vtkParametricFunction | None = None
