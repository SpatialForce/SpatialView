#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import os

import SpatialNode as sNode
from PySide6 import QtCore
from vtkmodules.vtkIOImage import vtkHDRReader

from SpatialView.node_model_template import (
    NodeModelTemplate,
    withModel,
    withProperty,
    withPort,
)
from SpatialView.ui import FileDialog
from SpatialView.vtk_algo_data import VtkAlgoData


@withModel(capStr="Vtk HDR Reader", category="Reader")
class VtkHDRReaderModel(NodeModelTemplate):
    @property
    def fileName(self):
        return self._reader.GetFileName()

    @withProperty(FileDialog("*.hdr *.pic"))
    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self.dataUpdated.emit(0)

    @withPort(0, sNode.PortType.Out, VtkAlgoData)
    @property
    def outPort(self):
        return self._reader.GetOutputPort()

    def __init__(self):
        super().__init__()

        # Create source
        self._reader = vtkHDRReader()

        # default file
        self.fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(
            "SpatialView/resources/meadow_2_1k.hdr"
        )
