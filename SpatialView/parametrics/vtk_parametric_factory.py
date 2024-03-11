#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from vtkmodules.vtkCommonComputationalGeometry import (
    vtkParametricKuen,
    vtkParametricBohemianDome,
    vtkParametricBour,
    vtkParametricBoy,
    vtkParametricCatalanMinimal,
    vtkParametricConicSpiral,
    vtkParametricCrossCap,
    vtkParametricDini,
    vtkParametricEllipsoid,
    vtkParametricEnneper,
    vtkParametricFigure8Klein,
    vtkParametricHenneberg,
    vtkParametricKlein,
    vtkParametricMobius,
    vtkParametricPluckerConoid,
    vtkParametricPseudosphere,
    vtkParametricRandomHills,
    vtkParametricRoman,
    vtkParametricSpline,
    vtkParametricSuperEllipsoid,
    vtkParametricSuperToroid,
    vtkParametricTorus,
)

from SpatialView.node_model_template import (
    withProperty,
    withModel,
)
from SpatialView.parametrics.vtk_parametric_function_model import (
    VtkParametricFunctionModel,
)
from SpatialView.ui import DoubleSpinBox


@withModel(capStr="Vtk Parametric Bohemian Dome", category="Parametrics")
class VtkParametricBohemianDomeModel(VtkParametricFunctionModel):
    @property
    def a(self):
        return self._source.GetA()

    @withProperty(DoubleSpinBox(0, 10, 0.1))
    @a.setter
    def a(self, value):
        self._source.SetA(value)
        self._renderer.interactorRender()

    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricBohemianDome()


@withModel(capStr="Vtk Parametric Bour", category="Parametrics")
class VtkParametricBourModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricBour()


@withModel(capStr="Vtk Parametric Boy", category="Parametrics")
class VtkParametricBoyModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricBoy()


@withModel(capStr="Vtk Parametric Catalan Minimal", category="Parametrics")
class VtkParametricCatalanMinimalModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricCatalanMinimal()


@withModel(capStr="Vtk Parametric Conic Spiral", category="Parametrics")
class VtkParametricConicSpiralModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricConicSpiral()


@withModel(capStr="Vtk Parametric Cross Cap", category="Parametrics")
class VtkParametricCrossCapModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricCrossCap()


@withModel(capStr="Vtk Parametric Dini", category="Parametrics")
class VtkParametricDiniModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricDini()


@withModel(capStr="Vtk Parametric Ellipsoid", category="Parametrics")
class VtkParametricEllipsoidModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricEllipsoid()


@withModel(capStr="Vtk Parametric Enneper", category="Parametrics")
class VtkParametricEnneperModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricEnneper()


@withModel(capStr="Vtk Parametric Figure8Klein", category="Parametrics")
class VtkParametricFigure8KleinModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricFigure8Klein()


@withModel(capStr="Vtk Parametric Henneberg", category="Parametrics")
class VtkParametricHennebergModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricHenneberg()


@withModel(capStr="Vtk Parametric Klein", category="Parametrics")
class VtkParametricKleinModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricKlein()


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


@withModel(capStr="Vtk Parametric Mobius", category="Parametrics")
class VtkParametricMobiusModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricMobius()


@withModel(capStr="Vtk Parametric Plucker Conoid", category="Parametrics")
class VtkParametricPluckerConoidModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricPluckerConoid()


@withModel(capStr="Vtk Parametric Pseudosphere", category="Parametrics")
class VtkParametricPseudosphereModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricPseudosphere()


@withModel(capStr="Vtk Parametric Random Hills", category="Parametrics")
class VtkParametricRandomHillsModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricRandomHills()


@withModel(capStr="Vtk Parametric Roman", category="Parametrics")
class VtkParametricRomanModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricRoman()


@withModel(capStr="Vtk Parametric Spline", category="Parametrics")
class VtkParametricSplineModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricSpline()


@withModel(capStr="Vtk Parametric Super Ellipsoid", category="Parametrics")
class VtkParametricSuperEllipsoidModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricSuperEllipsoid()


@withModel(capStr="Vtk Parametric Super Toroid", category="Parametrics")
class VtkParametricSuperToroidModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricSuperToroid()


@withModel(capStr="Vtk Parametric Torus", category="Parametrics")
class VtkParametricTorusModel(VtkParametricFunctionModel):
    def __init__(self):
        super().__init__()

        # Create source
        self._source = vtkParametricTorus()
