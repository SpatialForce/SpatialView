#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

import SpatialNode as sNode
from vtkmodules.vtkRenderingCore import vtkRenderer, vtkRenderWindowInteractor

from .filter.vtk_texture_data import VtkTextureData
from .vtk_skybox import VtkSkybox


class VtkSkyboxModel(sNode.NodeDelegateModel):
    def __init__(self, renderer: vtkRenderer, interactor: vtkRenderWindowInteractor):
        super().__init__()
        self._actor = VtkSkybox()
        self._interactor = interactor
        self._renderer = renderer
        renderer.AddActor(self._actor.skybox)

    @override
    def caption(self):
        return "Skybox Display"

    @override
    def captionVisible(self):
        return True

    @staticmethod
    @override
    def name():
        return "VtkSkyboxModel"

    @staticmethod
    @override
    def register(registry: sNode.NodeDelegateModelRegistry, *args, **kwargs):
        renderer, interactor = args
        registry.registerModel(
            lambda: VtkSkyboxModel(renderer, interactor),
            VtkSkyboxModel.name(),
            "Displays",
        )

    @override
    def nPorts(self, portType):
        result = 1
        match portType:
            case sNode.PortType.In:
                result = 1
            case sNode.PortType.Out:
                result = 0
        return result

    @override
    def dataType(self, portType, portIndex):
        return VtkTextureData().type()

    @override
    def outData(self, port):
        return None

    @override
    def setInData(self, nodeData, portIndex):
        texture = None
        if isinstance(nodeData, VtkTextureData):
            texture = nodeData.texture()

        self._actor.texture = texture
        if texture is not None:
            self._interactor.ReInitialize()

    @override
    def embeddedWidget(self):
        return None
