from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit

from muphyn.packages.core.base import LogManager, GlobalEnvVariablesManager
from muphyn.packages.core.application import DataType
from muphyn.utils.paths import ROOT_DIR

from .abstractpropertywidget import AbstractPropertyWidget

class TypedPropertyLineEdit(AbstractPropertyWidget):

    def __init__(self, parameterToEdit, propertyType: DataType, parent = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)

        # Init Layout
        layout = QHBoxLayout()

        # 
        self._parameterToEdit = parameterToEdit
        self._propertyType: DataType = propertyType

        # Init Line Edit
        self._lineEdit = QLineEdit()
        self._lineEdit.editingFinished.connect(self.line_edit_editing_finished)
        self._lineEditTooltip = QAction(
            QIcon(ROOT_DIR + "/assets/GeneralIcons/error.svg"), 
            ""
        )

        # Set Layout
        layout.addWidget(self._lineEdit)
        self.setLayout(layout)

        # 
        self._isVariable = False
    
    # ------------
    #  Properties
    # ------------
    @property
    def parameterToEdit(self) -> dict:
        return self._parameterToEdit
    
    @property
    def propertyType(self):
        return self._propertyType
    
    # ------------------
    #  Abstract Methods
    # ------------------
    def checkType(self, value: Any):
        raise(NotImplementedError(f"{self.__class__.__name__}.checkType not implemented yet"))
        
    def setTypedValue(self, value: str):
        raise(NotImplementedError(f"{self.__class__.__name__}.setTypedValue not implemented yet"))

    # ---------
    #  Methods
    # ---------
    def setError(self, isError: bool, message: str = None):
        if isError:
            # Test if Tool Tip Icon is in Line Edit
            if not self._lineEditTooltip in self._lineEdit.actions():
                self._lineEdit.addAction(
                    self._lineEditTooltip, 
                    QLineEdit.ActionPosition.TrailingPosition
                )

            # Set Tool Tip message
            if message is not None:
                self._lineEditTooltip.setToolTip(message)
            
        else:
            # Remove tooltip Icon
            if self._lineEditTooltip in self._lineEdit.actions():
                self._lineEdit.removeAction(self._lineEditTooltip)
    
    def setValue(self, newValue: str):
        # Remove leading and ending whitespaces
        newValue = str(newValue).strip()

        # Handle variable name case
        if newValue in GlobalEnvVariablesManager().global_vars:
            # Get global variable
            global_var = GlobalEnvVariablesManager().global_vars[newValue]

            # Set Property Line Edit as variable value
            self._isVariable = True

            if self.checkType(global_var):
                # Set Checked
                self.validValue(newValue)
            else:
                self.setError(True, f"{self._propertyType} object expected: {type(global_var)} instead")
                LogManager().error(TypeError(f"{self._propertyType} object expected: {type(global_var)} instead"))


        # Handle typed value case
        elif self.checkType(newValue):
            self._isVariable = False
            self.setTypedValue(newValue)

        else:
            self._isVariable = False
            self.setError(True, f"Invalid input: Please set a {self._propertyType} value or an existing variable name")
            LogManager().error(TypeError(f"Invalid input: Not a int neither an existing variable name"))

    def validValue(self, newValue: Any):
        # Save value
        self._value = newValue

        # Set Checked
        self._lineEdit.setText(str(newValue))

        # Emit value changed
        self.valueChanged.emit()

        # Reset Error
        self.setError(False)

    # -------
    #  Slots
    # -------
    def line_edit_editing_finished(self):
        self.setValue(self._lineEdit.text())
