#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from SpatialNode import QJsonObject
from vtkmodules.vtkFiltersSources import vtkSphereSource

from SpatialView.helper import create_setting_panel
import json


class VtkSphereSource:
    def __init__(self, model):
        self._source = vtkSphereSource()
        self._model = model

    @property
    def radius(self):
        return self._source.GetRadius()

    @radius.setter
    def radius(self, value):
        self._source.SetRadius(value)
        self._model.dataUpdated.emit(0)

    @property
    def radiusMax(self):
        return self._source.GetRadiusMaxValue()

    @property
    def radiusMin(self):
        return self._source.GetRadiusMinValue()

    @property
    def endPhi(self):
        return self._source.GetEndPhi()

    @endPhi.setter
    def endPhi(self, value):
        self._source.SetEndPhi(value)
        self._model.dataUpdated.emit(0)

    @property
    def endPhiMax(self):
        return self._source.GetEndPhiMaxValue()

    @property
    def endPhiMin(self):
        return self._source.GetEndPhiMinValue()

    @property
    def endTheta(self):
        return self._source.GetEndTheta()

    @endTheta.setter
    def endTheta(self, value):
        self._source.SetEndTheta(value)
        self._model.dataUpdated.emit(0)

    @property
    def endThetaMax(self):
        return self._source.GetEndThetaMaxValue()

    @property
    def endThetaMin(self):
        return self._source.GetEndThetaMinValue()

    @property
    def startPhi(self):
        return self._source.GetStartPhi()

    @startPhi.setter
    def startPhi(self, value):
        self._source.SetStartPhi(value)
        self._model.dataUpdated.emit(0)

    @property
    def startPhiMax(self):
        return self._source.GetStartPhiMaxValue()

    @property
    def startPhiMin(self):
        return self._source.GetStartPhiMinValue()

    @property
    def startTheta(self):
        return self._source.GetStartTheta()

    @startTheta.setter
    def startTheta(self, value):
        self._source.SetStartTheta(value)
        self._model.dataUpdated.emit(0)

    @property
    def startThetaMax(self):
        return self._source.GetStartThetaMaxValue()

    @property
    def startThetaMin(self):
        return self._source.GetStartThetaMinValue()

    @property
    def phiResolution(self):
        return self._source.GetPhiResolution()

    @phiResolution.setter
    def phiResolution(self, value):
        self._source.SetPhiResolution(value)
        self._model.dataUpdated.emit(0)

    @property
    def phiResolutionMax(self):
        return self._source.GetPhiResolutionMaxValue()

    @property
    def phiResolutionMin(self):
        return self._source.GetPhiResolutionMinValue()

    @property
    def thetaResolution(self):
        return self._source.GetThetaResolution()

    @thetaResolution.setter
    def thetaResolution(self, value):
        self._source.SetThetaResolution(value)
        self._model.dataUpdated.emit(0)

    @property
    def thetaResolutionMax(self):
        return self._source.GetThetaResolutionMaxValue()

    @property
    def thetaResolutionMin(self):
        return self._source.GetThetaResolutionMinValue()

    @property
    def center(self):
        return self._source.GetCenter()

    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self._model.dataUpdated.emit(0)

    def dialog(self):
        return create_setting_panel(self, VtkSphereSource)

    def outputPort(self):
        return self._source.GetOutputPort()

    def load(self, p):
        source = p["source"]
        self.radius = source["radius"]
        self.endPhi = source["endPhi"]
        self.endTheta = source["endTheta"]
        self.startPhi = source["startPhi"]
        self.startTheta = source["startTheta"]
        self.phiResolution = source["phiResolution"]
        self.thetaResolution = source["thetaResolution"]
        self.center = json.loads(source["center"])

    def save(self):
        source = QJsonObject()
        source["radius"] = self.radius
        source["endPhi"] = self.endPhi
        source["endTheta"] = self.endTheta
        source["startPhi"] = self.startPhi
        source["startTheta"] = self.startTheta
        source["phiResolution"] = self.phiResolution
        source["thetaResolution"] = self.thetaResolution
        source["center"] = json.dumps(self.center)
        return source
