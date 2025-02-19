from PySide6 import QtCore, QtWidgets, QtGui

from ez_manage_tool.app_window import EZMWindow
from ez_manage_tool.util import *

import sys

# Only exists on Windows. set icon for taskbar
try:
    from ctypes import windll  
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

def initUI():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    style = get_path('sources', 'style', 'dark.qss')
    if style:loadStylesheet(app, style)

    window = EZMWindow()
    window.show()

    sys.exit(app.exec())

# # to start
# initUI()