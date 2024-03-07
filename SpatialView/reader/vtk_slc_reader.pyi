#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from SpatialNode import QJsonObject
from vtkmodules.vtkIOImage import vtkSLCReader

from SpatialView.reader.vtk_slc_reader_model import VtkSLCReaderModel

class VtkSLCReader:
    def __init__(self, model: VtkSLCReaderModel):
        self._reader: vtkSLCReader = None
        self._model: VtkSLCReaderModel = None

    @property
    def fileName(self) -> str: ...
    @fileName.setter
    def fileName(self, value: str): ...
    def outputPort(self): ...
    def load(self, p: QJsonObject): ...
    def save(self) -> QJsonObject: ...
    def dialog(self): ...
