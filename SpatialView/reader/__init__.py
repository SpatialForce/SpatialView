from .vtk_exodusII_reader_model import VtkExodusIIReaderModel
from .vtk_slc_reader_model import VtkSLCReaderModel

import SpatialNode as sNode


def registerDataModels(ret: sNode.NodeDelegateModelRegistry):
    VtkExodusIIReaderModel.register(ret)
    VtkSLCReaderModel.register(ret)
