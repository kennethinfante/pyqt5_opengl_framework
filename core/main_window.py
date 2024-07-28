import sys

from OpenGL.GL import *
from OpenGL.GLU import *

# from PySide6 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QStatusBar, QSizePolicy
from PyQt5.QtOpenGL import *

from .gl_widget import GLWidget


class MainWindow(QWidget):

    def __init__(self, version_profile):
        # same as MainWindow, self
        super().__init__()
        self.glWidget = GLWidget(version_profile, self)
        self.statusbar = QStatusBar()
        self.statusbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.statusbar.showMessage(
            "Click anywhere on the QGLWidget to see a pixel's RGBA value!"
        )
        layout = QVBoxLayout()
        layout.addWidget(self.glWidget)
        layout.addWidget(self.statusbar)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)
