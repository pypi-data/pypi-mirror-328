

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel

from muphyn.packages.core.base import LogManager

from ..abstractpropertywidget import AbstractPropertyWidget

class UnknownTypePropertyWidget(AbstractPropertyWidget):

    def __init__(self, type_name: str, parent = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)
        
        # Value
        self._value = False

        # Type Name
        self._type_name = type_name

        # Init VBoxLayout
        layout = QHBoxLayout()

        # Double Spin
        self.label = QLabel(f"Uknown Type : {type_name}")

        # Set Layout
        layout.addWidget(self.label)
        self.setLayout(layout)

    # -------------
    # Properties
    # -------------

    # -------------
    # Methods
    # -------------
    def setValue(self, new_value: str):
        LogManager().error(f"Can't set value of UnknownType : {self._type_name}")