#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonComputationalGeometry import (
    vtkParametricFunction,
    vtkParametricKuen,
)

from SpatialView import Renderer
from SpatialView.node_model_template import (
    NodeModelTemplate,
    withProperty,
    withPort,
    withModel,
)
from SpatialView.parametrics.vtk_parametric_function_model import (
    VtkParametricFunctionModel,
)
from SpatialView.type_id import TypeID
from SpatialView.ui import DoubleSpinBox, SpinBox


@withModel(capStr="Vtk Parametric Kuen", category="Parametrics")
class VtkParametricKuenModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        self._renderer: Renderer = Renderer()
        # Create source
        self._source = vtkParametricKuen()
