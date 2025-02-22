#-----------------------------------
# Imports
#-----------------------------------

from PyQt6.QtCore import QPointF, QSizeF
from PyQt6.QtWidgets import QGraphicsItem

from muphyn.packages.core.application import DataType

from ...signalsmodel.inputconnectionmodel import InputConnectionModel
from ...signalsmodel.outputconnectionmodel import OutputConnectionModel
from .abstractboxmodel import AbstractBoxModel


#-----------------------------------
# Class
#-----------------------------------

class AbstractBoxIOModel (AbstractBoxModel) :
    """Est la classe des entrées des boxes. Elles peuvent-être drag and drop dans l'interface."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF, rotation : float = 0.0,
                  text : str = '', parent : QGraphicsItem = None) :
        
        AbstractBoxModel.__init__(self, name, position, size, rotation, text, parent)

        self._data_type : DataType = data_type
    
    # -------------
    # Properties
    # -------------

    @property
    def data_type (self) -> DataType :
        """Permet de récuperer le type de lien."""
        return self._data_type

    @data_type.setter
    def data_type (self, data_type_ : DataType) -> None :
        """Permet de modifier le type du lien."""
        self._data_type = data_type_

    # -------------
    # Properties
    # -------------

    def insert_input (self, index : int, input : InputConnectionModel) -> None :
        """Permet d'insérer une entrée dans la box."""
        ...

    def remove_input (self, input : InputConnectionModel) -> None :
        """Permet de suppprimer une entrée de la box."""
        ...

    def insert_output (self, index : int, output : OutputConnectionModel) -> None :
        """Permet d'insérer une sortie dans la box."""
        ...

    def remove_output (self, output : OutputConnectionModel) -> None : 
        """Permet de supprimer une sortie de la box."""
        ...