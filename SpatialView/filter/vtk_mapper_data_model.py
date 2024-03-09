#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper

from SpatialView import Renderer
from SpatialView.node_model_template import withModel, withPort, NodeModelTemplate
from SpatialView.node_data.vtk_algo_data import VtkAlgoData
from SpatialView.node_data.vtk_mapper_data import VtkMapperData


@withModel(
    capStr="Vtk Mapper Data",
    category="Operators",
)
class VtkMapperDataModel(NodeModelTemplate):
    @withPort(0, sNode.PortType.Out, VtkMapperData)
    @property
    def outPort(self):
        return self._mapper

    @property
    def inPort(self):
        return self._mapper.GetInputConnection(0, 0)

    @withPort(0, sNode.PortType.In, VtkAlgoData)
    @inPort.setter
    def inPort(self, value):
        if value:
            self._mapper.SetInputConnection(value.algo())
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create a mapper
        self._mapper = vtkPolyDataMapper()
