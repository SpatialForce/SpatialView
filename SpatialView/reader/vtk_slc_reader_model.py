#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkIOImage import vtkSLCReader

from SpatialView.node_model_template import (
    NodeModelTemplate,
    withModel,
    withPort,
    withProperty,
)
from SpatialView.ui import FileDialog
from SpatialView.vtk_algo_data import VtkAlgoData


@withModel(capStr="Vtk SLC Reader", category="Reader")
class VtkSLCReaderModel(NodeModelTemplate):
    @property
    def fileName(self):
        return self._reader.GetFileName()

    @withProperty(FileDialog("*.slc"))
    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self._reader.Update()
        self.dataUpdated.emit(0)

    @withPort(0, sNode.PortType.Out, VtkAlgoData)
    @property
    def outPort(self):
        return self._reader.GetOutputPort()

    def __init__(self):
        super().__init__()

        # Create source
        self._reader = vtkSLCReader()
