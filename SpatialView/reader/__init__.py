from .vtk_exodusII_reader_model import VtkExodusIIReaderModel
from .vtk_slc_reader_model import VtkSLCReaderModel
from .vtk_hdr_reader_model import VtkHDRReaderModel

from ..node_model_template import ret


def registerDataModels():
    VtkExodusIIReaderModel.register(ret)
    VtkSLCReaderModel.register(ret)
    VtkHDRReaderModel.register(ret)
