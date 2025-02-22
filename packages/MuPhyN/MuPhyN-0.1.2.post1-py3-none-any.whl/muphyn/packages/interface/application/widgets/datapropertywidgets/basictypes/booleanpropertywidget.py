
# Python imports
from typing import Any, Union

# PyQt imports
from PyQt6.QtCore import Qt

# Project imports
from muphyn.packages.core.base import Regex
from muphyn.packages.core.application import DataType

from ..typedpropertylineedit import TypedPropertyLineEdit

class BooleanPropertyLineEdit(TypedPropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.INT, parent, flags)
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isBoolean(value)
        else:
            return type(value) == bool

    def setTypedValue(self, value: Union[bool, str]):
        if type(value) == bool: 
            self.validValue(value)
        elif type(value) == str:
            self.validValue(Regex.isTrueValue(value))