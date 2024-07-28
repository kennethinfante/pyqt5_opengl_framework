import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtOpenGL import *

from core.main_window import MainWindow

if __name__ == "__main__":
    # deal with dpi
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)  # enable high dpi scaling
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)  # use high dpi icons

    # added for mac
    fmt = QSurfaceFormat()
    fmt.setVersion(4, 1)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    vp = QOpenGLVersionProfile()
    vp.setVersion(4, 1)
    vp.setProfile(QSurfaceFormat.CoreProfile)

    app = QApplication(sys.argv)

    window = MainWindow(version_profile=vp)
    window.setWindowTitle("Color Picker Demo")
    window.show()

    sys.exit(app.exec_())
