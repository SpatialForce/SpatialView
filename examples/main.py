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
from vtkmodules.vtkRenderingCore import vtkRenderer
from PySide6 import QtWidgets, QtCore

import SpatialNode as sNode
import SpatialView as sView


class VtkView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setWindowTitle("Vtk Viewer")
        self.setGeometry(0, 0, 800, 600)

        centralWidget = QtWidgets.QWidget(self)
        gridlayout = QtWidgets.QGridLayout(centralWidget)
        vtkWidget = QVTKRenderWindowInteractor(centralWidget)
        gridlayout.addWidget(vtkWidget, 0, 0, 1, 1)
        self.setCentralWidget(centralWidget)

        self.ren = vtkRenderer()
        vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = vtkWidget.GetRenderWindow().GetInteractor()


def registerDataModels(renderer, interactor):
    ret = sNode.NodeDelegateModelRegistry()
    ret.registerModel(sView.VtkSphereSourceModel, "Sources")
    ret.registerModel(sView.VtkCylinderSourceModel, "Sources")
    ret.registerModel(sView.VtkMapperDataModel, "Operators")
    ret.registerModel(
        lambda: sView.VtkDisplayActorModel(renderer, interactor), "Displays"
    )
    return ret


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # vtk
    vtkWindow = VtkView()
    vtkWindow.show()
    vtkWindow.iren.Initialize()  # Need this line to actually show the render inside Qt

    # node
    nodeWindow = QtWidgets.QWidget()
    nodeLayout = QtWidgets.QVBoxLayout(nodeWindow)
    registry = registerDataModels(vtkWindow.ren, vtkWindow.iren)
    dataFlowGraphModel = sNode.DataFlowGraphModel(registry)
    scene = sNode.DataFlowGraphicsScene(dataFlowGraphModel)
    nodeView = sNode.GraphicsView(scene)
    nodeLayout.addWidget(nodeView)
    nodeLayout.setContentsMargins(0, 0, 0, 0)
    nodeLayout.setSpacing(0)
    nodeWindow.setWindowTitle("Node-based flow editor")
    nodeWindow.show()

    # menu
    menuBar = QtWidgets.QMenuBar()
    menu = menuBar.addMenu("File")
    saveAction = menu.addAction("Save Scene")
    saveAction.triggered.connect(scene.save)
    loadAction = menu.addAction("Load Scene")
    loadAction.triggered.connect(scene.load)
    scene.sceneLoaded.connect(nodeView.centerScene)

    vtkWindow.setMenuBar(menuBar)
    nodeLayout.addWidget(menuBar)

    sys.exit(app.exec())
