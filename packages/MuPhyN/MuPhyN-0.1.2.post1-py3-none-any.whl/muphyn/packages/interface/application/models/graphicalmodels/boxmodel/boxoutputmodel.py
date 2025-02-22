#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable

from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPointF, QSizeF, Qt
from PyQt6.QtWidgets import QGraphicsItem

from muphyn.packages.core.application import Data, DataType
from ...signalsmodel.inputconnectionmodel import InputConnectionModel
from ...signalsmodel.signallinkmodel import SignalLinkModel
from .abstractboxIOmodel import AbstractBoxIOModel

#-----------------------------------
# Class
#-----------------------------------

class BoxOutputModel (AbstractBoxIOModel) :
    """Est la classe des sorties des boxes composite."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF,
                 rotation : float = 0.0, links : Iterable[SignalLinkModel] = [], text : str = '',
                 color: QColor = Qt.GlobalColor.black, parent : QGraphicsItem = None) :

        AbstractBoxIOModel.__init__(self, name, data_type, position, size, rotation, text, parent)

        self._inputs.append(InputConnectionModel('', data_type, QPointF(0, 0), '', color, self))
    
    # -------------
    # Properties
    # -------------

    @property
    def default_value (self) -> Data :
        """Permet de récuperer la valeur par défaut du lien."""
        return self._default_value

    @default_value.setter
    def default_value (self, default_value_ : Data) :
        """Permet de modifier la valeur par défaut du lien."""

        if default_value_ is None :
            self._default_value = Data(self.data_type)

        elif not default_value_._data_type == self.data_type :
            self._default_value = Data(self.data_type)
        
        else :
            self._default_value = default_value_