from .vtk_cylinder_source_model import VtkCylinderSourceModel
from .vtk_sphere_source_model import VtkSphereSourceModel

import SpatialNode as sNode


def registerDataModels(ret: sNode.NodeDelegateModelRegistry):
    VtkCylinderSourceModel.register(ret)
    VtkSphereSourceModel.register(ret)
