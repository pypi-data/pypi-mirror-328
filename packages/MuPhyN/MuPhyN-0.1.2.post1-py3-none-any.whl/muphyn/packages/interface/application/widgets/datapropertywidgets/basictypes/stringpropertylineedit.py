# Python imports
from typing import Any 

# PyQt imports
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFocusEvent
from PyQt6.QtWidgets import QLineEdit

# Project imports
from muphyn.packages.core.base import LogManager, Regex
from muphyn.packages.core.application import DataType

from ..typedpropertylineedit import TypedPropertyLineEdit

class StringPropertyLineEdit(TypedPropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.STRING, parent, flags)

        # Set limit characters
        self._limitCharacters = -1
        if "maxLength" in parameterToEdit:
            limitCharacters = parameterToEdit["maxLength"]
            try:
                self._limitCharacters = max(int(limitCharacters), self._limitCharacters)
            except:
                LogManager().error(f"StringPropertyWidget.__init__(): given 'maxLength' value not a valid value: {limitCharacters}")
        self._lineEdit.setMaxLength(self._limitCharacters)

        # Active Line Edit focus event
        self._lineEdit.focusInEvent = self.lineEditFocusIn
        self._lineEdit.editingFinished.connect(self.addQuotes)

        # 
        self.addQuotes()

    def addQuotes(self):
        if not self._isVariable:
            # Update max characters length
            if self._limitCharacters > -1:
                self._lineEdit.setMaxLength(self._limitCharacters+2)
                
            # Add quotes from displayed text
            self._lineEdit.setText(f"\"{self.value}\"")
        
    def checkType(self, value: Any):
        return type(value) == str
    
    def removeQuotes(self):
        if not self._isVariable:
            # Remove quotes from displayed text
            self._lineEdit.setText(f"{self.value}")

            # Update max characters length
            if self._limitCharacters > -1:
                self._lineEdit.setMaxLength(self._limitCharacters)

    def setTypedValue(self, value: str):
        if Regex.isStringLiteral(value):
            value = value[1:-1]
        elif type(value) == str:
            pass
        else:
            raise(AttributeError(f"value attribute has an unsupported type: {type(value)} instead of str"))
        
        # 
        self._isQuotedValue = True
        
        # Set valid value
        self.validValue(value)
    
    def lineEditFocusIn(self, focusEvent: QFocusEvent) -> None:
        # Remove quotes
        self.removeQuotes()
        return QLineEdit.focusInEvent(self._lineEdit, focusEvent)