#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import SpatialNode as sNode
from vtkmodules.vtkFiltersSources import vtkParametricFunctionSource

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import SpinBox


@withModel(capStr="Vtk Parametric Function Source", category="Parametrics")
class VtkParametricFunctionSourceModel(NodeModelTemplate):
    @property
    def uResolutionMax(self):
        return self._source.GetUResolutionMaxValue()

    @property
    def uResolutionMin(self):
        return self._source.GetUResolutionMinValue()

    @property
    def uResolution(self):
        return self._source.GetUResolution()

    @withProperty(SpinBox("uResolutionMin", "uResolutionMax"))
    @uResolution.setter
    def uResolution(self, value):
        self._source.SetUResolution(value)
        self._renderer.interactorRender()

    @property
    def vResolutionMax(self):
        return self._source.GetVResolutionMaxValue()

    @property
    def vResolutionMin(self):
        return self._source.GetVResolutionMinValue()

    @property
    def vResolution(self):
        return self._source.GetVResolution()

    @withProperty(SpinBox("vResolutionMin", "vResolutionMax"))
    @vResolution.setter
    def vResolution(self, value):
        self._source.SetVResolution(value)
        self._renderer.interactorRender()

    @property
    def wResolutionMax(self):
        return self._source.GetWResolutionMaxValue()

    @property
    def wResolutionMin(self):
        return self._source.GetWResolutionMinValue()

    @property
    def wResolution(self):
        return self._source.GetWResolution()

    @withProperty(SpinBox("wResolutionMin", "wResolutionMax"))
    @wResolution.setter
    def wResolution(self, value):
        self._source.SetWResolution(value)
        self._renderer.interactorRender()

    @property
    def scalarModeMax(self):
        return self._source.GetScalarModeMaxValue()

    @property
    def scalarModeMin(self):
        return self._source.GetScalarModeMinValue()

    @property
    def scalarMode(self):
        return self._source.GetScalarMode()

    @withProperty(SpinBox("scalarModeMin", "scalarModeMax"))
    @scalarMode.setter
    def scalarMode(self, value):
        self._source.SetScalarMode(value)
        self._renderer.interactorRender()

    @property
    def generateNormalsMax(self):
        return self._source.GetGenerateNormalsMaxValue()

    @property
    def generateNormalsMin(self):
        return self._source.GetGenerateNormalsMinValue()

    @property
    def generateNormals(self):
        return self._source.GetGenerateNormals()

    @withProperty(SpinBox("generateNormalsMin", "generateNormalsMax"))
    @generateNormals.setter
    def generateNormals(self, value):
        self._source.SetGenerateNormals(value)
        self._renderer.interactorRender()

    @property
    def generateTextureCoordinatesMax(self):
        return self._source.GetGenerateTextureCoordinatesMaxValue()

    @property
    def generateTextureCoordinatesMin(self):
        return self._source.GetGenerateTextureCoordinatesMinValue()

    @property
    def generateTextureCoordinates(self):
        return self._source.GetGenerateTextureCoordinates()

    @withProperty(
        SpinBox("generateTextureCoordinatesMin", "generateTextureCoordinatesMax")
    )
    @generateTextureCoordinates.setter
    def generateTextureCoordinates(self, value):
        self._source.SetGenerateTextureCoordinates(value)
        self._renderer.interactorRender()

    @withPort(0, sNode.PortType.Out, TypeID.ALGORITHM)
    @property
    def geo(self):
        return self._source.GetOutputPort()

    @property
    def func(self):
        return self._source.GetParametricFunction()

    @withPort(0, sNode.PortType.In, TypeID.ParametricFunction)
    @func.setter
    def func(self, value):
        if value:
            self._source.SetParametricFunction(value)
            self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkParametricFunctionSource()
