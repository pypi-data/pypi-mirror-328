#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from ...models.signalsmodel.signallinkmodel import SignalLinkModel
from .abstract_diagram_action import AbstractDiagramAction

#-----------------------------------
# Class
#-----------------------------------

class DiagramUnlinkNodesAction (AbstractDiagramAction) :
    """Est le type d'action qui permet de lier des noeuds entre eux."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, link: SignalLinkModel) :

        AbstractDiagramAction.__init__(self, link.diagram_model)

        # Save old IO graphical Index
        self._inputIndex = link.input.graphical_index
        self._outputIndex = link.output.graphical_index
        
        # Get Link Index
        self._linkIndex = link.graphical_index

    # -------------
    # Methods
    # -------------
    def do (self) :
        link : SignalLinkModel = self.diagram_model.get_element_by_graphical_index(self._linkIndex)
        if link is not None:
            # Disconnect signal
            link.unbind()

            # Remove graphical
            self.diagram_model.remove_element(link)

    def undo (self) :
        input_ = self.diagram_model.get_element_by_graphical_index(self._inputIndex)
        output = self.diagram_model.get_element_by_graphical_index(self._outputIndex)

        if input_ is not None and output is not None:

            # Set input_ as connected
            input_.is_connected = True

            link = self.diagram_model.link_nodes(input_, output)

            if self._linkIndex == -1 :
                self._linkIndex = link.graphical_index
            
            else :
                link.graphical_index = self._linkIndex
