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
from PySide6 import QtWidgets, QtGui, QtCore

import SpatialNode as sNode
import SpatialView as sView
from SpatialView.node_model_template import ret


class VtkView(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Viewer")
        self.setGeometry(0, 0, 800, 600)

        renderer = sView.Renderer()
        self.gridlayout = QtWidgets.QGridLayout(self)

        # toolbar
        toolbar = QtWidgets.QToolBar()
        self.gridlayout.addWidget(toolbar)

        # viewer
        vtkWidget = QVTKRenderWindowInteractor(self)
        self.gridlayout.addWidget(vtkWidget)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)

        vtkWidget.GetRenderWindow().AddRenderer(renderer.handle)
        renderer.interactor = vtkWidget.GetRenderWindow().GetInteractor()

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.gridlayout.addWidget(statusbar)

        # action
        action = QtGui.QAction("Reset Cam", self)
        action.triggered.connect(self, renderer.resetCamera)
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
        self.renderer: sView.Renderer = sView.Renderer()
        self.renderer.interactor.Initialize()  # Need this line to actually show the render inside Qt

        centralWidget = QtWidgets.QWidget(self)
        nodeLayout = QtWidgets.QGridLayout(centralWidget)
        dataFlowGraphModel = sNode.DataFlowGraphModel(ret)
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

        def sceneLoad():
            self.scene.load()
            self.renderer.interactorRender()

        loadAction.triggered.connect(sceneLoad)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    nodeWindow = NodeView()
    nodeWindow.show()

    sys.exit(app.exec())
