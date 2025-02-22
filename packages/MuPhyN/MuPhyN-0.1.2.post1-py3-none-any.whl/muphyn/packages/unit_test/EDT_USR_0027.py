
from PyQt6.QtWidgets import QApplication
import sys

from ..interface.mainwindow import MainWindow 

app = QApplication(sys.argv)
win = MainWindow()

win.show()
sys.exit(app.exec_())