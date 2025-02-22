from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QMainWindow, QWidget

from muphyn.packages.interface.base.finders import findMainWindow

class TutorialHighlighter:

    @staticmethod
    def highlightItem(item: QWidget):
        # Get main window
        main: QMainWindow = findMainWindow()

        # Get geometry
        boundingRect: QRect = item.geometry()
