#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt6.QtWidgets import QGraphicsItem

from muphyn.packages.core.application import DataType
from ..linksmodel.linkmodel import LinkModel
from ..linksmodel.linktype import LinkType
from .abstractsignalmodel import AbstractSignalModel

#-----------------------------------
# Class
#-----------------------------------

class SignalLinkModel (AbstractSignalModel, LinkModel) :
    """Est le modèle représentant les liens typés entre les boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, data_type : DataType, input : Any, output : Any, link_type : LinkType = LinkType.SQUARE, 
                  text : str = '') :
                  
        AbstractSignalModel.__init__(self, data_type)
        LinkModel.__init__(self, input, output, link_type, text)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        self.b = False
        self.setZValue(0)

    # -------------
    # Properties
    # -------------

    @property
    def is_connected_to_input (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""
        return False