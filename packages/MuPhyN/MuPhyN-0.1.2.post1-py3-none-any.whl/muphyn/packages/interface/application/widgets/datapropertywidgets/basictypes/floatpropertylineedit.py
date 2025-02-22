# Python imports
import numpy as np
from typing import Any, Union

# PyQt imports
from PyQt6.QtCore import Qt

# Project imports
from muphyn.packages.core.base import LogManager, Regex
from muphyn.packages.core.application import DataType

from ..typedpropertylineedit import TypedPropertyLineEdit

class FloatPropertyLineEdit(TypedPropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.FLOAT, parent, flags)

        # Get min/max values
        self._minValue = -np.inf
        # self._minValue = -sys.float_info.max
        if "min" in parameterToEdit:
            minValue = parameterToEdit["min"]
            try:
                self._minValue = max(float(minValue), self._minValue)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'min' value not a float: {minValue}")


        self._maxValue = np.inf
        # self._maxValue = sys.float_info.max
        if "max" in parameterToEdit:
            maxValue = parameterToEdit["max"]
            try:
                self._maxValue = min(float(maxValue), self._maxValue)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'max' value not a float: {maxValue}")
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isInteger(value) or Regex.isDotFloat(value)
        else:
            return type(value) == int or type(value) == float

    def setTypedValue(self, value: Union[float, int, str]):
        # Handle from numeric type conversion
        if type(value) == float or type(value) == int:
            # Convert to float
            value = float(value)

        # Handle from string type conversion
        elif type(value) == str:
            if value == "" or value == "+" or value == "-":
                value = 0.0
            elif value == "inf":
                value = np.inf
            else:
                # Handle Comma decimal separator
                if Regex.isCommaFloat(value):
                    value = value.replace(",", ".")

                # Convert to float
                value = float(value)

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