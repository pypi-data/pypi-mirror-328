#-----------------------------------
# Imports
#-----------------------------------

from typing import Iterable, List

from PyQt6.QtGui import QDrag
from PyQt6.QtCore import QMimeData, QPointF, QSizeF, Qt
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsSceneMouseEvent

from muphyn.packages.core.application import DataType

from .abstractconnectionmodel import AbstractConnectionModel
from .signallinkmodel import SignalLinkModel

#-----------------------------------
# Fnctions
#-----------------------------------

def startDrag (signal_creator : AbstractConnectionModel, event: QGraphicsSceneMouseEvent) -> bool :
    mimeData : QMimeData = QMimeData()
    mimeData.setData('action', bytearray('new link'.encode()))
    mimeData.setData('link', bytearray(str(id(signal_creator)).encode()))
    mimeData.setData('type', bytearray(signal_creator.data_type.__str__().encode()))

    drag: QDrag = QDrag(signal_creator)
    drag.setMimeData(mimeData)
    da: Qt.DropAction = drag.exec(Qt.DropAction.LinkAction)
    
#-----------------------------------
# Class
#-----------------------------------

class SignalNodeModel (AbstractConnectionModel) :
    """Est le modèle des noeuds permettant de diviser les liens en plusieurs segments."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, size : QSizeF, links : Iterable[SignalLinkModel] = [],
                  text : str = '', is_infinite : bool = False, parent : QGraphicsItem = None) :

        AbstractConnectionModel.__init__(self, name, data_type, position, size, links, text, is_infinite, parent=parent)
        
    # -------------
    # Properties
    # -------------

    @property 
    def is_input (self) -> bool :
        """Permet de savoir si l'élément est une entrée."""
        return False

    @property
    def is_connected_to_input (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""

        if self.is_input :
            return True
        
        is_connected = False

        lst_already_passed : List[AbstractConnectionModel] = [self]
        lst_to_pass : List[AbstractConnectionModel] = [] 

        for link in self._links :

            if not(link.node_1 in lst_already_passed) :
                if not(link.node_1 in lst_to_pass) :
                    lst_to_pass.append(link.node_1)
            
            if not(link.node_2 in lst_already_passed) :
                if not(link.node_2 in lst_to_pass) :
                    lst_to_pass.append(link.node_2)

        while lst_to_pass.__len__() > 0 :
            
            connectionModel : AbstractConnectionModel = lst_to_pass[0]
            
            if connectionModel.is_input :
                return True
            
            for link in connectionModel._links :

                if not(link.node_1 in lst_already_passed) :
                    if not(link.node_1 in lst_to_pass) :
                        lst_to_pass.append(link.node_1)
                
                if not(link.node_2 in lst_already_passed) :
                    if not(link.node_2 in lst_to_pass) :
                        lst_to_pass.append(link.node_2)

            lst_to_pass.remove(connectionModel)
            lst_already_passed.append(connectionModel)
        
        return is_connected

    # -------------
    # Methods
    # -------------
    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None :

        if (event.button() == Qt.MouseButton.LeftButton and event.modifiers() == Qt.KeyboardModifier.ControlModifier) :
            startDrag(self, event)
            event.accept() 

        return super().mousePressEvent(event)