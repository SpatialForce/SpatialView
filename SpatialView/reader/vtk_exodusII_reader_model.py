#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkIOExodus import vtkExodusIIReader

from SpatialView import Renderer
from SpatialView.node_model_template import (
    withModel,
    withPort,
    withProperty,
    NodeModelTemplate,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import FileLoadDialog


@withModel(capStr="Vtk ExodusII Reader", category="Reader")
class VtkExodusIIReaderModel(NodeModelTemplate):

    @withProperty(FileLoadDialog("*.e *.exo"))
    @property
    def fileName(self):
        return self._reader.GetFileName()

    @fileName.setter
    def fileName(self, value):
        self._reader.SetFileName(value)
        self._reader.UpdateInformation()
        self._reader.SetTimeStep(10)
        self._reader.SetAllArrayStatus(
            vtkExodusIIReader.NODAL, 1
        )  # enables all NODAL variables
        self._reader.Update()
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def outPort(self):
        return self._reader.GetOutputPort()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._reader = vtkExodusIIReader()
