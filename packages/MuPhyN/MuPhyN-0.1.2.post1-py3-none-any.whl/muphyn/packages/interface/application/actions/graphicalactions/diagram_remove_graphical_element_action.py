#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Iterable, List, Any

# Project Imports
from ...models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ...models.graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from ...models.linksmodel.abstractlinkmodel import AbstractLinkModel
from .abstract_diagram_action import AbstractDiagramAction
import muphyn.packages.interface.application.actions.graphicalactions.parser_decode as parser_decode
import muphyn.packages.interface.application.actions.graphicalactions.parser_encode as parser_encode

#-----------------------------------
# Class
#-----------------------------------

class DiagramRemoveGraphicalElementAction (AbstractDiagramAction) :
    """Est l'action capable de supprimer la sélection actuelle de box."""

    # -------------
    # Methods
    # -------------
    
    def __init__ (self, diagram_model : Any, elements : Iterable[Any]) :

        AbstractDiagramAction.__init__(self, diagram_model)
        
        self._elements_index = []
        for el in elements :
            if isinstance(el, AbstractBoxModel) or isinstance(el, AbstractLinkModel) : 
                self._elements_index.append(el.graphical_index)

        self._reconstructors = []

    # -------------
    # Methods
    # -------------
    
    def elements (self) -> Iterable[AbstractGraphicalElement] :
        """Permet de récuperer les éléments à supprimer directement depuis leur indexs."""

        for index in self._elements_index :

            el = self.diagram_model.get_element_by_graphical_index(index)
            if not(el is None) : 
                yield el

    def do (self) :
        
        to_delete : List[AbstractBoxModel] = []
        for box_model in self.elements() :
            if isinstance(box_model, AbstractBoxModel) :
                to_delete.append(box_model)

        for link in self.elements() :
            if isinstance(link, AbstractLinkModel) : 
                self._reconstructors.append(parser_encode.link(link))
                link.unbind()
                self.diagram_model.remove_element(link)
                
        for box in to_delete :
            signals = list(box.signals)
            for index, link in enumerate(signals):
                self._reconstructors.append(parser_encode.link(link))
                link.unbind()
                self.diagram_model.remove_element(link)
        
        for box in to_delete :
            self._reconstructors.append(parser_encode.encode(box))
            self.diagram_model.remove_element(box)

        self._elements_index.clear()

    def undo (self) :
        
        # Rebuild all items except link
        for reconstructor_box in self._reconstructors :
            if not(reconstructor_box['type'] == 'link') :
                box_model = parser_decode.box(reconstructor_box)
                
                self.diagram_model.add_element(box_model)
                self._elements_index.append(box_model.graphical_index)

                box_model.setSelected(True)
                
        # Rebuild all links
        for reconstructor_link in self._reconstructors :
            if reconstructor_link['type'] == 'link' :

                link_model = parser_decode.link(reconstructor_link, self.diagram_model)
                
                self._elements_index.append(link_model.graphical_index)
                link_model.setSelected(True)

        self._reconstructors.clear()