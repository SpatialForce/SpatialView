#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkFiltersHybrid import vtkImplicitModeller

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, NodeModelTemplate, withPort
from SpatialView.type_id import TypeID


@withModel(
    capStr="Vtk Implicit Modeller",
    category="SDF",
)
class VtkImplicitModellerModel(NodeModelTemplate):
    @property
    def adjustDistanceMax(self):
        return self._mapper.GetAdjustDistanceMaxValue()

    @property
    def adjustDistanceMin(self):
        return self._mapper.GetAdjustDistanceMinValue()

    @property
    def adjustDistance(self):
        return self._mapper.GetAdjustDistance()

    @adjustDistance.setter
    def adjustDistance(self, value):
        self._mapper.SetAdjustDistance(value)

    @property
    def maximumDistanceMax(self):
        return self._mapper.GetMaximumDistanceMaxValue()

    @property
    def maximumDistanceMin(self):
        return self._mapper.GetMaximumDistanceMinValue()

    @property
    def maximumDistance(self):
        return self._mapper.GetMaximumDistance()

    @maximumDistance.setter
    def maximumDistance(self, value):
        self._mapper.SetMaximumDistance(value)

    @property
    def numberOfThreadsMax(self):
        return self._mapper.GetNumberOfThreadsMaxValue()

    @property
    def numberOfThreadsMin(self):
        return self._mapper.GetNumberOfThreadsMinValue()

    @property
    def numberOfThreads(self):
        return self._mapper.GetNumberOfThreads()

    @numberOfThreads.setter
    def numberOfThreads(self, value):
        self._mapper.SetNumberOfThreads(value)

    @property
    def processModeMax(self):
        return self._mapper.GetProcessModeMaxValue()

    @property
    def processModeMin(self):
        return self._mapper.GetProcessModeMinValue()

    @property
    def processMode(self):
        return self._mapper.GetProcessMode()

    @processMode.setter
    def processMode(self, value):
        self._mapper.SetProcessMode(value)

    @property
    def sampleDimensions(self):
        return self._mapper.GetSampleDimensions()

    @sampleDimensions.setter
    def sampleDimensions(self, value):
        self._mapper.SetSampleDimensions(value)

    @property
    def outputScalarType(self):
        return self._mapper.GetOutputScalarType()

    @outputScalarType.setter
    def outputScalarType(self, value):
        self._mapper.SetOutputScalarType(value)

    @property
    def modelBounds(self):
        return self._mapper.GetModelBounds()

    @modelBounds.setter
    def modelBounds(self, value):
        self._mapper.SetModelBounds(value)

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def func(self):
        return self._mapper.GetOutputPort()

    @property
    def inPort(self):
        return self._mapper.GetInputConnection(0, 0)

    @withPort(0, sNode.PortType.In, TypeID.ALGORITHM)
    @inPort.setter
    def inPort(self, value):
        if value:
            self._mapper.SetInputConnection(value)
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create a mapper
        self._mapper = vtkImplicitModeller()
