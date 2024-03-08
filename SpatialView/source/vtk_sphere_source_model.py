#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkSphereSource

from SpatialView.node_model_template import NodeModelTemplate, withProperty, withPort
from SpatialView.ui import DoubleSpinBox
from SpatialView.ui.spin_box import SpinBox
from SpatialView.vtk_algo_data import VtkAlgoData


class VtkSphereSourceModel(NodeModelTemplate):
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
    def endPhiMax(self):
        return self._source.GetEndPhiMaxValue()

    @property
    def endPhiMin(self):
        return self._source.GetEndPhiMinValue()

    @property
    def endPhi(self):
        return self._source.GetEndPhi()

    @withProperty(DoubleSpinBox("endPhiMin", "endPhiMax", 0.1))
    @endPhi.setter
    def endPhi(self, value):
        self._source.SetEndPhi(value)
        self.dataUpdated.emit(0)

    @property
    def endThetaMax(self):
        return self._source.GetEndThetaMaxValue()

    @property
    def endThetaMin(self):
        return self._source.GetEndThetaMinValue()

    @property
    def endTheta(self):
        return self._source.GetEndTheta()

    @withProperty(DoubleSpinBox("endThetaMin", "endThetaMax", 0.1))
    @endTheta.setter
    def endTheta(self, value):
        self._source.SetEndTheta(value)
        self.dataUpdated.emit(0)

    @property
    def startPhiMax(self):
        return self._source.GetStartPhiMaxValue()

    @property
    def startPhiMin(self):
        return self._source.GetStartPhiMinValue()

    @property
    def startPhi(self):
        return self._source.GetStartPhi()

    @withProperty(DoubleSpinBox("startPhiMin", "startPhiMax", 0.1))
    @startPhi.setter
    def startPhi(self, value):
        self._source.SetStartPhi(value)
        self.dataUpdated.emit(0)

    @property
    def startThetaMax(self):
        return self._source.GetStartThetaMaxValue()

    @property
    def startThetaMin(self):
        return self._source.GetStartThetaMinValue()

    @property
    def startTheta(self):
        return self._source.GetStartTheta()

    @withProperty(DoubleSpinBox("startThetaMin", "startThetaMax", 0.1))
    @startTheta.setter
    def startTheta(self, value):
        self._source.SetStartTheta(value)
        self.dataUpdated.emit(0)

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
        self.dataUpdated.emit(0)

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
        self._source = vtkSphereSource()
        self.center = (0, 0, 0)
        self.radius = 0.5

    @override
    def caption(self):
        return "Vtk Sphere Source"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkSphereSource"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        registry.registerModel(
            VtkSphereSourceModel, VtkSphereSourceModel.name(), "Sources"
        )
