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
from vtkmodules.vtkIOImage import (
    vtkBMPWriter,
    vtkPNMWriter,
    vtkPostScriptWriter,
    vtkTIFFWriter,
    vtkPNGWriter,
    vtkJPEGWriter,
)
from vtkmodules.vtkRenderingCore import vtkWindowToImageFilter

import SpatialView as sView


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
        self.renWin = vtkWidget.GetRenderWindow()

        # status bar
        statusbar = QtWidgets.QStatusBar()
        self.gridlayout.addWidget(statusbar)

        # action
        action = QtGui.QAction("Reset Cam", self)
        action.triggered.connect(self, renderer.resetCamera)
        toolbar.addAction(action)


class GraphicsView(sNode.GraphicsView):
    def dropEvent(self, event):
        super().dropEvent(event)
        sView.Renderer().interactorRender()


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
        dataFlowGraphModel = sNode.DataFlowGraphModel(sView.modelRegistry)
        self.scene = sNode.DataFlowGraphicsScene(dataFlowGraphModel)
        nodeView = GraphicsView(self.scene)
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

    def _writeImage(self, fileName, rgba=True):
        """
        Write the render window view to an image file.

        Image types supported are:
         BMP, JPEG, PNM, PNG, PostScript, TIFF.
        The default parameters are used for all writers, change as needed.

        :param fileName: The file name, if no extension then PNG is assumed.
        :param rgba: Used to set the buffer type.
        :return:
        """

        import os

        if fileName:
            # Select the writer to use.
            path, ext = os.path.splitext(fileName)
            ext = ext.lower()
            if not ext:
                ext = ".png"
                fileName = fileName + ext
            if ext == ".bmp":
                writer = vtkBMPWriter()
            elif ext == ".jpg":
                writer = vtkJPEGWriter()
            elif ext == ".pnm":
                writer = vtkPNMWriter()
            elif ext == ".ps":
                if rgba:
                    rgba = False
                writer = vtkPostScriptWriter()
            elif ext == ".tiff":
                writer = vtkTIFFWriter()
            else:
                writer = vtkPNGWriter()

            windowto_image_filter = vtkWindowToImageFilter()
            windowto_image_filter.SetInput(self.vtkWindow.renWin)
            windowto_image_filter.SetScale(1)  # image quality
            if rgba:
                windowto_image_filter.SetInputBufferTypeToRGBA()
            else:
                windowto_image_filter.SetInputBufferTypeToRGB()
                # Read from the front buffer.
                windowto_image_filter.ReadFrontBufferOff()
                windowto_image_filter.Update()

            writer.SetFileName(fileName)
            writer.SetInputConnection(windowto_image_filter.GetOutputPort())
            writer.Write()
        else:
            raise RuntimeError("Need a filename.")

    def _createMenu(self):
        menuBar = QtWidgets.QMenuBar()
        self.setMenuBar(menuBar)

        # File
        file_menu = menuBar.addMenu("&File")

        def sceneLoad():
            self.scene.load()
            self.renderer.interactorRender()

        loadAction = file_menu.addAction("Load Scene")
        loadAction.triggered.connect(sceneLoad)

        saveAction = file_menu.addAction("Save Scene")
        saveAction.triggered.connect(self.scene.save)

        def saveImage():
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
                None,
                "Open Flow Scene",
                QtCore.QDir.homePath(),
                "Files (*)",
            )

            if len(fileName) > 0:
                self._writeImage(fileName)

        saveAction = file_menu.addAction("Save Image")
        saveAction.triggered.connect(saveImage)

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
