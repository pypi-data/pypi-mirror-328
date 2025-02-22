#-----------------------------------
# Imports
#-----------------------------------
from typing import List, Dict, Any
import copy

from muphyn.packages.core.application import BoxesLibrariesManager, SchedulersLibrariesManager,\
    Box, Diagram, Input, Output, Scheduler, SchedulerParams, Signal, get_data_type
from muphyn.packages.core.base import GlobalEnvVariablesManager, Regex, loadCode

from muphyn.packages.interface.application.models.editablemodels.schedulermodel import SchedulerModel
from muphyn.packages.interface.application.models.editablemodels.simulationmodel import SimulationModel
from muphyn.packages.interface.application.models.graphicalmodels.boxmodel.boxmodel import BoxModel
from muphyn.packages.interface.application.models.signalsmodel.abstractsignalmodel import AbstractSignalModel
from muphyn.packages.interface.application.models.signalsmodel.abstractconnectionmodel import AbstractConnectionModel


#-----------------------------------
# Class
#-----------------------------------

class Parser : 

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...
    
    # -------------
    # Methods
    # -------------      

    def parse (self, element : object) -> Scheduler :
        """Est la méthode pour convertir/traduire un objet en un scheduler prêt à être simuler."""
        
        if isinstance(element, SimulationModel) :
            
            return self.__parse_simulation__(element)

        elif isinstance(element, str) :
            ...

        return None

    def __parse_simulation__ (self, simulation_model : SimulationModel) -> Scheduler :
        """Est la méthode pour convertir/traduire une simulation en un scheduler prêt à être simuler."""

        if simulation_model.scheduler_model is None :
            return None

        else :
            if simulation_model.scheduler_model.params is None :
                return None 

            else :

                scheduler = SchedulersLibrariesManager().construct_scheduler(simulation_model.scheduler_model.library, simulation_model.scheduler_model.name)

                # Si pas de scheduler sélectionné.
                if scheduler is None : 
                    
                    scheduler_library = None 

                    # On prend le premier.
                    for lib in SchedulersLibrariesManager().schedulers :
                        if not(lib is None) :
                            scheduler_library = lib
                            break

                    if scheduler_library is None :
                        return None

                    else :
                        simulation_model.scheduler_model = SchedulerModel(scheduler_library.scheduler_library, scheduler_library.scheduler_name, simulation_model.scheduler_model.params)
                        scheduler = scheduler_library.construct_scheduler()

                scheduler.params = SchedulerParams(simulation_model.scheduler_model.params.stop_time, simulation_model.scheduler_model.params.step_time)
                scheduler.diagram = Diagram()
                
                last_signal_index = 0
                signals_dict : Dict[AbstractSignalModel, Signal] = {} 
                diagrams : List[Diagram] = []

                # Box codes
                boxCodes: Dict[str, Dict[str, Any]] = {}

                for box_model in simulation_model.box :

                    if isinstance(box_model, BoxModel) :

                        params = {}
                        for param in box_model.get_parameters() :
                            params[param] = box_model.get_parameter(param)['value']

                        box = BoxesLibrariesManager().construct_box(box_model.library, box_model.name, **params)
                        box = copy.deepcopy(box)
                        box._graphical_index = box_model._graphical_index
                        scheduler.diagram.append(box)

                        if isinstance(box, Box) :

                            if not box_model.completeLibrary in boxCodes:
                                # Get library element
                                libraryElement = BoxesLibrariesManager().get_box_data(box_model.library, box_model.name)

                                # Load code
                                foo = loadCode(libraryElement.box_library, f"{libraryElement.path}.py")

                                boxCodes[box_model.completeLibrary] = {
                                    "init_method": getattr(foo, libraryElement._init_method) \
                                        if libraryElement._init_method is not None and libraryElement._init_method != "" \
                                            else lambda box, scheduler : ...,
                                    "box_method": getattr(foo, libraryElement._box_function) \
                                        if libraryElement._box_function is not None and libraryElement._box_function != "" \
                                            else lambda box, scheduler : ...,
                                    "end_method": getattr(foo, libraryElement._end_method) \
                                        if libraryElement._end_method is not None and libraryElement._end_method != "" \
                                            else lambda box : ...,
                                }

                            # Init function
                            box._init_method = boxCodes[box_model.completeLibrary]["init_method"]

                            # Simulation function
                            box._function = boxCodes[box_model.completeLibrary]["box_method"]

                            # End function
                            box._end_method = boxCodes[box_model.completeLibrary]["end_method"]

                            # Handle Inputs
                            for input_ in box_model.inputs :

                                # Get connected signal if there is
                                inputLinks = list(input_.links)
                                link = None if len(inputLinks) == 0 else inputLinks[0]

                                # Append input
                                box.append_input(Input(input_.text, link))

                                if link is not None :
                                    link = input_._links[0]

                                    inverted = input_._connectionType == AbstractConnectionModel.ConnectionType.Inverted

                                    if link in signals_dict :
                                        scheduler.diagram.add_box_inputs(box, signals_dict[link])
                                        signals_dict[link].input_name = input_.text
                                        if inverted:
                                            signals_dict[link].inverted = bool(1-signals_dict[link].inverted)

                                    else :
                                        signal : Signal = Signal(
                                            last_signal_index, 
                                            link.data_type, 
                                            link.data_type.default_value(), 
                                            input_name=input_.text,
                                            inverted = inverted
                                        )
                                        scheduler.diagram.append(signal)
                                        signals_dict[link] = signal
                                        scheduler.diagram.add_box_inputs(box, signal)
                                        last_signal_index += 1
                                        
                            # Handle Outputs
                            for output in box_model.outputs :

                                # Init output data
                                outputData = Output(output.text)

                                # Append output data
                                box.append_output(outputData)
                                                                
                                inverted = output._connectionType == AbstractConnectionModel.ConnectionType.Inverted
                                for link in output.links :
                                    
                                    if link in signals_dict :
                                        # Get signal from signal dict
                                        signal = signals_dict[link]

                                        # Append signal to box
                                        outputData.appendSignal(signal)

                                        scheduler.diagram.add_box_outputs(box, signal)
                                        signal.ouput_name = output.text

                                        if inverted:
                                            signal.inverted = bool(1-signal.inverted)

                                    else :
                                        # Create signal
                                        signal : Signal = Signal(
                                            last_signal_index, 
                                            link.data_type, 
                                            link.data_type.default_value(), 
                                            output_name=output.text,
                                            inverted = inverted
                                        )

                                        # Append signal to box
                                        outputData.appendSignal(signal)

                                        # Append signal to diagram
                                        scheduler.diagram.append(signal)

                                        # Add signal to signals dict
                                        signals_dict[link] = signal

                                        # 
                                        scheduler.diagram.add_box_outputs(box, signal)
                                        last_signal_index += 1


                            # Handle Parameters
                            for param in box.params:
                                # Get param value from Box
                                param_value = box.get_parameter(param)
                                if type(param_value) == str:
                                
                                    # Test if scientific notation number
                                    if Regex.isDotScientificFloat(param_value):
                                        # Valid Value
                                        box[param] = float(param_value)

                                    # Test if value exists as global variable
                                    elif str(param_value) in GlobalEnvVariablesManager().global_vars:
                                        # Get global variable value
                                        global_var = GlobalEnvVariablesManager().global_vars[param_value]

                                        # Get parameter type
                                        param_type = get_data_type(box_model.get_parameter(param)["type"])
                                        
                                        # Compare types
                                        if str(param_type) == "float" and str(type(global_var).__name__) in ['float', 'int']:
                                            box[param] = float(global_var)
                                        elif str(param_type) == "int" and str(type(global_var).__name__) in ['float', 'int']:
                                            box[param] = int(global_var)
                                        else:
                                            box[param] = param_type.default_value()


                        elif isinstance(box, Diagram) : 
                            diagrams.append(box)

                return scheduler

                        