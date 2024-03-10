#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkIOXML import vtkXMLDataSetWriter

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withModel,
    withPort,
    withProperty,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import FileWriteDialog


@withModel(capStr="Vtk XML Data Set Writer", category="Writer")
class VtkXMLDataSetWriterModel(NodeModelTemplate):
    @property
    def fileName(self):
        return self._writer.GetFileName()

    @withProperty(FileWriteDialog("vtu"))
    @fileName.setter
    def fileName(self, value):
        self._writer.SetFileName(value)
        self._writer.Write()
        self._renderer.interactorRender()

    @property
    def inPort(self):
        return self._writer.GetInputDataObject(0, 0)

    @withPort(0, sNode.PortType.In, TypeID.ALGORITHM)
    @inPort.setter
    def inPort(self, value):
        self._writer.SetInputData(value)

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._writer = vtkXMLDataSetWriter()
