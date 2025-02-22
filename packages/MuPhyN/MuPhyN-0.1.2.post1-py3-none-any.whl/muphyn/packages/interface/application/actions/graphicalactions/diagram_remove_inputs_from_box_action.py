#-----------------------------------
# Imports
#-----------------------------------

from typing import List, Dict

from ...models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ...models.signalsmodel.inputconnectionmodel import InputConnectionModel
from .abstract_unique_element_diagram_action import AbstractUniqueElementDiagramAction
import muphyn.packages.interface.application.actions.graphicalactions.parser_decode as parser_decode
import muphyn.packages.interface.application.actions.graphicalactions.parser_encode as parser_encode

#-----------------------------------
# Class
#-----------------------------------

class DiagramRemoveInputsFromBoxAction (AbstractUniqueElementDiagramAction) :
    """Est l'action permettant de supprimer les entrées d'une box."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, box_element : AbstractBoxModel, input_group_name: str, inputs : list[InputConnectionModel]) :

        AbstractUniqueElementDiagramAction.__init__(self, box_element)

        self._reconstructors : List[Dict] = []
        self._input_group_name: str = input_group_name
        self._inputs: list[InputConnectionModel] = inputs


    # -------------
    # Methods
    # -------------
    def do (self):

        box_model: AbstractBoxModel = self.graphical_element

        if box_model is None : 
            return

        for input_ in self._inputs:
            input_dict : Dict = {"graphical_index": input_.graphical_index}
            current_input : Dict = parser_encode.box_input(input_, input_dict)
            current_input['signals'] = []


            for signal in input_.links:
                current_input['signals'].append(parser_encode.link(signal))
                signal.unbind()
                self.diagram_model.remove_element(signal)

            input_._links.clear()
            
            box_model.remove_input(self._input_group_name, input_)

            self._reconstructors.append(current_input)

 
    def undo (self) :
        
        box_model : AbstractBoxModel = self.graphical_element 

        if box_model is None : 
            return

        self._reconstructors.reverse()
        for input_dict in self._reconstructors :

            # Append Input
            input_ = box_model.append_input(input_dict["name"])

            # Set input parameters
            input_.text = input_dict["text"]
            input_.graphical_index = input_dict["graphical_index"]

            for signal_dict in input_dict['signals'] : 
                parser_decode.link(signal_dict, self.diagram_model)