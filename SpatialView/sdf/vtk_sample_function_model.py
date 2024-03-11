#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction

from SpatialView import Renderer
from SpatialView.node_model_template import (
    withModel,
    NodeModelTemplate,
    withPort,
    withProperty,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import CheckBox


@withModel(
    capStr="Vtk Sample Function",
    category="SDF",
)
class VtkSampleFunctionModel(NodeModelTemplate):
    @property
    def sampleDimensions(self):
        return self._function.GetSampleDimensions()

    @sampleDimensions.setter
    def sampleDimensions(self, value):
        self._function.SetSampleDimensions(value)

    @property
    def modelBounds(self):
        return self._function.GetModelBounds()

    @modelBounds.setter
    def modelBounds(self, value):
        self._function.SetModelBounds(value)

    @property
    def computeNormals(self):
        return self._function.GetComputeNormals()

    @withProperty(CheckBox())
    @computeNormals.setter
    def computeNormals(self, value):
        self._function.SetComputeNormals(value)

    @property
    def outputScalarType(self):
        return self._function.GetOutputScalarType()

    @outputScalarType.setter
    def outputScalarType(self, value):
        self._function.SetOutputScalarType(value)

    @property
    def capping(self):
        return self._function.GetCapping()

    @capping.setter
    def capping(self, value):
        self._function.SetCapping(value)

    @property
    def capValue(self):
        return self._function.GetCapValue()

    @capValue.setter
    def capValue(self, value):
        self._function.SetCapValue(value)

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def outPort(self):
        return self._function.GetOutputPort(0)

    @property
    def func(self):
        return self._function.GetImplicitFunction()

    @withPort(0, sNode.PortType.In, TypeID.ImplicitFunction)
    @func.setter
    def func(self, value):
        if value:
            self._function.SetImplicitFunction(value)
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create a mapper
        self._function = vtkSampleFunction()
