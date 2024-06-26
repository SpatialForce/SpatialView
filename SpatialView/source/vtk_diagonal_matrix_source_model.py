#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkDiagonalMatrixSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleLineEdit, IntLineEdit


@withModel(capStr="Vtk Diagonal Matrix Source", category="Sources2D")
class VtkDiagonalMatrixSourceModel(NodeModelTemplate):
    @property
    def diagonal(self):
        return self._source.GetDiagonal()

    @withProperty(DoubleLineEdit())
    @diagonal.setter
    def diagonal(self, value):
        self._source.SetDiagonal(value)
        self._renderer.interactorRender()

    @property
    def superDiagonal(self):
        return self._source.GetSuperDiagonal()

    @withProperty(DoubleLineEdit())
    @superDiagonal.setter
    def superDiagonal(self, value):
        self._source.SetSuperDiagonal(value)
        self._renderer.interactorRender()

    @property
    def subDiagonal(self):
        return self._source.GetSubDiagonal()

    @withProperty(DoubleLineEdit())
    @subDiagonal.setter
    def subDiagonal(self, value):
        self._source.SetSubDiagonal(value)
        self._renderer.interactorRender()

    @property
    def extents(self):
        return self._source.GetExtents()

    @withProperty(IntLineEdit())
    @extents.setter
    def extents(self, value):
        self._source.SetExtents(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def geo(self):
        return self._source.GetOutputPort()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkDiagonalMatrixSource()
