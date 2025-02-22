from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QHBoxLayout, QLineEdit

from muphyn.packages.interface.base import file_selector_button

from ..abstractpropertywidget import AbstractPropertyWidget

class AbstractPathPropertyWidget(AbstractPropertyWidget):

    def __init__(self, file_mode: QFileDialog.FileMode, parent = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)
        
        # Init VBoxLayout
        layout = QHBoxLayout()

        # Add text field
        self.textfield = QLineEdit()
        self.textfield.editingFinished.connect(self.on_textfield_path_edited)

        # Add button to explore file
        self.select_path_button = file_selector_button(file_mode)
        self.select_path_button.accepted.connect(self.on_path_selector_accepted)

        # Set Layout
        layout.addWidget(self.textfield, 1)
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

    def on_textfield_path_edited(self):
        # change path value
        self.setValue(self.textfield.text())

    def setValue(self, new_value: str):
        self._value = new_value

        # Update LineEdit
        if self.textfield.text() != new_value:
            self.textfield.setText(new_value)

        # Emit path changed
        self.valueChanged.emit()