#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import abc
import SpatialNode as sNode


class AbstractWidgetType(abc.ABC):
    @abc.abstractmethod
    def render(self, target): ...

    @abc.abstractmethod
    def save(self, p: sNode.QJsonObject, target): ...

    @abc.abstractmethod
    def load(self, p: sNode.QJsonObject, target): ...
