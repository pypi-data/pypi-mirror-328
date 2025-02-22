from PyQt6.QtWidgets import QFileDialog

from .abstractpathpropertywidget import AbstractPathPropertyWidget

class ExistingFilePropertyWidget(AbstractPathPropertyWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(QFileDialog.FileMode.ExistingFile, parent)