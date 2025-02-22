#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt6.QtWidgets import QGridLayout, QScrollArea

from muphyn.packages.interface.base import PlainButton, PlainTextLabel

from .abstract_dialog import AbstractDialog

#-----------------------------------
# Class
#-----------------------------------

class ErrorDialog (AbstractDialog) :
    """Est la classe permettant d'afficher une boîte de dialogue capable de modifier les bibliothèques des boxes et des solveurs."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, errorMessage: str, ) :
        AbstractDialog.__init__(self, dialog_holder, 'error', 'Errors')
        
        # Set error message
        self._errorMessage = errorMessage

        self.initUI()

    def initUI(self):
        # Resize Window
        self.setMinimumSize(480, 360)
        self.resize(640, 480)
        
        # Init main layout
        mainLayout = QGridLayout()

        # Init text area
        errorMessageLabel = PlainTextLabel(self._errorMessage)

        # Init close button
        closeButton = PlainButton("Close")
        closeButton.pressed.connect(self.close)

        # init scrollarea
        scrollArea = QScrollArea()
        scrollArea.setWidget(errorMessageLabel)

        # Add widgets to layout
        mainLayout.addWidget(scrollArea, 0, 0, 1, 2)
        mainLayout.addWidget(closeButton, 1, 1)
        mainLayout.setColumnStretch(0, 1)

        # Set main layout
        self.setLayout(mainLayout)