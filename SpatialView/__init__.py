from .vtk_algo_data import VtkAlgoData
from .vtk_display_actor_model import VtkDisplayActorModel

from .filter import *
from .source import *
from .reader import *


def registerAllDataModels():
    ret = sNode.NodeDelegateModelRegistry()
    filter.registerDataModels(ret)
    source.registerDataModels(ret)
    reader.registerDataModels(ret)
    return ret
