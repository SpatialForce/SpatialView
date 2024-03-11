#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonComputationalGeometry import (
    vtkParametricKuen,
)

from SpatialView.node_model_template import (
    withProperty,
    withModel,
)
from SpatialView.parametrics.vtk_parametric_function_model import (
    VtkParametricFunctionModel,
)
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk Parametric Kuen", category="Parametrics")
class VtkParametricKuenModel(VtkParametricFunctionModel):
    @property
    def deltaV0(self):
        return self._source.GetDeltaV0()

    @withProperty(DoubleSpinBox(0, 10, 0.1))
    @deltaV0.setter
    def deltaV0(self, value):
        self._source.SetDeltaV0(value)
        self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricKuen()
