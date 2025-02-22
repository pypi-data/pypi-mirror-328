#-----------------------------------
# Imports
#-----------------------------------

# general Imports
from typing import Any

# PyQt6 Imports
from PyQt6.QtCore import QPointF, pyqtSlot

# Project Imports
from .linktype import LinkType
from .abstractlinkmodel import AbstractLinkModel

#-----------------------------------
# Class
#-----------------------------------

class LinkModel (AbstractLinkModel) :
    """Est le type générique de lien pour afficher des liens non typés dans l'interface."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, node_model_1 : Any, node_model_2 : Any, link_type : LinkType,
                  text : str = '') :


        # Save Input & Output model
        self._inputModel : Any = node_model_1
        self._outputModel : Any = node_model_2

        # Get absolute position of Input & Output
        input_position : QPointF = self._inputModel.absolute_connector_center
        output_position : QPointF = self._outputModel.absolute_connector_center

        # Init base class
        AbstractLinkModel.__init__(self, output_position, input_position, link_type, text)

        # Connect Input position changed
        self._inputModel.position_changed.connect(self.input_changed)
        self._inputModel.size_changed.connect(self.input_changed)
        self._inputModel.rotation_changed.connect(self.input_changed)

        # Connect Input position changed
        if self._inputModel.box_model is not None :
            self._inputModel.box_model.position_changed.connect(self.input_changed)
            self._inputModel.box_model.size_changed.connect(self.input_changed)
            self._inputModel.box_model.rotation_changed.connect(self.input_changed)

        # Connect Output position changed
        self._outputModel.position_changed.connect(self.output_changed)
        self._outputModel.size_changed.connect(self.output_changed)
        self._outputModel.rotation_changed.connect(self.output_changed)

        # Connect Input position changed
        if self._outputModel.box_model is not None:
            self._outputModel.box_model.position_changed.connect(self.output_changed)
            self._outputModel.box_model.size_changed.connect(self.output_changed)
            self._outputModel.box_model.rotation_changed.connect(self.output_changed)

        self._about_to_erased = False


    # -------------
    # Properties
    # -------------    
    @property
    def input (self) -> Any :
        """Permet de récuperer le noeud d'entrée du lien."""
        return self._inputModel

    @property 
    def output (self) -> Any :
        """Permet de récuperer le noeud de sortie du lien."""
        return self._outputModel

    # -------------
    # Methods
    # -------------
    @pyqtSlot()
    def input_changed (self) :
        """Est la méthode appelée lorsque la poistion du noeud 1 change."""
        self.endPoint = self._inputModel.absolute_connector_center

    @pyqtSlot()
    def output_changed (self) :
        """Est la méthode appelée lorsque la position du noeud 2 change."""
        self.startPoint = self._outputModel.absolute_connector_center

    def unbind (self) -> None :
        """Permet de détruire le lien entre les deux noeuds."""

        if self._about_to_erased :
            return

        if self in self._inputModel._links :
            self._inputModel.remove_link(self)
            self._inputModel.is_connected = False
            self._inputModel.update(self._inputModel.boundingRect())

        if self in self._outputModel._links :
            self._outputModel.remove_link(self)
            self._outputModel.update(self._outputModel.boundingRect())
        
        self._about_to_erased = True

    def to_dict(self) -> dict:
        """Est la méthode appelée pour créer un dictionnaire contenant les données d'un lien entre des entrées/sorties."""

        signal_dict = {}

        signal_dict['value'] = 0.0
        signal_dict['data_type'] = self.data_type.__str__()
        signal_dict['index'] = -1
        signal_dict['link_type'] = self.link_type.__str__()
        signal_dict['link_value'] = self.link_value
        signal_dict['text'] = self.text
    
        return signal_dict

