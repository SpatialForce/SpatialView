#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

import os
from PySide6 import QtWidgets, QtCore

from SpatialView.ui.abstract_widget_type import AbstractWidgetType


class FileLoadDialog(AbstractWidgetType):
    def __init__(self, ext: str):
        super().__init__()
        self.ext = ext

    def render(self, target):
        def fileLoader():
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Open Flow Scene",
                QtCore.QDir.homePath(),
                f"Files ({self.ext})",
            )

            if not QtCore.QFileInfo.exists(fileName):
                return

            type(target).__setattr__(target, self.property, fileName)

        button = QtWidgets.QPushButton("Open")
        button.setStyleSheet("QPushButton {background-color:#ffffff}")
        button.clicked.connect(fileLoader)
        return button

    def save(self, p, target):
        relative = QtCore.QDir(os.getcwd()).relativeFilePath(
            target.__getattribute__(self.property)
        )
        p[self.property] = relative

    def load(self, p, target):
        fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(p[self.property])
        type(target).__setattr__(target, self.property, fileName)


class FileWriteDialog(AbstractWidgetType):
    def __init__(self, ext: str):
        super().__init__()
        self.ext = ext

    def render(self, target):
        def fileLoader():
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
                None,
                "Open Flow Scene",
                QtCore.QDir.homePath(),
                f"Files (*.{self.ext})",
            )

            if not fileName.endswith(self.ext):
                fileName += f".{self.ext}"

            type(target).__setattr__(target, self.property, fileName)

        button = QtWidgets.QPushButton("Save")
        button.setStyleSheet("QPushButton {background-color:#ffffff}")
        button.clicked.connect(fileLoader)
        return button

    def save(self, p, target):
        relative = QtCore.QDir(os.getcwd()).relativeFilePath(
            target.__getattribute__(self.property)
        )
        p[self.property] = relative

    def load(self, p, target):
        fileName = QtCore.QDir(os.getcwd()).absoluteFilePath(p[self.property])
        type(target).__setattr__(target, self.property, fileName)
