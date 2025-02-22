#-----------------------------------
# Imports
#-----------------------------------

# General Imports

# Project Imports
from PyQt6.QtWidgets import QGraphicsSceneMouseEvent

# Project Imports
from ..signalsmodel.abstractconnectionmodel import AbstractConnectionModel
from .abstractlinkmodel import AbstractLinkModel
from .linktype import LinkType

#-----------------------------------
# Class
#-----------------------------------
class TemporaryLinkModel(AbstractLinkModel):
    def __init__(self, signal_creator: AbstractConnectionModel):

        # Get output position
        outputPosition = signal_creator.absolute_connector_center

        super().__init__(outputPosition, outputPosition, LinkType.SQUARE)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.endPoint = event.scenePos()
        return super().mouseMoveEvent(event)
        
