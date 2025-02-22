#-----------------------------------
# Imports
#-----------------------------------

from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPointF, QSizeF, Qt
from PyQt6.QtWidgets import QGraphicsItem

from muphyn.packages.core.application import DataType

from ...signalsmodel.outputconnectionmodel import OutputConnectionModel
from ...signalsmodel.signallinkmodel import SignalLinkModel
from .abstractboxIOmodel import AbstractBoxIOModel

#-----------------------------------
# Class
#-----------------------------------

class BoxInputModel (AbstractBoxIOModel) :
    """Est la classe des entrées des boxes composite."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF,
                  rotation : float = 0.0, link : SignalLinkModel = None, text : str = '',
                  color: QColor = Qt.GlobalColor.black, parent : QGraphicsItem = None) :

        AbstractBoxIOModel.__init__(self, name, data_type, position, size, rotation, text, parent)
        
        self._outputs.append(OutputConnectionModel('', data_type, QPointF(0, 0), link, None, '', color, self))
