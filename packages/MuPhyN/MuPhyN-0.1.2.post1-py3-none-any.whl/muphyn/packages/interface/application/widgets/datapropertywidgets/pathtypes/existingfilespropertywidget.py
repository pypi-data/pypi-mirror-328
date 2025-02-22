from typing import Iterable
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from muphyn.packages.interface.base import ExistingFilesSelectorButton

from ..abstractpropertywidget import AbstractPropertyWidget

class ExistingFilesPropertyWidget(AbstractPropertyWidget):

    def __init__(self, parent = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)

        # Path
        self._value = ""

        # Init VBoxLayout
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add button to explore file
        self.select_path_button = ExistingFilesSelectorButton()
        self.select_path_button.accepted.connect(self.on_path_selector_accepted)

        # Set Layout
        layout.addWidget(self.select_path_button)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def on_path_selector_accepted(self):
        # Change path value
        self.setValue(self.select_path_button.path)

    def setValue(self, new_value: Iterable[str]):
        self._value = new_value

        # Emit path changed
        self.valueChanged.emit()
