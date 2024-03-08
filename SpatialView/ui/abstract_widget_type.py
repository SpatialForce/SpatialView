#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import abc


class AbstractWidgetType:
    def __init__(self):
        self.property = None

    @abc.abstractmethod
    def render(self, target): ...

    def save(self, p, target):
        p[self.property] = target.__getattribute__(self.property)

    def load(self, p, target):
        type(target).__setattr__(target, self.property, p[self.property])
