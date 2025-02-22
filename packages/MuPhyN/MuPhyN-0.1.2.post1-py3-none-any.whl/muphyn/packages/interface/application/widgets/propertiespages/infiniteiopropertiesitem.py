#-----------------------------------
# Imports
#-----------------------------------

# PyQt6 imports
from typing import Any, Dict
from PyQt6.QtCore import QCoreApplication 
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QComboBox

# Project imports
from muphyn.packages.interface.base import PropertyLabel

from ...models.signalsmodel.abstractconnectionmodel import AbstractConnectionModel

#-----------------------------------
# Class
#-----------------------------------

class InifiniteIOPropertiesItem (QWidget) :
    """Est l'item qui permet d'afficher des éléments visuels pour modifier une entrée/sortie dans la liste des entrées/sorites infinies."""

    # -------------
    # Constants
    # -------------
    ItemHeight: int = 40

    # -------------
    # Constructors
    # -------------

    def __init__ (self, number : int, connection_model : AbstractConnectionModel, parent : QWidget = None) :

        QWidget.__init__(self, parent)

        # Connection Model
        self._connectionModel = connection_model

        # Number
        self._number = number

        self.init_ui()
        self.translate_ui()

        # Set field text
        self._textLineEdit.setText(connection_model.text)        

        # Connect text change
        self._connectionModel.param_changed.connect(self.onTextChanged)

    # -------------
    # Methods
    # -------------

    @property
    def number (self) -> int :
        """Permet de récuperer le nombre de l'item."""
        return self._number

    @number.setter
    def number (self, newNumber : int) -> None :
        """Permet de modifier le nombre de l'item."""
        if self._number != newNumber:
            self._number = newNumber
            self._labelIndex.setText(f"{self._number} :")

    @property
    def connection_model (self) -> AbstractConnectionModel :
        """Permet de récuperer le modèle de la connexion."""
        return self._connectionModel

    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None :
        """Permet de créer et dessinier l'interface graphique."""

        layout : QHBoxLayout = QHBoxLayout()

        # Label Index
        self._labelIndex : PropertyLabel = PropertyLabel(f"{self._number} :")

        # 
        self._textLineEdit : QLineEdit = QLineEdit()
        self._textLineEdit.editingFinished.connect(self.textFieldEdited)

        # 
        items: Dict[str, AbstractConnectionModel.ConnectionType] = AbstractConnectionModel.ConnectionType.items()
        currentIndex = list(items.values()).index(self._connectionModel.connectionType)
        self._typeComboBox: QComboBox = QComboBox()
        self._typeComboBox.addItems(AbstractConnectionModel.ConnectionType.items())
        self._typeComboBox.setCurrentIndex(currentIndex)
        self._typeComboBox.currentIndexChanged.connect(self.inputTypeChanged)

        # Add widgets to layout
        layout.addWidget(self._labelIndex)
        layout.addWidget(self._textLineEdit, 1)
        layout.addWidget(self._typeComboBox)

        self.setLayout(layout)

    def translate_ui (self) -> None :
        """Permet de traduire les éléments de l'interface graphique."""

        self._textLineEdit.setPlaceholderText(QCoreApplication.translate(self.objectName(), u"Texte", None))

    def inputTypeChanged(self, currentIndex: int):
        newType = AbstractConnectionModel.ConnectionType.items()[self._typeComboBox.currentText()]
        self._connectionModel.setConnectionType(newType)

    def textFieldEdited (self) -> None : 
        """Est la méthode appelée lorsque l'utilisateur termine de modifier le champ d'étition du texte de l'entrée."""
        self._connectionModel.text = self._textLineEdit.text()
        # self._connectionModel.name = self._textLineEdit.text()

    def onTextChanged(self, connection_model: AbstractConnectionModel, param_name: str, old_value: Any, new_value: Any) -> None:
        if param_name == "text":
            self._textLineEdit.setText(new_value)