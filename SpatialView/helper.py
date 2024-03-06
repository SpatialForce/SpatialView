#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from PySide6 import QtWidgets, QtCore
from functools import partial


def create_setting_panel(self, CLS):
    settings = QtWidgets.QDialog()
    settings.setWindowFlags(
        QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Popup
    )
    settings.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
    settings.setWindowTitle(f"{CLS.__name__} Settings")

    layout_root = QtWidgets.QHBoxLayout(settings)
    layout_root.setContentsMargins(0, 0, 0, 0)
    layout_root.setSpacing(0)

    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    )
    scroll_area.setWidgetResizable(True)
    layout_root.addWidget(scroll_area)

    scroll_area_main_widget = QtWidgets.QWidget()
    scroll_area.setWidget(scroll_area_main_widget)
    scroll_area_main_layout = QtWidgets.QVBoxLayout()
    scroll_area_main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    scroll_area_main_widget.setLayout(scroll_area_main_layout)

    grid_layout = QtWidgets.QGridLayout()
    grid_layout.setSpacing(6)
    scroll_area_main_layout.addLayout(grid_layout)

    row = 0
    for name, obj in vars(CLS).items():
        if isinstance(obj, property):
            if name.endswith("Max") or name.endswith("Min"):
                continue
            if isinstance(self.__getattribute__(name), float):
                label_widget = QtWidgets.QLabel(name)
                label_widget.setMaximumWidth(150)
                label_widget.setTextInteractionFlags(
                    QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
                )
                grid_layout.addWidget(
                    label_widget, row, 0, QtCore.Qt.AlignmentFlag.AlignLeft
                )

                value_widget = QtWidgets.QDoubleSpinBox()
                value_widget.setSingleStep(0.2)
                value_widget.setMaximum(self.__getattribute__(name + "Max"))
                value_widget.setMinimum(self.__getattribute__(name + "Min"))
                value_widget.setValue(self.__getattribute__(name))
                value_widget.valueChanged.connect(partial(CLS.__setattr__, self, name))
                grid_layout.addWidget(
                    value_widget, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft
                )
                row += 1
            if isinstance(self.__getattribute__(name), int):
                label_widget = QtWidgets.QLabel(name)
                label_widget.setMaximumWidth(150)
                label_widget.setTextInteractionFlags(
                    QtCore.Qt.TextInteractionFlag.TextBrowserInteraction
                )
                grid_layout.addWidget(
                    label_widget, row, 0, QtCore.Qt.AlignmentFlag.AlignLeft
                )

                if hasattr(self, name + "Max"):
                    value_widget = QtWidgets.QSpinBox()
                    value_widget.setValue(self.__getattribute__(name))

                    value_widget.setMaximum(self.__getattribute__(name + "Max"))
                    value_widget.setMinimum(self.__getattribute__(name + "Min"))
                    value_widget.valueChanged.connect(
                        partial(CLS.__setattr__, self, name)
                    )
                    grid_layout.addWidget(
                        value_widget, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft
                    )
                else:
                    value_widget = QtWidgets.QCheckBox()
                    value_widget.setChecked(self.__getattribute__(name))
                    value_widget.toggled.connect(partial(CLS.__setattr__, self, name))
                    grid_layout.addWidget(
                        value_widget, row, 1, QtCore.Qt.AlignmentFlag.AlignLeft
                    )
                row += 1

    return settings
