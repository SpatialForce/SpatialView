#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkPlaneSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import MultiDoubleLineEdit, IntLineEdit


@withModel(capStr="Vtk Plane Source", category="Sources")
class VtkPlaneSourceModel(NodeModelTemplate):
    @property
    def xResolution(self):
        return self._source.GetXResolution()

    @withProperty(IntLineEdit())
    @xResolution.setter
    def xResolution(self, value):
        self._source.SetXResolution(value)
        self._renderer.interactorRender()

    @property
    def yResolution(self):
        return self._source.GetYResolution()

    @withProperty(IntLineEdit())
    @yResolution.setter
    def yResolution(self, value):
        self._source.SetYResolution(value)
        self._renderer.interactorRender()

    @property
    def center(self):
        return self._source.GetCenter()

    @withProperty(MultiDoubleLineEdit())
    @center.setter
    def center(self, value):
        self._source.SetCenter(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def geo(self):
        return self._source.GetOutputPort()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkPlaneSource()
