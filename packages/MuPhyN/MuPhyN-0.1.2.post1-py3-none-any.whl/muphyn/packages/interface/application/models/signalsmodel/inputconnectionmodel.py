#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import ctypes
from typing import Any, overload, Union

# PyQt6 Imports
from PyQt6.QtCore import QLineF, QPointF, Qt, QRectF
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsSceneDragDropEvent, QGraphicsSceneHoverEvent

# Project Imports
from muphyn.packages.core.application import DataType
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import GroupedShapes, Line, Text, Polygon, Circle
from muphyn.packages.interface.application.utils.constants import MuphynFonts

from ...actions.graphicalactions.diagram_unlink_nodes_action import DiagramUnlinkNodesAction
from ...actions.graphicalactions.diagram_link_nodes_action import DiagramLinkNodesAction
from ..graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from .signalnodemodel import SignalNodeModel
from .abstractconnectionmodel import AbstractConnectionModel

#-----------------------------------
# Class
#-----------------------------------

class InputConnectionModel (SignalNodeModel) :
    """Est la classe décrivant le fonctionnement des entrées des boxes."""
    # -------------
    # Static Values
    # -------------
    ConnectorPoints = [
        QPointF(0, AbstractConnectionModel.ConnectorSide),
        QPointF(0, 2 * AbstractConnectionModel.ConnectorSide),
        QPointF(AbstractConnectionModel.ConnectorSide, 3 * AbstractConnectionModel.ConnectorSide/2),
    ]
    LinePoints = [
        QPointF(AbstractConnectionModel.ConnectorSide, 3*AbstractConnectionModel.ConnectorSide/2),
        QPointF(AbstractConnectionModel.ConnectorSide + AbstractConnectionModel.ConnectorLineLength, 3*AbstractConnectionModel.ConnectorSide/2)
    ]

    InvertedInputCircleRadius = AbstractConnectionModel.ConnectorLineLength / 4
    InvertedInputCircleCenter = QPointF(
        AbstractConnectionModel.ConnectorSide + 0.75 * AbstractConnectionModel.ConnectorLineLength, 
        ConnectorPoints[2].y()
    )
    InvertedInputLinePoints = [
        QPointF(AbstractConnectionModel.ConnectorSide, 3*AbstractConnectionModel.ConnectorSide/2),
        QPointF(AbstractConnectionModel.ConnectorSide + AbstractConnectionModel.ConnectorLineLength/2, 3*AbstractConnectionModel.ConnectorSide/2)
    ]


    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, text : str = '', is_infinite : bool = False, 
                  parent : QGraphicsItem = None) :

        SignalNodeModel.__init__(self, name, data_type, position, AbstractConnectionModel.ItemSize, [], text, is_infinite, parent=parent)
        
        # Enable Dropping
        self.setAcceptDrops(True)
        
        # Connector Group
        self._connectorGroup = GroupedShapes(parent=self)

        # Draw Input
        self.drawInput()

        # Connect events
        self._connectorGroup.setAcceptHoverEvents(True)
        self._connectorGroup.hoverEnterEvent = self.connectorHoverEnterEvent
        self._connectorGroup.hoverLeaveEvent = self.connectorHoverLeaveEvent

        self.param_changed.connect(self.onParamChanged)

    # -------------
    # Properties
    # -------------       
    @property
    def is_connected_to_input (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""
        return True

    @property 
    def is_input (self) -> bool :
        """Permet de savoir si l'élément est une entrée."""
        return True

    # -------------
    # Methods
    # -------------
    def connector_bounding_rect(self):
        return self._connectorGroup.boundingRect()
    
    def drawConnector(self):
        # Connector
        self._connector: Polygon = Polygon(
            InputConnectionModel.ConnectorPoints,
            border_color=self._color,
            fill_color=Qt.GlobalColor.white,
            pen_join_style=Qt.PenJoinStyle.RoundJoin, 
            parent=self._connectorGroup
        )

        # Get Connector center
        self.connector_center = self._connector.boundingRect().center()

    def drawInvertedInput(self):
        # Draw Circle
        self._circle = Circle(InputConnectionModel.InvertedInputCircleCenter, 
            InputConnectionModel.InvertedInputCircleRadius, parent=self._connectorGroup)
        
        # Reset Line
        self.setLine(QLineF(*InputConnectionModel.InvertedInputLinePoints))

    def drawLabel(self):
        # Label
        self._label = Text(
            self._text, QPointF(-3, 0), 
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight,
            font=MuphynFonts.IOConnectorFont, parent=self)
        
        # Hide label
        self._label.hide()
    
    def drawNormalInput(self):
        # Undraw Circle
        if hasattr(self, "_circle") and self._circle is not None:
            self._circle.setParentItem(None)
            self._circle.deleteLater()

        # Reset Line
        self.setLine(QLineF(*InputConnectionModel.LinePoints))

    def drawInput(self):
        # Draw Connector
        if not hasattr(self, "_connector") or self._connector is None:
            self.drawConnector()

        # Draw Label
        if not hasattr(self, "_label") or self._label is None:
            self.drawLabel()

        # Draw rest of Input
        if self._connectionType == AbstractConnectionModel.ConnectionType.Normal:
            self.drawNormalInput()
        elif self._connectionType == AbstractConnectionModel.ConnectionType.Inverted:
            self.drawInvertedInput()
        else:
            self.drawNormalInput()

    def setLine(self, newLine: QLineF):
        if not hasattr(self, "_line") or self._line is None:
            self._line = Line(newLine, parent=self._connectorGroup)
        else:
            self._line.line = newLine

    def setConnectionType(self, newConnectionType: Union[int, AbstractConnectionModel.ConnectionType]):
        if type(newConnectionType) == int:
            newConnectionType = AbstractConnectionModel.ConnectionType(newConnectionType)

        if self._connectionType != newConnectionType:
            super().setConnectionType(newConnectionType)

            # Redraw Input
            self.drawInput()

    # -------------
    # Event Methods
    # -------------
    def connectorHoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        self._label.show()
        return super().hoverEnterEvent(event)

    def connectorHoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        self._label.hide()
        return super().hoverLeaveEvent(event)
        
    def dragEnterEvent (self, event: QGraphicsSceneDragDropEvent) -> None :
        if event.possibleActions() == Qt.DropAction.LinkAction :
            if not(self.is_connected) :
                if self.data_type.__str__() == event.mimeData().data('type') :
                    event.accept()
                    return super().dragEnterEvent(event)
            
        event.ignore()

        return super().dragEnterEvent(event)

    def dragMoveEvent(self, event : QGraphicsSceneDragDropEvent) -> None :
        if event.possibleActions() == Qt.DropAction.LinkAction :
            if not(self.is_connected) :
                if self.data_type.__str__() == event.mimeData().data('type') :
                    event.accept()
                    return super().dragEnterEvent(event)
        
        event.ignore()

        return super().dragEnterEvent(event)

    def dropEvent (self, event: QGraphicsSceneDragDropEvent) -> None :
        if event.possibleActions() == Qt.DropAction.LinkAction and event.mimeData().data('action') == 'new link':
            # If a link already exists → Unbind it
            if self.is_connected:
                link = list(self.links)[0]
                removeLinkAction = DiagramUnlinkNodesAction(link)
                removeLinkAction.do()
                self.scene().parent().parent().actions_holder.append(removeLinkAction)

            # Add new link
            node = ctypes.cast(int(event.mimeData().data('link')), ctypes.py_object).value
            addLinkAction = DiagramLinkNodesAction(self, node)
            addLinkAction.do()
            self.scene().parent().parent().actions_holder.append(addLinkAction)
    
            event.accept()

        return super().dropEvent(event)

    def add_link (self, link : Any) -> None :
        """Permet d'ajouter un lien à la position données."""

        if link is None : 
            return

        if len(self._links) > 0 :
            return

        self._links.append(link)

    def insert_link (self, index : int, link : Any) -> None :
        """Permet d'insérer un lien à la position données."""

        if link is None : 
            return

        if len(self._links) > 0 :
            return

        if index > len(self._links) :
            return

        self._links.insert(index, link)

    def has_link(self) -> bool:
        return len(self._links) > 0

    def to_dict(self) -> dict:
        input_dict = {
            "text": self.text,
            "signal_index": -1,
            "connectionType": self._connectionType.value
        }

        return input_dict
    
    def onParamChanged(self, connection_model: AbstractConnectionModel, param_name: str, old_value: Any, new_value: Any):
        if param_name == "text":
            self._label.text = new_value

class InputConnectionGroupModel(AbstractGraphicalElement):
    
    def __init__(self, name: str, is_infinite: bool, data_type: DataType, minimum_count: int, maximum_count: int, 
            default_count: int=0, group_position: QPointF = QPointF(), rotation: float = 0, text: str = '', parent: QGraphicsItem = None) -> None:
        super().__init__(name, group_position, rotation, text, parent)

        # Save group parameters
        self._name: str = name
        self._is_infinite = is_infinite
        self._data_type: DataType = data_type
        self._minimum_count: int = minimum_count if minimum_count >= 0 else 0
        self._maximum_count: int = maximum_count if maximum_count >= minimum_count else minimum_count+1

        # Init inputs list
        self._inputs: list[InputConnectionModel] = []

        for input_index in range(default_count):
            new_input = InputConnectionModel(
                name, 
                data_type, 
                QPointF(0, input_index * (AbstractConnectionModel.ItemHeight + 10)), 
                f"{name}_{input_index}", 
                is_infinite, 
                parent=self
            )
            self._inputs.append(new_input)

    
    # -------------
    # Properties
    # -------------
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if new_name != self._name:
            self._name = new_name

    @property
    def is_infinite(self) -> bool:
        return self._is_infinite

    @is_infinite.setter
    def is_infinite(self, new_is_infinite: str) -> None:
        if new_is_infinite != self._is_infinite:
            self._is_infinite = new_is_infinite

    @property
    def data_type(self) -> DataType:
        return self._data_type

    @data_type.setter
    def data_type(self, new_data_type: str) -> None:
        if new_data_type != self._data_type:
            self._data_type = new_data_type

    @property
    def minimum_count(self) -> int:
        return self._minimum_count

    @minimum_count.setter
    def minimum_count(self, new_minimum_count: str) -> None:
        if new_minimum_count != self._minimum_count:
            self._minimum_count = new_minimum_count

    @property
    def maximum_count(self) -> int:
        return self._maximum_count

    @maximum_count.setter
    def maximum_count(self, new_maximum_count: str) -> None:
        if new_maximum_count != self._maximum_count:
            self._maximum_count = new_maximum_count

    @property
    def count(self) -> int:
        return len(self._inputs)

    @count.setter
    def count(self, new_count: str) -> None:
        if new_count != self._count:
            self._count = new_count

    @property
    def inputs(self) -> list[InputConnectionModel]:
        return self._inputs

    @property
    def diagram_model (self) :
        return self.parent().diagram_model

    @diagram_model.setter
    def diagram_model (self, new_diagram_model) :
        self.diagram_model = new_diagram_model

    # -------------
    # Methods
    # -------------
    def connectors_bounding_rect(self):
        if len(self._inputs) == 0:
            return QRectF()
        elif len(self._inputs) == 1:
            return self._inputs[0].connector_bounding_rect()
        else:
            # Init connectors bounding rect
            connectors_bounding_rect = self._inputs[0].connector_bounding_rect()
            for input_ in self._inputs:
                connectors_bounding_rect = connectors_bounding_rect.united(input_.connector_bounding_rect())

            return connectors_bounding_rect

    def append_input(self) -> InputConnectionModel:
        # Add new graphical item in the group
        new_input = InputConnectionModel(
            self._name, 
            self._data_type, 
            QPointF(0, len(self._inputs) * (AbstractConnectionModel.ItemHeight + 10)), 
            f"{self._name}_{len(self._inputs)}", 
            self._is_infinite, 
            parent=self
        )
        new_input.action_param_semaphore = False

        # Append input in the list
        self._inputs.append(new_input)

        return new_input

    def insert_input(self, input_index) -> InputConnectionModel:
        # Recompute all inputs positions
        new_input = InputConnectionModel(
            self._name,
            self._data_type,
            QPointF(0, len(self._inputs) * (AbstractConnectionModel.ItemHeight + 10)),
            f"{self._name}_{len(self._inputs)}",
            self._is_infinite,
            parent=self
        )
        new_input.action_param_semaphore = False
        
        # Recompute all inputs positions
        self._inputs.insert(input_index, new_input)

        # Recompute all inputs positions
        self.recompute(from_index=input_index)

        return new_input

    @overload
    def remove_input(self, input_index: int) -> InputConnectionModel:
        ...

    @overload
    def remove_input(self, input_: InputConnectionModel) -> InputConnectionModel:
        ...

    def remove_input(self, input_: Union[int, InputConnectionModel]) -> InputConnectionModel:
        if type(input_) == int:
            # Get input_ index
            input_index = input_
            
            # Get input_ item
            input_ = self._inputs[input_index]
        elif type(input_) == InputConnectionModel:
            # Get input_ index
            input_index = self._inputs.index(input_)
            
            # Get input_ item
            input_ = self._inputs[input_index]
        else:
            LogManager().error(f"InputConnectionGroupModel.remove_input(): given arg is not a supported type '{type(input_)}' instead of 'int' or 'InputConnectionModel'")
            return 
            
        # Remove item from list
        self._inputs.remove(input_)

        # Remove from connection group
        input_.setParentItem(None)

        # Delete graphical item
        input_.deleteLater()

        # Recompute positions
        self.recompute(from_index=input_index)

    def clear_inputs(self):
        if self._is_infinite:
            # Remove only if this group is infinite
            while len(self._inputs) > 0:
                # Pop input_ from the list
                input_ = self._inputs.pop(0)

                # Remove graphical item
                input_.deleteLater()


    def recompute(self, from_index: int = 0):
        # If index is out of list limit → don't do anything
        if from_index < 0 or from_index >= len(self._inputs):
            return

        # Recompute positions
        for input_index, input_ in enumerate(self._inputs[from_index:]):
            input_.setPos(QPointF(0, input_index * (AbstractConnectionModel.ItemHeight + 10)))

    def to_dict(self) -> dict:
        inputs_group_dict = {
            "name": self.name,
            "isInfinite": self.is_infinite,
            "data_type": str(self.data_type),
            "inputs": [input_.to_dict() for input_ in self._inputs]
        }

        return inputs_group_dict