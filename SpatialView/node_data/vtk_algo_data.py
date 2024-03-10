#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from SpatialView.node_data.type_id import TypeID


class VtkAlgoData(sNode.NodeData):
    def __init__(self, algo=None):
        super().__init__()
        self._algo = algo

    @override
    def type(self):
        return sNode.NodeDataType(TypeID.ALGORITHM.value, "Algo")

    def algo(self):
        return self._algo
