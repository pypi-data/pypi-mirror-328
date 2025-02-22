#-----------------------------------
# Imports
#-----------------------------------
import numbers
import numpy as np
import sys
from typing import Callable, Iterator, List, Any, Dict, Union


from muphyn.packages.core.base import LogManager

from ..data.plci_core_data import Data
from ..data.plci_core_data_type import DataType
from ..io.plci_core_io import Input, Output
from ..scheduler.plci_core_scheduler_params import SchedulerParams
from ..scheduler.plci_core_scheduler_event import SchedulerEvent
from ..signal.plci_core_signal_event import SignalEvent
from ..signal.plci_core_signal import Signal

#-----------------------------------
# Class
#-----------------------------------

class Box :
    """Est la classe décrivant les boxes."""
    # -------------
    # Constructors
    # -------------

    def __init__ (  self, 
                    index_ : int, 
                    name_ : str,
                    library_ : str,
                    init_method_ : Callable[[Any], None] = None, 
                    function_ : Callable[[Any, SchedulerEvent], List[SignalEvent]] = None, 
                    end_method_ : Callable[[Any], None] = None,
                    inputs: List[Input] = [],
                    outputs: List[Output] = [],
                    wait_for_events_ : bool = True,
                    wait_for_all_signal_events_ : bool = True, 
                    params_ : Dict[str, Any] = None) :
        
        self._index : int = index_
        self._name : str = name_
        self._library : str = library_
        
        if params_ is None :
            self._params : Dict[str, Any] = {}
        else :
            self._params : Dict[str, Any] = params_

        # IO
        self._inputs: List[Input] = inputs
        self._outputs: List[Output] = outputs

        # Init signals 
        self._inputSignals : Dict[Signal, float] = {}
        self._outputSignals : List[Signal] = []

        self._wait_for_events : bool = wait_for_events_
        self._wait_for_all_signal_events : bool = wait_for_all_signal_events_

        self._current_timing : float = 0.0

        if (init_method_ == None) : 
            self._init_method : Callable[[Box], None] = lambda box, scheduler_params : ...
        else :
            self._init_method : Callable[[Box], None] = init_method_

        if (function_ == None) :
            self._function : Callable[[Box, SchedulerEvent], List[SignalEvent]] = lambda box, timing : []
        else :
            self._function : Callable[[Box, SchedulerEvent], List[SignalEvent]] = function_

        if (end_method_ == None) :
            self._end_method : Callable[[Box], None] = lambda box : ...
        else :
            self._end_method : Callable[[Box], None] = end_method_
        
    # -------------
    # Properties
    # -------------

    @property 
    def index (self) -> int :
        """Permet de récuperer l'index de la box."""
        return self._index

    @property
    def name (self) -> str :
        """Permet de récuperer le nom de la box."""
        return self._name

    @property
    def library (self) -> str :
        """Permet de récuperer la bibliothèque dans laquelle se trouve la box."""
        return self._library
    
    @property
    def inputs(self) -> List[Input]:
        return self._inputs
    
    @property
    def inputSignals (self) -> List[Signal] :
        """Permet de récuperer les entrées de la box."""
        return self._inputSignals.keys()
    
    @property
    def inuptNames(self) -> List[str]:
        return [input_.name for input_ in self._inputs]
    
    @property
    def outputs(self) -> List[Output]:
        return self._outputs

    @property
    def outputSignals (self) -> List[Signal] :
        """Permet de récuperer les sorties de la box."""
        return self._outputSignals
    
    @property
    def outputNames(self) -> List[str]:
        return [output.name for output in self._outputs]

    @property
    def params (self) -> Dict[str, Any] :
        """Permet de récuperer les paramètres de le box."""
        return self._params

    @property
    def wait_for_events (self) -> bool :
        """Permet de savoir si la box ne peut être utilisée que lors d'un événement."""
        return self._wait_for_events

    @property
    def wait_for_all_signal_events (self) -> bool :
        """Permet de savoir si la box ne peut être appelée que lorsque toutes ses entrées ont reçues un événement au timing actuel."""
        return self._wait_for_all_signal_events

    @property 
    def events_on_all_inputs (self) -> bool :
        """Permet de savoir si toutes les entrées ont bien reçues un événement au timing actuel."""
        for signal in self._inputSignals.keys() :
            if self._inputSignals[signal] < self.current_timing : 
                return False
        return True

    @property 
    def current_timing (self) -> float :
        """Permet de récuperer le timing de la box."""
        return self._current_timing
    
    @property
    def input_values(self) -> List:
        return [inputSignal.value for inputSignal in self.inputSignals]


    # -------------
    # Methods
    # -------------

    def init (self, scheduler_params: SchedulerParams) -> None :
        """Permet de lancer la méthode d'initialisation de la box."""
        self._init_method(self, scheduler_params)

    def function (self, event_ : SchedulerEvent) -> List[SignalEvent] :
        """Permet de réaliser le traitement de la box et de modifier les éventuels sorties."""

        self._current_timing = event_.timing
        
        # Si on attend que des événements et que ce n'est pas un événement. On s'arrête
        if self.wait_for_events and event_.signal is None:
            return None
            
        # Si c'est bien un événement, on modifie le timing de l'entrée concernée.
        if event_.signal is not None :
            self._inputSignals[event_.signal] = event_.timing
        
        # Si on attend tous les événement et qu'un événement n'est pas encore arrivé. On s'arrête.
        if self.wait_for_all_signal_events :
            if not self.events_on_all_inputs :
                return None

        # Activation de la box.
        returnedData = self._function(self, event_)
        
        # Get data type
        returnedDataType = type(returnedData)

        if returnedData is None:
            return []
        elif returnedDataType == list or returnedDataType == tuple or isinstance(returnedData, np.ndarray):
            boxOutputsNames = self.outputNames

            newEvents = []

            if len(boxOutputsNames) == len(returnedData):

                for index, outputName in enumerate(boxOutputsNames):
                    # get value
                    value = returnedData[index]

                    # Construct signals
                    newEvents.extend([self.construct_signal_event(output, value) for output in self.getOutputs(outputName)])

            else:
                raise(Exception(f"Len of output {returnedDataType} ({len(returnedData)}) is not equal to the number of the output ({len(boxOutputsNames)})"))

            return newEvents
            
        elif returnedDataType == dict:
            boxOutputsNames = self.outputNames

            newEvents = []

            if all([outputValueKey in boxOutputsNames for outputValueKey in returnedData.keys()]):

                for outputName in boxOutputsNames:
                    # get value
                    value = returnedData[outputName]

                    # Construct signals
                    newEvents.extend([self.construct_signal_event(output, value) for output in self.getOutputs(outputName)])

            else:
                raise(Exception(f"Not all outputs name ({list(returnedData.keys())}) of returned dictionnary are in self outputs ({boxOutputsNames})"))
        
            return newEvents

        else:
            return [self.construct_signal_event(outputSignal, returnedData) for outputSignal in self._outputSignals]

        # Retour du tableau d'activation.
        # return returnedData

    def end (self) -> None :
        """Permet d'appeler la méthode de fin de la box une fois que le planificateur a terminé."""
        self._end_method(self)

    def append_input(self, input_: Input):
        self._inputs.append(input_)

    def append_output(self, output: Output):
        self._outputs.append(output)

    def append_input_signals (self, *inputs : Signal) -> None : 
        """Permet d'ajouter autant d'entrée que voulue à la box."""
        for input in inputs :
            self._inputSignals[input] = -1

    def append_output_signals (self, *outputs : Signal) -> None :
        """Permet d'ajouter autant de sorties que voulue à la box."""
        for output in outputs :
            self._outputSignals.append(output)

    def get_input (self, inputIndex : Union[int, str]) -> Signal :
        """Permet de récuperer un index suivant son index dans la liste de la boite actuelle."""
        # Create list of signals
        signals = list(self._inputSignals.keys())

        # If string index → get input index by name
        if type(inputIndex) == str:
            try: 
                inputIndex = [signal.input_name for signal in signals].index(inputIndex)
            except:
                inputIndex = -1

        # Return selected signals
        if type(inputIndex) == int and inputIndex < len(signals) and inputIndex > -1:
            return signals[inputIndex]
        else:
            LogManager().error(TypeError(f"Unsupported type for inputIndex parameter: {type(inputIndex)} instead of int or str"))
            return None
        
    def getOutputs(self, outputIndex: Union[str, int]) -> Signal:
        if isinstance(outputIndex, int):
            outputIndex = self.outputNames[outputIndex]

        if isinstance(outputIndex, str):
            return [outputSginal for outputSginal in self._outputSignals if outputIndex == outputSginal.output_name]

        else:
            LogManager().error(f"Unsupported type for {self.__class__.__name__}.getOutput(output): \n'output' parameter type = {type(outputIndex)} instead of 'str' or 'int'")

    def get_parameter(self, name: str):
        if name in self._params:
            return self._params[name]
        else:
            raise(Exception(f"No {name} parameter in Box parameters -> {[param for param in self._params]}"))

    def construct_signal_event (self, output : Signal, value : Any) -> SignalEvent :
        """Permet de générer des events signal."""
        
        if output.inverted:
            if isinstance(value, numbers.Number):
                value = -value

        if isinstance(value, float) :
            if output.signal_type == DataType.FLOAT :
                data = Data(DataType.FLOAT, value)

            elif output.signal_type == DataType.INT :
                data = Data(DataType.INT, int(value))

        elif isinstance(value, str) :
            data = Data(DataType.STRING, value)
        
        elif isinstance(value, int) :
            if output.signal_type == DataType.FLOAT :
                data = Data(DataType.FLOAT, float(value))

            elif output.signal_type == DataType.INT :
                data = Data(DataType.INT, value)

        elif isinstance(value, object) :
            data = Data(DataType.OBJECT, value)

        else :
            data = Data(DataType.UNDIFINED, value)
        
        return SignalEvent(output, self, data)

    def __str__ (self) :
        """Permet de retourner la box sous la forme d'un string."""
        self._params.__setitem__
        return "Box [" + self._library + " " + self._name + " | " + str(self._index) + "]"

    def __getitem__ (self, name : str) -> Any :
        """Permet de récuperer un objet des paramètres en utilisant les crochets."""

        if name in self._params :
            return self._params.__getitem__(name)

        else :
            return None

    def __setitem__ (self, name : str, obj : Any) -> None :
        """Permet de modifier un paramètre en utilisant les crochets."""
        self._params.__setitem__(name, obj) 
        self._params.__iter__()

    def __delitem__ (self, name : str) -> None :
        """Permet de supprimer un paramètre en utilisant son nom."""
        self._params.__delitem__(name)

    def __iter__ (self) -> Iterator[str] :
        """Permet d'itérer dans les paramètres."""
        return self._params.__iter__()

    if sys.version_info >= (3, 8):
        def __reversed__ (self) -> Iterator[str] :
            """Permet de récuperer la version inversée de la liste des paramètres."""
            return self._params.__reversed__()

    def __contains__ (self, obj : str) -> bool : 
        """Permet de savoir si l'a box cotient l'élément passé en in."""
        return self._params.__contains__(obj)
