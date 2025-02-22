#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from datetime import date
from typing import Dict, Iterable, List, Optional

# Project Imports
from muphyn.utils.appconstants import CurrentVersion
from muphyn.packages.core.application import SchedulerParams, Signal
from ...models.linksmodel.linktype import get_link_type
from ...utils.user import getCurrentUser
from ..graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from ..graphicalmodels.boxmodel.boxmodel import BoxModel
from .abstracteditablemodel import AbstractEditableModel
from .abstractdiagrammodel import AbstractDiagramModel
from .schedulermodel import SchedulerModel

#-----------------------------------
# Class
#-----------------------------------

class SimulationModel (AbstractEditableModel, AbstractDiagramModel) :
    """Est le modèle pour l'éditeur de simulation."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, name : str, path : str, creator : str, date_ : date, version : float, scheduler_model : SchedulerModel, graphical_elements : Iterable[AbstractGraphicalElement] = []) :
        
        AbstractEditableModel.__init__(self, name, path, creator, date_, version)
        AbstractDiagramModel.__init__(self, graphical_elements)
        
        self._scheduler_model : SchedulerModel = scheduler_model

    # -------------
    # Properties
    # -------------

    @property
    def scheduler_model (self) -> SchedulerModel :
        """Permet de récuperer le modèle de planificateur."""
        return self._scheduler_model

    @scheduler_model.setter
    def scheduler_model (self, scheduler_model_ : SchedulerModel) -> None :
        """Permet de modifier le modèle de planificateur."""
        self._scheduler_model = scheduler_model_

    # -------------
    # Methods
    # -------------
    def toDict(self) -> Dict:
        pass

    # ---------------
    # Static methods
    # ---------------

    @staticmethod
    def default(name: str, path: str) -> "SimulationModel":
        # Init default scheduler model
        defaultSchedulerModel = SchedulerModel.default()

        # Get current user
        current_user = getCurrentUser()

        # Build simulation model
        SimulationModel(name, path, current_user, date.today(), CurrentVersion, defaultSchedulerModel)

    @staticmethod
    def fromDict(simulationModelDict: Dict, name: str = "", path: str = "") -> "SimulationModel":
        # General Project informations
        creationDate = simulationModelDict.get("date_creation", date.today())
        creator = simulationModelDict.get("creator", getCurrentUser())
        version = simulationModelDict.get("version", CurrentVersion)

        print("creationDate:", creationDate)
        print("creator:", creator)
        print("version:", version)

        # Scheduler Model
        if "scheduler" in simulationModelDict:            
            schedulerModel = SchedulerModel.fromDict(simulationModelDict["scheduler"])
        else:
            schedulerModel = SchedulerModel.default()

        print("schedulerModel:", schedulerModel)

        # Init simulation model
        simulationModel = SimulationModel(name, path, creator, creationDate, version, schedulerModel)

        # Diagram
        diagramDict: Dict = simulationModelDict.get("diagram", {})

        # Get list of all boxes & signalsDict
        boxes: List[Dict] = diagramDict.get("boxes", [])
        signalsDict: List[Dict] = diagramDict.get("signals", [])
        
        for signal in signalsDict : 
            signal['input'] = None
            signal['output'] = None

        for box_dict in boxes :

            # Get default box data from dict informations
            box_model = BoxModel.fromDict(box_dict)

            # Build infinite inputs groups
            for inputs_group in box_dict["inputs_groups"]:

                # Get group data
                is_infinite = inputs_group["isInfinite"]
                inputs_group_name = inputs_group["name"]

                if is_infinite:
                    # Add inputs
                    for input_data in inputs_group['inputs'] : 
                        # Input data
                        input_signal_index = int(input_data["signal_index"])
                        input_text = input_data["text"]

                        # Append input to box model
                        input_ = box_model.append_input(inputs_group_name)

                        # Set input parameter
                        input_.text = input_text

                        # Set input type
                        if "connectionType" in input_data:
                            input_.setConnectionType(input_data["connectionType"]) 

                        if input_signal_index < len(signalsDict) and input_signal_index >= 0 : 
                            # Get signal data
                            signal_data = signalsDict[input_signal_index]

                            # Add input to signal data
                            if signal_data['input'] is None : 
                                signal_data['input'] = input_

                else:
                    # Set inputs
                    for input_index, input_data in enumerate(inputs_group['inputs']): 
                        # Input data
                        input_signal_index = int(input_data["signal_index"])
                        input_text = input_data["text"]

                        # Get input from box model
                        input_ = box_model.inputs_groups[inputs_group_name].inputs[input_index]

                        # Set input parameter
                        input_.text = input_text

                        # Set input type
                        if "connectionType" in input_data:
                            input_.setConnectionType(input_data["connectionType"]) 

                        if input_signal_index < len(signalsDict) and input_signal_index >= 0 : 
                            # Get signal data
                            signal_data = signalsDict[input_signal_index]

                            # Add input to signal data
                            if signal_data['input'] is None : 
                                signal_data['input'] = input_

            
            # Build infinite outputs groups
            for outputs_group in box_dict["outputs_groups"]:

                # Get group data
                is_infinite = outputs_group["isInfinite"]
                outputs_group_name = outputs_group["name"]

                if is_infinite:
                    # Add outputs
                    for output_data in outputs_group['outputs'] : 
                        # Input data
                        output_signal_indices = output_data["signal_indices"]
                        output_text = output_data["text"]

                        # Append output to box model
                        output_ = box_model.append_output(outputs_group_name)

                        # Set output parameter
                        output_.text = output_text

                        # Set input type
                        if "connectionType" in output_data:
                            output_.setConnectionType(output_data["connectionType"])

                        for output_signal_index in output_signal_indices:

                            if output_signal_index < len(signalsDict) and output_signal_index >= 0 : 
                                # Get signal data
                                signal_data = signalsDict[output_signal_index]

                                # Add output to signal data
                                if signal_data['output'] is None : 
                                    signal_data['output'] = output_

                else:
                    # Set outputs
                    for output_index, output_data in enumerate(outputs_group['outputs']): 
                        # Input data
                        output_signal_indices = output_data["signal_indices"]
                        output_text = output_data["text"]

                        # Get output from box model
                        output_ = box_model.outputs_groups[outputs_group_name].outputs[output_index]

                        # Set output parameter
                        output_.text = output_text

                        # Set input type
                        if "connectionType" in output_data:
                            output_.setConnectionType(output_data["connectionType"])

                        for output_signal_index in output_signal_indices:
                            if output_signal_index >= 0 : 
                                # Get signal data
                                signal_data = signalsDict[output_signal_index]

                                # Add output to signal data
                                if signal_data['output'] is None :
                                    signal_data['output'] = output_

            # Append Box Model
            simulationModel.add_element(box_model)

            
        # Signals
        for signal_data in signalsDict:
            # Get signal data
            input_ = signal_data["input"]
            output = signal_data["output"]
            
            # Create link
            if input_ is not None and output is not None:
                simulationModel.link_nodes(input_, output, -1, -1,
                    float(signal_data['link_value']), get_link_type(signal_data['link_type']), '')

        return simulationModel
