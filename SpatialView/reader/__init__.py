from .vtk_exodusII_reader_model import VtkExodusIIReaderModel
from .vtk_slc_reader_model import VtkSLCReaderModel
from .vtk_hdr_reader_model import VtkHDRReaderModel
import SpatialNode as sNode


def registerDataModels(ret: sNode.NodeDelegateModelRegistry):
    VtkExodusIIReaderModel.register(ret)
    VtkSLCReaderModel.register(ret)
    VtkHDRReaderModel.register(ret)
