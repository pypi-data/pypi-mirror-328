from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget

class PlainTextLabel(QLabel):
    
    def __init__(self, text: str = "", parent: QWidget = None, flags: Qt.WindowType = Qt.WindowType.Widget):
        super().__init__(text, parent, flags)

        # Word wrap
        self.setWordWrap(True)

class PropertyLabel(QLabel):
    pass

class TitlePropertyLabel(QLabel):
    pass