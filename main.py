#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import sys

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QMainWindow
import SpatialNode as sNode

from SpatialView.vtk_display_actor_model import VtkDisplayActorModel
from SpatialView.vtk_source_data_model import VtkSourceDataModel


class VtkView(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.setObjectName("MainWindow")
        self.resize(603, 553)

        centralWidget = QWidget(self)
        gridlayout = QGridLayout(centralWidget)
        vtkWidget = QVTKRenderWindowInteractor(centralWidget)
        gridlayout.addWidget(vtkWidget, 0, 0, 1, 1)
        self.setCentralWidget(centralWidget)

        self.ren = vtkRenderer()
        vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = vtkWidget.GetRenderWindow().GetInteractor()

        # # Create source
        # source = vtkSphereSource()
        # source.SetCenter(0, 0, 0)
        # source.SetRadius(5.0)
        #
        # # Create a mapper
        # mapper = vtkPolyDataMapper()
        # mapper.SetInputConnection(source.GetOutputPort())
        #
        # # Create an actor
        # actor = vtkActor()
        # actor.SetMapper(mapper)
        #
        # self.ren.AddActor(actor)


def registerDataModels(renderer):
    ret = sNode.NodeDelegateModelRegistry()
    ret.registerModel(VtkSourceDataModel)
    ret.registerModel(lambda: VtkDisplayActorModel(renderer))
    return ret


if __name__ == "__main__":
    app = QApplication(sys.argv)

    vtkWindow = VtkView()
    vtkWindow.show()
    vtkWindow.iren.Initialize()  # Need this line to actually show the render inside Qt

    registry = registerDataModels(vtkWindow.ren)
    dataFlowGraphModel = sNode.DataFlowGraphModel(registry)
    scene = sNode.DataFlowGraphicsScene(dataFlowGraphModel)
    nodeView = sNode.GraphicsView(scene)

    nodeView.setWindowTitle("Node-based flow editor")
    nodeView.resize(800, 600)
    nodeView.show()

    sys.exit(app.exec())
