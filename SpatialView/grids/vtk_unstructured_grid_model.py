#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid, vtkQuad

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID


@withModel(capStr="Vtk Unstructured Grid", category="Grids")
class VtkUnstructuredGridModel(NodeModelTemplate):
    @withPort(0, sNode.PortType.Out, TypeID.DataObject)
    @property
    def obj(self):
        return self._source

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        aCell = vtkQuad()
        pcoords = aCell.GetParametricCoords()
        for i in range(0, aCell.GetNumberOfPoints()):
            aCell.GetPointIds().SetId(i, i)
            aCell.GetPoints().SetPoint(
                i, (pcoords[3 * i]), (pcoords[3 * i + 1]), (pcoords[3 * i + 2])
            )

        ug = vtkUnstructuredGrid()
        ug.SetPoints(aCell.GetPoints())
        ug.InsertNextCell(aCell.GetCellType(), aCell.GetPointIds())
        self._source = ug
