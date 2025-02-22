
#-----------------------------------
# Imports
#-----------------------------------
import os
from datetime import date
from typing import Callable, List, Any, Dict, Optional

from PyQt6.QtCore import QSize, QRect, QPoint
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QColor

from muphyn.packages.core.base import loadCode
from muphyn.utils.paths import ROOT_DIR

from .plci_core_box import Box
from ..data.plci_core_data import Data
from ..data.plci_core_data_type import DataType, get_data_type
from ..diagram.plci_core_diagram import Diagram
from ..signal.plci_core_signal import Signal
from ..signal.plci_core_signal_event import SignalEvent
from ..scheduler.plci_core_scheduler_event import SchedulerEvent

#-----------------------------------
# Methods
#-----------------------------------

def constructDiagram (signals : Dict, boxes : Dict, inputs : Dict, outputs : Dict, box_params : Dict[str, Any], boxes_library : Any) -> Diagram :
   
    diagram = Diagram()
    
    for signal_data in signals :
        
        data_type : DataType = get_data_type(signal_data['type'])
        signal : Signal = Signal(signal_data['index'], data_type, signal_data['value']) 
        diagram.append(signal)

    for box_data in boxes :

        params = box_data['params']
        if params == 'None' :
            box = boxes_library.construct_box(box_data['library'], box_data['name'])
        else :
            box = boxes_library.construct_box(box_data['library'], box_data['name'], **params)
        
        if isinstance(box, Diagram) :
            diagram.append(box)

            if not box_data['inputs'] == 'None' :

                for signal_index, input in enumerate(box_data['inputs']) :
                    signal = diagram.signals[input['signal_index']]
                    
                    input_signal = box.signals[box.inputSignals[signal_index]]
                    diagram.add_linked_signals(signal, input_signal)

            if not box_data['outputs'] == 'None' :

                for signal_index, output in enumerate(box_data['outputs']) :
                    signal = diagram.signals[output['signal_index']]
                    
                    output_signal = box.signals[box.outputs[signal_index]]
                    diagram.add_linked_signals(output_signal, signal)

        elif isinstance(box, Box) :
            diagram.append(box)

            if not box_data['inputs'] == 'None' :

                for box_input_data in box_data['inputs'] :
                    diagram.add_box_inputs(box, diagram.signals[box_input_data['signal_index']])

            if not box_data['outputs'] == 'None' :
                
                for box_output_data in box_data['outputs'] :
                    diagram.add_box_outputs(box, diagram.signals[box_output_data['signal_index']])

    for input in inputs :
        diagram.inputs.append(input['signal_index'])

    for output in outputs :
        diagram.outputs.append(output['signal_index'])

    return diagram


#-----------------------------------
# Classes
#-----------------------------------

class AbstractBoxData : 
    """Est la classe commune des classes de données de bibliothèque."""

    # -------------
    # Constructors
    # -------------
    PixmapSize = QSize(60, 60)
    BasePixmapRect = QRect(1, 1, PixmapSize.width() - 2, PixmapSize.height() - 2)
    LogoPixmapSize = PixmapSize - QSize(5, 5)

    def __init__ (
            self, 
            path: str,
            box_name: str, 
            box_library: str, 
            box_type: str,
            creator: str,
            date_created: Any,
            version: float,
            inputs,
            outputs,
            description: str,
            icon: str = None
        ) :
        self._path = path
        self._boxName = box_name
        self._boxLibrary = box_library
        self._boxType = box_type
        self._creator : str = creator
        self._dateCreated : Any = date_created
        self._version : float = version
        self._inputs: dict[str, dict] = inputs
        self._outputs: dict[str, dict] = outputs
        self._fullBoxPath = self._boxLibrary + '.' + self._boxName
        self._description = description

        # Handling icon
        if icon is not None:
            if os.path.isabs(icon):
                self._icon = icon
            else:
                if icon.startswith("./") or icon.startswith("../"):
                    self._icon = os.path.join(os.path.dirname(path), icon).replace("\\", "/")
                else:
                    self._icon = ROOT_DIR + "/" + icon
        else:
            self._icon = None

    # -------------
    # Properties
    # -------------

    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, newPath: str):
        if self._path != newPath:
            self._path = newPath

    @property 
    def box_name (self) -> str :
        """Permet de récuperer le nom de la box."""
        return self._boxName
    
    @box_name.setter
    def box_name(self, newBoxName: str):
        if self._boxName != newBoxName:
            self._boxName = newBoxName

    @property
    def box_library (self) -> str :
        """Permet de récuperer la bibliothèque dans laquel se trouve la box."""
        return self._boxLibrary
    
    @box_library.setter
    def box_library(self, newBoxLibrary: str):
        if self._box_library != newBoxLibrary:
            self._box_library = newBoxLibrary

    @property 
    def box_complete_name (self) -> str :
        """Permet de récuperer le nom de la box."""
        return f"{self._boxLibrary}.{self._boxName}"

    @property
    def box_type (self) -> str :
        """Permet de récuperer la bibliothèque dans laquel se trouve la box."""
        return self._boxType
    
    @box_type.setter
    def box_type(self, newBoxType: str):
        if self._boxType != newBoxType:
            self._boxType = newBoxType

    @property
    def creator (self) -> str :
        """Permet de récuperer le nom de la personne qui a créé la box."""
        return self._creator
    
    @creator.setter
    def creator(self, newCreator: str):
        if self._creator != newCreator:
            self._creator = newCreator

    @property
    def date_created (self) -> Any :
        """Permet de récuperer la date à laquelle la box a été créée."""
        return self._dateCreated
    
    @date_created.setter
    def date_created(self, newCreationDate: Any):
        if self._dateCreated != newCreationDate:
            self._dateCreated = newCreationDate

    @property
    def version (self) -> float :
        """Permet de récuperer la version de la box."""
        return self._version
    
    @version.setter
    def version(self, newVersion: float):
        if self._version != newVersion:
            self._version = newVersion

    @property
    def inputs (self) :
        """Permet de récuperer la liste des signaux considérés comme entrées."""
        return self._inputs
    
    @inputs.setter
    def inputs(self, newInputs: Dict):
        if self._inputs != newInputs:
            self._inputs = newInputs

    @property
    def outputs (self) :
        """Permet de récuperer la liste des signaux considérés comme sorties."""
        return self._outputs
    
    @outputs.setter
    def outputs(self, newOutputs: Dict):
        if self._outputs != newOutputs:
            self._outputs = newOutputs

    @property
    def full_box_path (self) -> str :
        """Permet de récuperer le nom complet de la boite (bibliothèque + nom)."""
        return self._fullBoxPath
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, newDescription: str):
        if self._description != newDescription:
            self._description = newDescription

    @property
    def icon(self) -> str:
        return self._icon
    
    @icon.setter
    def icon(self, newIcon: str):
        if self._icon != newIcon:
            self._icon = newIcon
    
    @property
    def pixmap(self) -> QPixmap:
        # Init Pixmap
        basePixmap = QPixmap(AbstractBoxData.PixmapSize)
        basePixmap.fill(QColor(255, 255, 255))

        # Init painter
        painter = QPainter(basePixmap)

        # Draw border
        painter.setPen(QColor(0, 0, 0))
        painter.drawRect(AbstractBoxData.BasePixmapRect)

        if self._icon is not None and os.path.exists(self._icon):
            # Load Logo Pixmap
            logoPixmap = QIcon(self._icon).pixmap(AbstractBoxData.LogoPixmapSize)

            # Draw Logo
            sourceRect = QRect(QPoint(0, 0), AbstractBoxData.LogoPixmapSize)
            diffSize: QSize = (AbstractBoxData.BasePixmapRect.size() - sourceRect.size()) / 2
            offset = AbstractBoxData.BasePixmapRect.topLeft() + QPoint(diffSize.width(), diffSize.height())
            painter.drawPixmap(QRect(offset, AbstractBoxData.LogoPixmapSize), logoPixmap, sourceRect)
        
        return basePixmap


    # -------------
    # Methods
    # -------------

    def __lt__ (self, other) :
        return self._fullBoxPath.__lt__(other._fullBoxPath) 


    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Any :
        """Permet de générer la box."""
        raise Exception('AbstractBoxData construct_box is an abstract method and must be overriden !')
    
    @staticmethod
    def default():
        return AbstractBoxData("", "", "", "code", "", date.today(), 0, [], [], "", "")

class CompositeBoxData (AbstractBoxData) :
    """Est la classe qui permet de contenir les données des boxes composites."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (
            self, 
            path: str,
            box_name : str, 
            box_library : str, 
            creator : str,
            date_created : Any,
            version : float,
            signals, 
            boxes, 
            inputs, 
            outputs,
            icon: str = None
        ) :
        AbstractBoxData.__init__(self, path, box_name, box_library, creator, date_created, version, inputs, outputs, icon)
        self._signals = signals
        self._boxes = boxes
    
    # -------------
    # Properties
    # -------------
    @property
    def signals (self) :
        """Permet de récuperer le dictionnaire contenant la composition des signaux de la box composite."""
        return self._signals
    
    @signals.setter
    def signals(self, newSignals):
        if self._signals != newSignals:
            self._signals = newSignals

    @property
    def boxes (self) :
        """Permet de récuperer le dictionnaire contenant la composition des boxes de la box composite."""
        return self._boxes
    
    @boxes.setter
    def boxes(self, newBoxes):
        if self._boxes != newBoxes:
            self._boxes = newBoxes

    # -------------
    # Methods
    # -------------

    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Diagram :
        """Permet de générer la box."""
        
        return constructDiagram(self._signals, self._boxes, self._inputs, self._outputs, box_params, boxes_library)

class CodeBoxData (AbstractBoxData) :
    """Est la classe qui permet de contenir les données des boxes importées par un bibliothèque."""

    # -------------
    # Constructors
    # -------------
    def __init__ (
            self, 
            path: str,
            box_name : str, 
            box_library : str, 
            box_type: str,
            wait_for_event : bool, 
            wait_for_all_signal_events : bool,
            params : Dict[str, Data], 
            box_init_method_ : Callable[[Box], None], 
            box_function_ : Callable[[Box, SchedulerEvent], List[SignalEvent]], 
            box_end_method_ : Callable[[Box], None],
            creator : str,
            date_created : Any,
            version : float, 
            inputs,
            outputs,
            description: str,
            icon: str = None
        ) :

        AbstractBoxData.__init__(self, path, box_name, box_library, box_type, creator, date_created, version, inputs, outputs, description, icon)
        self._init_method: Optional[str] = box_init_method_
        self._box_function: Optional[str] = box_function_
        self._end_method: Optional[str] = box_end_method_
        self._params : Dict[str, Data] = params
        self._wait_for_event = wait_for_event
        self._wait_for_all_signal_events = wait_for_all_signal_events

    # -------------
    # Properties
    # -------------

    @property
    def init_method (self) -> str:
        """Permet de récuperer la méthode d'initialisation de la box."""
        return self._init_method
    
    @init_method.setter
    def init_method (self, newIniMethod: str):
        if self._init_method != newIniMethod:
            self._init_method = newIniMethod
    
    @property
    def box_function (self) -> str:
        """Permet de récuperer la fonction de la box."""
        return self._box_function
    
    @box_function.setter
    def box_function (self, newIniMethod: str):
        if self._box_function != newIniMethod:
            self._box_function = newIniMethod

    @property
    def end_method (self) -> str :
        """Permet de récuperer la méthode de fin de la box."""
        return self._end_method
    
    @end_method.setter
    def end_method (self, newIniMethod: str):
        if self._end_method != newIniMethod:
            self._end_method = newIniMethod

    @property
    def params (self) -> Dict[str, Data] : 
        """Permet de récuperer tous les paramètres requis pour la génération de ce type de box."""
        return self._params

    @params.setter
    def params (self, newParams: Dict[str, Data]):
        if self._params != newParams:
            self._params = newParams

    @property 
    def wait_for_event (self) -> bool :
        """Permet de récuperer le fait qu'il faille attendre un événement pour que la box puisse s'activer."""
        return self._wait_for_event

    @wait_for_event.setter 
    def wait_for_event (self, newWaitForEvent: bool):
        if self._wait_for_event != newWaitForEvent:
            self._wait_for_event = newWaitForEvent

    @property
    def wait_for_all_signal_events (self) -> bool :
        """Permet de récuperer le fait qu'il faille que toutes les entrées de la box aie eu des événements au timing actuel pour qu'elle s'active."""
        return self._wait_for_all_signal_events

    @wait_for_all_signal_events.setter
    def wait_for_all_signal_events (self, newWaitForAllSignalEvents: bool) :
        if self._wait_for_all_signal_events != newWaitForAllSignalEvents:
            self._wait_for_all_signal_events = newWaitForAllSignalEvents

    # -------------
    # Methods
    # -------------
    
    def construct_box (self, index, box_params : Dict[str, Any], boxes_library : Any) -> Box :
        """Permet de générer la box."""
        # Load code
        foo = loadCode(self._boxLibrary, f"{self._path}.py")

        # Init function
        if self._init_method is not None and self._init_method != "": 
            init_method = getattr(foo, self._init_method)
        else :
            init_method = lambda box, scheduler : ...

        # Simulation function
        if self._box_function is not None and self._box_function != "": 
            box_function = getattr(foo, self._box_function)
        else :
            box_function = lambda box, event : ...

        # End function
        if self._end_method is not None and self._end_method != "": 
            end_method = getattr(foo, self._end_method)
        else :
            end_method = lambda box : ...

        return Box(
                    index_ = index,
                    name_ = self.box_name,
                    library_ = self.box_library,
                    # init_method_ = init_method,
                    # function_ = box_function,
                    # end_method_ = end_method,
                    wait_for_events_ = self.wait_for_event,
                    wait_for_all_signal_events_ = self.wait_for_all_signal_events,
                    params_ = box_params
                )
    
    @staticmethod
    def default():
        defaultAbstractBoxData = AbstractBoxData.default()

        return CodeBoxData(
            defaultAbstractBoxData.path,
            defaultAbstractBoxData.box_name,
            defaultAbstractBoxData.box_library,
            defaultAbstractBoxData.box_type,
            True,
            True,
            {},
            None,
            None,
            None,
            defaultAbstractBoxData.creator,
            defaultAbstractBoxData.date_created,
            defaultAbstractBoxData.version,
            defaultAbstractBoxData.inputs,
            defaultAbstractBoxData.outputs,
            defaultAbstractBoxData.description,
            defaultAbstractBoxData.icon
        )

class MultiPhysicsSimulationBoxData(CodeBoxData):
    def __init__(self, path, box_name: str, box_library: str, box_type: str, wait_for_event: bool, wait_for_all_signal_events: bool, params: Dict[str, Data], box_init_method_: Callable[[Box], None], box_function_: Callable[[Box, SchedulerEvent], List[SignalEvent]], box_end_method_: Callable[[Box], None], creator: str, date_created: Any, version: float, inputs, outputs, icon: str = None):
        super().__init__(path, box_name, box_library, box_type, wait_for_event, wait_for_all_signal_events, params, box_init_method_, box_function_, box_end_method_, creator, date_created, version, inputs, outputs, icon)

    @staticmethod
    def fromCodeBoxData(codeBoxData: CodeBoxData):

        return MultiPhysicsSimulationBoxData(
            codeBoxData.box_name,
            codeBoxData.box_library,
            codeBoxData.box_type,
            codeBoxData.wait_for_event,
            codeBoxData.wait_for_all_signal_events,
            codeBoxData.params,
            None if not hasattr(codeBoxData, "box_init_method_") else codeBoxData.box_init_method_, 
            None if not hasattr(codeBoxData, "box_function_") else codeBoxData.box_function_, 
            None if not hasattr(codeBoxData, "box_end_method_") else codeBoxData.box_end_method_,
            codeBoxData.creator,
            codeBoxData.date_created,
            codeBoxData.version,
            codeBoxData.inputs,
            codeBoxData.outputs,
            codeBoxData.icon
        )