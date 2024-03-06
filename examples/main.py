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
from PySide6 import QtWidgets, QtGui

import SpatialNode as sNode
import SpatialView as sView


class VtkView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setWindowTitle("Viewer")
        self.setGeometry(0, 0, 800, 600)

        centralWidget = QtWidgets.QWidget(self)
        gridlayout = QtWidgets.QGridLayout(centralWidget)
        vtkWidget = QVTKRenderWindowInteractor(centralWidget)
        gridlayout.addWidget(vtkWidget)
        gridlayout.setContentsMargins(0, 0, 0, 0)
        gridlayout.setSpacing(0)
        self.setCentralWidget(centralWidget)

        self.ren = vtkRenderer()
        vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = vtkWidget.GetRenderWindow().GetInteractor()

        # toolbar
        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

        # action
        action = QtGui.QAction("Reset Cam", self)

        def reset():
            self.ren.ResetCamera()
            self.iren.ReInitialize()

        action.triggered.connect(self, reset)
        toolbar.addAction(action)


class NodeView(QtWidgets.QMainWindow):
    def __init__(self, registry):
        super().__init__()
        self.setWindowTitle("Node-based flow editor")
        self.setGeometry(400, 300, 800, 600)

        centralWidget = QtWidgets.QWidget(self)
        nodeLayout = QtWidgets.QGridLayout(centralWidget)
        dataFlowGraphModel = sNode.DataFlowGraphModel(registry)
        scene = sNode.DataFlowGraphicsScene(dataFlowGraphModel)
        nodeView = sNode.GraphicsView(scene)
        nodeLayout.addWidget(nodeView)
        nodeLayout.setContentsMargins(0, 0, 0, 0)
        nodeLayout.setSpacing(0)
        self.setCentralWidget(centralWidget)

        # memu bar
        self._menuBar = QtWidgets.QMenuBar()
        menu = self._menuBar.addMenu("File")
        saveAction = menu.addAction("Save Scene")
        saveAction.triggered.connect(scene.save)
        loadAction = menu.addAction("Load Scene")
        loadAction.triggered.connect(scene.load)
        scene.sceneLoaded.connect(nodeView.centerScene)
        self.setMenuBar(self._menuBar)

        # toolbar
        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

    def menuBar(self):
        return self._menuBar


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

    # registry
    registry = registerDataModels(vtkWindow.ren, vtkWindow.iren)

    # node
    nodeWindow = NodeView(registry)
    nodeWindow.show()

    # menu
    vtkWindow.setMenuBar(nodeWindow.menuBar())

    sys.exit(app.exec())
