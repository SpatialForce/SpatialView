#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from SpatialNode import QJsonObject
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from SpatialView.helper import create_setting_panel
import json


class VtkCylinderSource:
    def __init__(self, model):
        self._source = vtkCylinderSource()
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
    def height(self):
        return self._source.GetHeight()

    @height.setter
    def height(self, height):
        self._source.SetHeight(height)
        self._model.dataUpdated.emit(0)

    @property
    def heightMax(self):
        return self._source.GetHeightMaxValue()

    @property
    def heightMin(self):
        return self._source.GetHeightMinValue()

    @property
    def resolution(self):
        return self._source.GetResolution()

    @resolution.setter
    def resolution(self, value):
        self._source.SetResolution(value)
        self._model.dataUpdated.emit(0)

    @property
    def resolutionMax(self):
        return self._source.GetResolutionMaxValue()

    @property
    def resolutionMin(self):
        return self._source.GetResolutionMinValue()

    @property
    def capping(self):
        return self._source.GetCapping()

    @capping.setter
    def capping(self, value):
        self._source.SetCapping(value)
        self._model.dataUpdated.emit(0)

    @property
    def capsuleCap(self):
        return self._source.GetCapsuleCap()

    @capsuleCap.setter
    def capsuleCap(self, value):
        self._source.SetCapsuleCap(value)
        self._model.dataUpdated.emit(0)

    @property
    def center(self):
        return self._source.GetCenter()

    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self._model.dataUpdated.emit(0)

    def dialog(self):
        return create_setting_panel(self, VtkCylinderSource)

    def outputPort(self):
        return self._source.GetOutputPort()

    def load(self, p):
        source = p["source"]
        self.radius = source["radius"]
        self.height = source["height"]
        self.resolution = source["resolution"]
        self.capping = source["capping"]
        self.capsuleCap = source["capsuleCap"]
        self.center = json.loads(source["center"])

    def save(self):
        source = QJsonObject()
        source["radius"] = self.radius
        source["height"] = self.height
        source["resolution"] = self.resolution
        source["capping"] = self.capping
        source["capsuleCap"] = self.capsuleCap
        source["center"] = json.dumps(self.center)
        return source
