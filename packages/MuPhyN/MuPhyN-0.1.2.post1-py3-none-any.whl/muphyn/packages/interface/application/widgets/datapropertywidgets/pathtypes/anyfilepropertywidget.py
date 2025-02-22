
from PyQt6.QtWidgets import QFileDialog

from .abstractpathpropertywidget import AbstractPathPropertyWidget

class AnyFilePropertyWidget(AbstractPathPropertyWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(QFileDialog.FileMode.AnyFile, parent)        
