#-----------------------------------
# Imports
#-----------------------------------
import os
from typing import Any, Type

from PyQt6.QtWidgets import QPushButton, QComboBox, QGridLayout, QVBoxLayout, QLabel, QLineEdit

from muphyn.packages.core.application import AbstractBoxData, CodeBoxData
from muphyn.packages.interface.base import PlainButton, DirectorySelectorButton

from ...models.editablemodels.boxdatamodel import BoxDataModel
from ...userdata import UserData
from .abstract_dialog import AbstractDialog

#-----------------------------------
# Class
#-----------------------------------

class NewBoxDialog (AbstractDialog) : 
    """Est la classe permettant d'afficher une boîte de dialogue capable de créer une nouvelle box."""

    BoxTypeChoices = {
        "Code": CodeBoxData,
        # "Composite": CompositeBoxData
    }

    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, user_data : UserData) :
        AbstractDialog.__init__(self, dialog_holder, 'new_box', 'New box')

        # Init UI
        self.initUI()
        
    def initUI(self):
        #
        self.resize(360, 120)

        # Box path
        self._pathLabel = QLabel()
        self._pathSelector = DirectorySelectorButton()
        self._pathSelector.accepted.connect(self.pathChanged)

        # Box file name
        self._boxBaseFileNameLineEdit = QLineEdit()

        # Box type combobox
        self._boxTypeComboBox = QComboBox()
        for boxTypeName, boxType in NewBoxDialog.BoxTypeChoices.items():
            self._boxTypeComboBox.addItem(boxTypeName, boxType)

        # Data Layout
        boxDataLayout = QGridLayout()
        boxDataLayout.addWidget(QLabel("Path"), 0, 0)
        boxDataLayout.addWidget(self._pathLabel, 0, 1)
        boxDataLayout.addWidget(self._pathSelector, 0, 2)
        boxDataLayout.addWidget(QLabel("Name"), 1, 0)
        boxDataLayout.addWidget(self._boxBaseFileNameLineEdit, 1, 1, 1, 2)
        boxDataLayout.addWidget(QLabel("Type"), 2, 0)
        boxDataLayout.addWidget(self._boxTypeComboBox, 2, 1, 1, 2)
        boxDataLayout.setColumnStretch(1, 1)
        
        # Confirm button
        self._confirmButton = PlainButton("Confirm")
        self._confirmButton.pressed.connect(self.confirmNewBoxData)

        # Cancel button
        self._cancelButton = QPushButton("Cancel")
        self._cancelButton.pressed.connect(self.cancelNewBoxData)

        # Buttons layout
        buttonsLayout = QGridLayout()
        buttonsLayout.addWidget(self._confirmButton, 0, 1)
        buttonsLayout.addWidget(self._cancelButton, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(boxDataLayout)
        mainLayout.addLayout(buttonsLayout)

        # Set Layout
        self.setLayout(mainLayout)

    def confirmNewBoxData(self):
        # Create default box data object
        currentData: Type[AbstractBoxData] = self._boxTypeComboBox.currentData()
        boxData: AbstractBoxData = currentData.default()

        # Set path
        boxData.path = self._pathSelector.path

        # Box base file name
        boxData.box_name = self._boxBaseFileNameLineEdit.text()

        # Open new diagram editor with box data
        self._value = BoxDataModel(boxData)
        
        # Close dialog
        self.close()

    def cancelNewBoxData(self):
        self.close()
        
    def pathChanged(self):
        self._pathLabel.setText(os.path.basename(self._pathSelector.path))