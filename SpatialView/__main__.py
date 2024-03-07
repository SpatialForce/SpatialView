#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import sys
from functools import partial

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import vtkRenderer
from PySide6 import QtWidgets, QtGui, QtCore

import SpatialNode as sNode
import SpatialView as sView


class VtkView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Viewer")
        self.setGeometry(0, 0, 800, 600)

        self.gridlayout = QtWidgets.QGridLayout(self)

        # toolbar
        toolbar = QtWidgets.QToolBar()
        self.gridlayout.addWidget(toolbar)

        # viewer
        vtkWidget = QVTKRenderWindowInteractor(self)
        self.gridlayout.addWidget(vtkWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.ren = vtkRenderer()
        self.ren.SetBackground(vtkNamedColors().GetColor3d("DimGray"))

        vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = vtkWidget.GetRenderWindow().GetInteractor()

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.gridlayout.addWidget(statusbar)

        # action
        action = QtGui.QAction("Reset Cam", self)

        def reset():
            self.ren.ResetCamera()
            self.ren.ResetCameraClippingRange()
            self.iren.ReInitialize()

        action.triggered.connect(self, reset)
        toolbar.addAction(action)


class NodeView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Node-based flow editor")
        self.setGeometry(400, 300, 800, 600)

        # vtk
        self.vtkWindow = VtkView()
        self.vtkWindow.setWindowFlags(
            QtCore.Qt.WindowType.CustomizeWindowHint
            | QtCore.Qt.WindowType.WindowMinMaxButtonsHint
        )
        self.vtkWindow.show()
        self.vtkWindow.iren.Initialize()  # Need this line to actually show the render inside Qt

        # registry
        registry = registerDataModels(self.vtkWindow.ren, self.vtkWindow.iren)

        centralWidget = QtWidgets.QWidget(self)
        nodeLayout = QtWidgets.QGridLayout(centralWidget)
        dataFlowGraphModel = sNode.DataFlowGraphModel(registry)
        self.scene = sNode.DataFlowGraphicsScene(dataFlowGraphModel)
        nodeView = sNode.GraphicsView(self.scene)
        nodeLayout.addWidget(nodeView)
        nodeLayout.setContentsMargins(0, 0, 0, 0)
        nodeLayout.setSpacing(0)
        self.setCentralWidget(centralWidget)
        self.scene.sceneLoaded.connect(nodeView.centerScene)

        # memu bar
        self._createMenu()

        # toolbar
        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)
        toolbar.addActions(nodeView.actions())

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(statusbar)

    def _createMenu(self):
        menuBar = QtWidgets.QMenuBar()
        self.setMenuBar(menuBar)

        # File
        file_menu = menuBar.addMenu("&File")
        saveAction = file_menu.addAction("Save Scene")
        saveAction.triggered.connect(self.scene.save)
        loadAction = file_menu.addAction("Load Scene")
        loadAction.triggered.connect(self.scene.load)

        # Help
        help_menu = menuBar.addMenu("&Help")
        homepage_action = help_menu.addAction("Homepage...")
        homepage_action.triggered.connect(
            partial(
                QtGui.QDesktopServices.openUrl,
                "https://github.com/SpatialForce/SpatialView",
            )
        )
        issues_action = help_menu.addAction("Issues...")
        issues_action.triggered.connect(
            partial(
                QtGui.QDesktopServices.openUrl,
                "https://github.com/SpatialForce/SpatialView/issues",
            )
        )
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self._creatAbout)

    def _creatAbout(self):
        info = """
           SpatialView
        """
        QtWidgets.QMessageBox.about(self, "About SpatialView", info)

    def closeEvent(self, event):
        sys.exit(0)


def registerDataModels(renderer, interactor):
    ret = sView.registerAllDataModels()
    sView.VtkDisplayActorModel.register(ret, renderer, interactor)
    sView.VtkSkyboxModel.register(ret, renderer, interactor)

    return ret


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    nodeWindow = NodeView()
    nodeWindow.show()

    sys.exit(app.exec())
