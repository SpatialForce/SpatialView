from .vtk_algo_data import VtkAlgoData
from .vtk_display_actor_model import VtkDisplayActorModel
from .vtk_skybox_model import VtkSkyboxModel

from .filter import *
from .source import *
from .reader import *


def registerAllDataModels():
    filter.registerDataModels()
    reader.registerDataModels()
