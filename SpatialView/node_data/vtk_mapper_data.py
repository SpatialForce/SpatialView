#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkMapper

from SpatialView.node_data.type_id import TypeID


class VtkMapperData(sNode.NodeData):
    def __init__(self, mapper: vtkMapper | None = None):
        super().__init__()
        self._mapper = mapper

    @override
    def type(self):
        return sNode.NodeDataType(TypeID.ALGORITHM.value, "Mapper")

    def mapper(self):
        return self._mapper
