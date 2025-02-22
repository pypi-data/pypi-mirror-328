#-----------------------------------
# Imports
#-----------------------------------

from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QWidget, QHBoxLayout

from muphyn.packages.interface.base import TitlePropertyLabel

from .abstractpropertieseditor import AbstractPropertiesEditor

#-----------------------------------
# Imports
#-----------------------------------

class TitlePropertiesElement (AbstractPropertiesEditor) :
    """Est la classe qui permet d'afficher un titre dans la liste des propriétées."""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, title : str, parent : QWidget = None) :

        self._title = title

        AbstractPropertiesEditor.__init__(self, None)
        
    # -------------
    # Properties
    # -------------

    @property
    def title (self) -> str :
        """Permet de récuperer le titre affiché."""
        return self._title 

    # -------------
    # Methods
    # -------------

    def init_ui (self) -> None : 
        self._lbl_title: TitlePropertyLabel = TitlePropertyLabel()
        self.layout().addWidget(self._lbl_title)

    def translate_ui (self) -> None :
        self._lbl_title.setText(QCoreApplication.translate(self.objectName(), self.title, None))

    def unload(self) -> None:
        pass

    def create_layout(self) -> None:
        return QHBoxLayout()