
# Python imports
import numpy as np
from typing import Any, Union

# PyQt imports
from PyQt6.QtCore import Qt

# Project imports
from muphyn.packages.core.base import Regex, decodeArray, formatArray
from muphyn.packages.core.application import DataType

from ..typedpropertylineedit import TypedPropertyLineEdit

class NdArrayPropertyLineEdit(TypedPropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, 
            flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        
        super().__init__(parameterToEdit, DataType.NDARRAY, parent, flags)
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isArray(value)
        else:
            return type(value) == np.ndarray

    def setTypedValue(self, value: Union[np.ndarray, str]):
        if type(value) == np.ndarray: 
            self.validValue(formatArray(value))
        elif type(value) == str:
            self.validValue(value)