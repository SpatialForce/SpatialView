#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import os

import SpatialNode as sNode
from PySide6 import QtCore
from vtkmodules.vtkIOImage import vtkHDRReader
from vtkmodules.vtkRenderingCore import vtkTexture

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withModel,
    withProperty,
    withPort,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import FileLoadDialog


@withModel(capStr="Vtk HDR Reader", category="Reader")
class VtkHDRReaderModel(NodeModelTemplate):
    @property
    def fileName(self):
        return self._reader.GetFileName()

    @withProperty(FileLoadDialog("*.hdr *.pic"))
    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.TEXTURE)
    @property
    def outPort(self):
        return self._texture

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._reader = vtkHDRReader()
        self._texture = vtkTexture()
        self._texture.SetColorModeToDirectScalars()

        # default file
        self.fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(
            "SpatialView/resources/meadow_2_1k.hdr"
        )

        self._texture.SetInputConnection(self._reader.GetOutputPort())
        self._texture.MipmapOn()
        self._texture.InterpolateOn()
