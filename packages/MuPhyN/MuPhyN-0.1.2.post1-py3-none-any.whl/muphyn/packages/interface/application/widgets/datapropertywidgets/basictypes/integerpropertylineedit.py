# Python imports
import numpy as np
from typing import Any, Union

# PyQt imports
from PyQt6.QtCore import Qt

# Project imports
from muphyn.packages.core.base import LogManager, Regex
from muphyn.packages.core.application import DataType

from ..typedpropertylineedit import TypedPropertyLineEdit

class IntegerPropertyLineEdit(TypedPropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.INT, parent, flags)

        # Get 64 bits integer informations
        int64_info = np.iinfo(np.int64)

        # Calculate min value
        self._minValue = int64_info.min
        if "min" in parameterToEdit:
            min_value = parameterToEdit["min"]
            try:
                self._minValue = max(int(float(min_value)), self._minValue)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'min' value not a integer: {min_value}")

        # Calculate max value
        self._maxValue = int64_info.max
        if "max" in parameterToEdit:
            max_value = parameterToEdit["max"]
            try:
                self._maxValue = min(int(float(max_value)), self._maxValue)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'max' value not a integer: {max_value}")
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isInteger(value) or Regex.isDotFloat(value)
        else:
            return type(value) == int or type(value) == float

    def setTypedValue(self, value: Union[float, int, str]):
        # Handle from numeric type conversion
        if type(value) == float or type(value) == int:
            # Convert to int
            value = int(value)

        # Handle from string type conversion
        elif type(value) == str:
            if value == "" or value == "+" or value == "-":
                self.validValue(0)
            else:
                # Handle Comma decimal separator
                if Regex.isCommaFloat(value):
                    value = value.replace(",", ".")

                # Convert to int
                value = int(float(value))

        # Handle other types
        else:
            raise(AttributeError(f"value attribute has an unsupported type: {type(value)} instead of float or int or str"))

        # Handle limits
        if value > self._maxValue:
            value = self._maxValue
        elif value < self._minValue:
            value = self._value

        # Set valid value
        self.validValue(value)