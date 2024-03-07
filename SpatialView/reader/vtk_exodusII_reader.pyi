#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from SpatialNode import QJsonObject
from vtkmodules.vtkIOExodus import vtkExodusIIReader

from SpatialView.reader.vtk_exodusII_reader_model import VtkExodusIIReaderModel

class VtkExodusIIReader:
    def __init__(self, model: VtkExodusIIReaderModel):
        self._reader: vtkExodusIIReader = None
        self._model: VtkExodusIIReaderModel = None

    @property
    def fileName(self) -> str: ...
    @fileName.setter
    def fileName(self, value: str): ...
    def outputPort(self): ...
    def load(self, p: QJsonObject): ...
    def save(self) -> QJsonObject: ...
    def dialog(self): ...
