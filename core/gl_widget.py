import sys

import OpenGL.GL as gl
from OpenGL.GLU import *
# from PySide6 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import *

class GLWidget(QOpenGLWidget):

    def __init__(self, version_profile, main_window, width=640, height=480, *args):
        # same as super(__class__, <first argument>)
        super().__init__(*args)
        self.parent = main_window
        self.version_profile = version_profile
        self.setMinimumSize(width, height)
        # LMB = left mouse button
        # True: fires mouseMoveEvents even when not holding down LMB
        # False: only fire mouseMoveEvents when holding down LMB
        self.setMouseTracking(False)

    def initializeGL(self):
        # not self.gl because there's no need to for it to be an attribute
        gl_context = self.context().versionFunctions(self.version_profile)
        if not gl_context:
            raise RuntimeError("unable to apply OpenGL version profile")

        gl_context.initializeOpenGLFunctions()
        gl.glClearColor(0, 0, 0, 1)
        gl.glClearDepth(1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)

    def resizeGL(self, width, height):
        # glViewport is needed for proper resizing of QGLWidget
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, width, 0, height, -1, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

    def paintGL(self):
        # Renders a triangle... obvious (and deprecated!) stuff
        w, h = self.width(), self.height()
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glBegin(gl.GL_TRIANGLES)
        gl.glColor3f(1, 0, 0)
        gl.glVertex3f(0, 0, 0)
        gl.glColor3f(0, 1, 0)
        gl.glVertex3f(w/2.0, h, 0)
        gl.glColor3f(0, 0, 1)
        gl.glVertex3f(w, 0, 0)
        gl.glEnd()

    def mousePressEvent(self, event):
        x, y = event.x(), event.y()
        w, h = self.width(), self.height()
        # required to call this to force PyQt to read from the correct, updated buffer
        # see issue noted by @BjkOcean in comments!!!
        gl.glReadBuffer(gl.GL_FRONT)
        data = self.grabFrameBuffer()#builtin function that calls glReadPixels internally
        data.save("test.png")
        rgba = QColor(data.pixel(x, y)).getRgb()#gets the appropriate pixel data as an RGBA tuple
        message = "You selected pixel ({0}, {1}) with an RGBA value of {2}.".format(x, y, rgba)
        statusbar = self.parent().statusbar#goes to the parent widget (main window QWidget) and gets its statusbar widget
        statusbar.showMessage(message)

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass
