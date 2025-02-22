import os

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QImageReader
from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget

from .fileselectorbutton import ExistingFileSelectorButton

class IconSelector(QWidget):

    iconPathChanged = pyqtSignal(str)

    def __init__(self, iconPath: str = None, parent: QWidget = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)

        # Set icon path
        self._iconPath = iconPath

        # Init UI
        self.initUI()

        # Set Pixmap
        self.setIconPixmap()

    def initUI(self):
        
        # Init Image Viewer
        self._imageViewer = QLabel()

        # Init File picker
        self._fileSelectorButton = ExistingFileSelectorButton()
        self._fileSelectorButton.accepted.connect(self.fileSelected)

        # Main layout
        mainLayout = QGridLayout()
        mainLayout.addWidget(self._imageViewer, 0, 0)
        mainLayout.addWidget(self._fileSelectorButton, 0, 1)

        # Set layout
        self.setLayout(mainLayout)

    def fileSelected(self):
        self.setIconPath(self._fileSelectorButton.path)

    def setIconPath(self, newIconPath: str):
        if self._iconPath != newIconPath:
            # Update icon path value
            self._iconPath = newIconPath

            # Set icon Pixmap
            self.setIconPixmap()

            # Emit icon path changed
            self.iconPathChanged.emit(self._iconPath)

    def setIconPixmap(self):
        if os.path.exists(self._iconPath) and QImageReader.imageFormat(self._iconPath) in QImageReader.supportedImageFormats():
            # Load pixmap
            iconPixmap = QPixmap(self._iconPath)

            # Set pixmap
            self._imageViewer.setPixmap(iconPixmap)