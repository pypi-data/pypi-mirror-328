#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import copy
from typing import Any, Dict

# Project Imports
from ...models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ...models.graphicalmodels.boxmodel.boxinputmodel import BoxInputModel
from ...models.graphicalmodels.boxmodel.boxoutputmodel import BoxOutputModel
from ...models.graphicalmodels.boxmodel.boxmodel import BoxModel
from ...models.linksmodel.abstractlinkmodel import AbstractLinkModel
from ...models.signalsmodel.inputconnectionmodel import InputConnectionGroupModel, InputConnectionModel
from ...models.signalsmodel.outputconnectionmodel import OutputConnectionGroupModel, OutputConnectionModel
from ...models.graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement

#-----------------------------------
# Functions
#-----------------------------------
def link (link : AbstractLinkModel) -> None :
    """Permet de peupler la liste de reconstructeur avec les éléments nécessaire pour reconstruire le lien actuel."""

    reconstructor = {}
    reconstructor["type"] = 'link'

    reconstructor["graphical_index"] = link.graphical_index
    reconstructor["input_box_index"] = link.input.box_model.graphical_index
    reconstructor["output_box_index"] = link.output.box_model.graphical_index
    reconstructor["input_index"] = link.input.graphical_index
    reconstructor["output_index"] = link.output.graphical_index

    reconstructor["link_type"] = link.link_type
    reconstructor["link_value"] = link.link_value
    reconstructor["link_text"] = link.text

    return copy.deepcopy(reconstructor)

def box (box : BoxModel) -> Dict : 
    """Permet de peupler la liste de reconstructeur avec les éléments nécessaire pour reconstruire une box."""

    # Common box informations
    reconstructor = abstract_box(box)

    # General box informations
    reconstructor["type"] = 'box'
    reconstructor["library"] = box.library

    # Parameters
    reconstructor["params"] = {}
    for param_name in box.get_parameters() :
        reconstructor["params"][param_name] = {}
        reconstructor["params"][param_name]["type"] = box.get_parameter(param_name)["type"]
        reconstructor["params"][param_name]["value"] = box.get_parameter(param_name)["value"]
    
    return copy.deepcopy(reconstructor)

def composite_box_input (input : BoxInputModel) -> Dict :
    """Permet de peupler la liste de reconstructeur avec les éléments nécesaire pour reconstruire une entrée de box composite."""

    reconstructor = abstract_box(input)
    reconstructor["type"] = 'box-composite-input'
    
    return copy.deepcopy(reconstructor)

def composite_box_output (output : BoxOutputModel) -> Dict :
    """Permet de peupler la liste de reconstructeur avec les éléments nécessaire pour reconstruire une sortie de box composite."""

    reconstructor = abstract_box(output)
    reconstructor["type"] = 'box-composite-output'
    
    return copy.deepcopy(reconstructor)

def box_inputs_group(inputs_group: InputConnectionGroupModel, inputs_group_reconstructor : Dict = {}) -> dict:
    # Inputs group informations
    inputs_group_reconstructor["name"] = inputs_group.name
    inputs_group_reconstructor["type"] = inputs_group.data_type
    inputs_group_reconstructor["isInfinite"] = inputs_group.is_infinite

    # Inputs informations
    inputs_group_reconstructor["inputs"] = [box_input(input_) for input_ in inputs_group.inputs]

    return copy.deepcopy(inputs_group_reconstructor)

def box_input (input_ : InputConnectionModel, input_reconstructor : Dict = {}) -> Dict :
    """Permet de créer un dictionnaire contenant les données d'une entrée de box."""
    input_reconstructor["graphical_index"] = input_.graphical_index
    input_reconstructor["name"] = input_.name
    input_reconstructor["type"] = input_.data_type
    input_reconstructor["isInfinite"] = input_.is_infinite
    input_reconstructor["text"] = input_.text
    # input_reconstructor["index"] = input_.parent().index_of_input(input_)

    return copy.deepcopy(input_reconstructor)

def box_outputs_group(outputs_group: OutputConnectionGroupModel, outputs_group_reconstructor : Dict = {}) -> dict:
    # Outputs group informations
    outputs_group_reconstructor["name"] = outputs_group.name
    outputs_group_reconstructor["type"] = outputs_group.data_type
    outputs_group_reconstructor["isInfinite"] = outputs_group.is_infinite

    # Outputs informations
    outputs_group_reconstructor["outputs"] = [box_output(output_) for output_ in outputs_group.outputs]

    return copy.deepcopy(outputs_group_reconstructor)

def box_output (output : OutputConnectionModel, output_reconstructor : Dict = {}) -> Dict :
    """Permet de créer un dictionnaire contenant les données d'une soirte de box."""
    
    output_reconstructor["graphical_index"] = output.graphical_index
    output_reconstructor["name"] = output.name
    output_reconstructor["type"] = output.data_type
    output_reconstructor["isInfinite"] = output.is_infinite
    output_reconstructor["text"] = output.text
    # output_reconstructor["index"] = output.parent().index_of_output(output)

    return copy.deepcopy(output_reconstructor)

def abstract_box (abstract_box : AbstractBoxModel) -> Dict :
    """Permet de peupler un reconstructeur avec les éléments d'une box abstraite."""

    reconstructor = abstract_graphical_element(abstract_box)

    # Inputs
    reconstructor["inputs_groups"] = [box_inputs_group(inputs_group) for inputs_group in abstract_box.inputs_groups.values()]

    # Outputs
    reconstructor["outputs_groups"] = [box_outputs_group(outputs_group) for outputs_group in abstract_box.outputs_groups.values()]
    reconstructor["outputs"] = []
    for output in abstract_box.outputs : 
        reconstructor["outputs"].append(box_output(output))

    return copy.deepcopy(reconstructor)

def abstract_graphical_element (abstract_graphical_element : AbstractGraphicalElement) -> Dict :
    """Permet de peupler un reconstructeur avec les éléments d'un graphical element."""

    reconstructor = {}

    reconstructor["graphical_index"] = abstract_graphical_element.graphical_index
    reconstructor["geometry"] = {}
    reconstructor["geometry"]["x"] = abstract_graphical_element.position.x()
    reconstructor["geometry"]["y"] = abstract_graphical_element.position.y()
    reconstructor["geometry"]["width"] = abstract_graphical_element.size.width()
    reconstructor["geometry"]["height"] = abstract_graphical_element.size.height()
    reconstructor["geometry"]["rotation"] = abstract_graphical_element.rot
    reconstructor["name"] = abstract_graphical_element.name
    reconstructor["text"] = abstract_graphical_element.text

    return copy.deepcopy(reconstructor)
    

def encode (element : Any) -> Dict :
    """Permet de sélectionne la bonne méthode à appeler pour peupler le reconstructeur."""

    if isinstance(element, AbstractLinkModel) :
        return link(element)

    elif isinstance(element, BoxModel) :
        return box(element)

    elif isinstance(element, BoxInputModel) :
        return composite_box_input(element)

    elif isinstance(element, BoxOutputModel) :
        return composite_box_output(element)