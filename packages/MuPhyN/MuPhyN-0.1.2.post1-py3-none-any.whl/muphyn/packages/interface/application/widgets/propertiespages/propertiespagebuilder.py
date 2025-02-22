#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Iterable, Any

# PyQt6 Imports
from PyQt6.QtCore import QCoreApplication

# Project Imports
from ...models.graphicalmodels.abstractmoveablegraphicalelement import AbstractMoveableGraphicalElement
from ...models.graphicalmodels.boxmodel.boxmodel import BoxModel
from ...models.graphicalmodels.boxmodel.boxinputmodel import BoxInputModel
from ...models.graphicalmodels.boxmodel.boxoutputmodel import BoxOutputModel
from ...models.signalsmodel.signallinkmodel import SignalLinkModel
from .abstractpropertieseditor import AbstractPropertiesEditor
from .boxproperties import BoxProperties
from .moveablegraphicalelementpropertieseditor import MoveableGraphicalElementPropertiesEditor
from .parameterpropertieseditor import ParameterPropertiesEditor
from .signalpropertieseditor import SignalPropertiesEditor
from .titlepropertieselement import TitlePropertiesElement
from .unknownpropertieseditor import UnknownPropertiesEditor
from .infiniteinputpropertieseditor import InfiniteInputPropertiesEditor
from .infiniteoutputpropertieseditor import InfiniteOutputPropertiesEditor

#-----------------------------------
# Function
#-----------------------------------

def getPropertiesPage (element : Any) -> Iterable[AbstractPropertiesEditor] :
    
    based_editor_loaded = False

    if isinstance(element, SignalLinkModel) : 
        yield SignalPropertiesEditor(element)
        return
    
    if isinstance(element, BoxOutputModel) :
        properties_page = None

    elif isinstance(element, BoxInputModel) : 
        properties_page = None

    elif isinstance(element, BoxModel) :
        box_model : BoxModel = element
        yield BoxProperties(box_model)

        # Inputs
        already_added_name_input = []
        for input_group in box_model.inputs_groups.values(): 
            if input_group.is_infinite and not(input_group.name in already_added_name_input):
                already_added_name_input.append(input_group.name)
                yield InfiniteInputPropertiesEditor(box_model, input_group)

        # Outputs
        already_added_name_output = []
        for output_group in box_model.outputs_groups.values(): 
            if output_group.is_infinite and not(output_group.name in already_added_name_output):
                    already_added_name_output.append(output_group.name)
                    yield InfiniteOutputPropertiesEditor(box_model, output_group)

        if box_model.get_parameters_len() > 0 :
            yield TitlePropertiesElement(QCoreApplication.translate('properties_page_builder', u"Parameters : ", None))
            for parameter in box_model.get_parameters() :
                yield ParameterPropertiesEditor(box_model, parameter)

        based_editor_loaded = True


    if based_editor_loaded == False :
        yield UnknownPropertiesEditor()
        return

    else :

        if isinstance(element, AbstractMoveableGraphicalElement) :
            yield MoveableGraphicalElementPropertiesEditor(element)
            