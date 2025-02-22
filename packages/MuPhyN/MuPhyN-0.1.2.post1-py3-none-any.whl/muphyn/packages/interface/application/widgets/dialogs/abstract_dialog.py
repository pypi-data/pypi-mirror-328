#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QHideEvent
from PyQt6.QtWidgets import QDialog, QWidget

from muphyn.utils.appconstants import ApplicationWindowTitle

#-----------------------------------
# Class
#-----------------------------------

class AbstractDialog (QDialog) :
    """Est la classe abstraite commune aux dialogues affichés par dessus la fenêtre principale."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, name : str, title : str, parent: QWidget = None, flags: Qt.WindowType = Qt.WindowType.Dialog) :
        QDialog.__init__(self, parent, flags)

        self.setWindowTitle(f"{ApplicationWindowTitle} - {title}")
        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)

        if not self.objectName():
            self.setObjectName('_dlg_' + name)
        
        self._name : str = name
        self._dialog_holder : Any = dialog_holder
        self._value : Any = None

    # -------------
    # Properties
    # -------------

    @property
    def name (self) -> str:
        """Permet de récuperer le nom de la boîte de dialogue."""
        return self._name

    @property
    def value (self) -> Any:
        """Permet de récuperer la valeur de la boite de dialogue."""
        return self._value

    # -------------
    # Methods
    # -------------

    def hideEvent (self, event: QHideEvent) -> None:
        """Est la méthode appelée lorsque la boite de dialogue est fermée."""
        super().hideEvent(event)

        if not self.isModal():
            self._dialog_holder._dialog_closed(self, None)

    def setWindowTitle(self, a0: str) -> None:
        if a0.startswith(f"{ApplicationWindowTitle} - "):
            return super().setWindowTitle(a0)
        else:
            return super().setWindowTitle(f"{ApplicationWindowTitle} - {a0}")