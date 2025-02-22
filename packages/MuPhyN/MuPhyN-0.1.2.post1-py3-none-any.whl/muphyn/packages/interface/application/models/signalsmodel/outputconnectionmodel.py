#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from typing import Iterable, overload, Union, Any

# PyQt6 Imports
from PyQt6.QtCore import QLineF, QPointF, Qt, QRectF
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent

# Project Imports
from muphyn.packages.core.application import Data, DataType
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.application.utils.constants import MuphynFonts
from muphyn.packages.interface.base import GroupedShapes, Line, Text, Polygon, Circle

from ..graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from .abstractconnectionmodel import AbstractConnectionModel
from .signallinkmodel import SignalLinkModel
from .signalnodemodel import startDrag


#-----------------------------------
# Class
#-----------------------------------

class OutputConnectionModel (AbstractConnectionModel) :
    """Est la classe décrivant le fonctionnement des sorties des boxes."""

    # -------------
    # Static Values
    # -------------
    ConnectorPoints = [
        QPointF(AbstractConnectionModel.ConnectorLineLength, AbstractConnectionModel.ConnectorSide),
        QPointF(AbstractConnectionModel.ConnectorLineLength, 2*AbstractConnectionModel.ConnectorSide),
        QPointF(AbstractConnectionModel.ConnectorLineLength + AbstractConnectionModel.ConnectorSide, 3*AbstractConnectionModel.ConnectorSide/2)
    ]
    LinePoints = [
        QPointF(0, 3*AbstractConnectionModel.ConnectorSide/2),
        QPointF(AbstractConnectionModel.ConnectorLineLength, 3*AbstractConnectionModel.ConnectorSide/2)
    ]
    
    InvertedOutputCircleRadius = AbstractConnectionModel.ConnectorLineLength / 4
    InvertedOutputCircleCenter = QPointF(
        InvertedOutputCircleRadius, 
        ConnectorPoints[2].y()
    )
    InvertedOutputLinePoints = [
        QPointF(AbstractConnectionModel.ConnectorLineLength/2, 3*AbstractConnectionModel.ConnectorSide/2),
        QPointF(AbstractConnectionModel.ConnectorLineLength, 3*AbstractConnectionModel.ConnectorSide/2)
    ]

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, data_type : DataType, position : QPointF, link : SignalLinkModel = None,
                  default_value : Data = None, text : str = '', is_infinite : bool = False, parent : QGraphicsItem = None) :
        
        links : Iterable[SignalLinkModel] = []
        if link is not None:
            links.append(link)

        AbstractConnectionModel.__init__(self, name, data_type, position, AbstractConnectionModel.ItemSize, links, text, is_infinite, parent=parent)

        self._default_value : Data = default_value

        # Connector Group
        self._connectorGroup = GroupedShapes(parent=self)

        # Draw Output
        self.drawOutput()

        # Connect events
        self._connectorGroup.setAcceptHoverEvents(True)
        self._connectorGroup.hoverEnterEvent = self.connectorHoverEnterEvent
        self._connectorGroup.hoverLeaveEvent = self.connectorHoverLeaveEvent

        self.param_changed.connect(self.onParamChanged)

    # -------------
    # Properties
    # -------------
    @property
    def default_value (self) -> Data :
        """Permet de récuperer la valeur par défaut du signal."""
        return self._default_value

    @default_value.setter
    def default_value (self, default_value_ : Data) -> None :
        """Permet de modifier la valeur par défaut du signal."""
        self._default_value = default_value_

    @property
    def is_connected_to_output (self) -> bool :
        """Permet de savoir si l'élément actuel est connecté à une entrée (ou est un entrée)."""
        return False

    # -------------
    # Methods
    # -------------
    def connector_bounding_rect(self):
        return self._connectorGroup.boundingRect()
    
    def drawConnector(self):
        # Connector
        self._connector: Polygon = Polygon( 
            OutputConnectionModel.ConnectorPoints, 
            border_color=self._color,
            fill_color=Qt.GlobalColor.white,
            pen_join_style=Qt.PenJoinStyle.RoundJoin, 
            parent=self._connectorGroup
        )

        # Get Connector center
        self.connector_center = self._connector.boundingRect().center()

    def drawInvertedOutput(self):
        # Draw Circle
        self._circle = Circle(OutputConnectionModel.InvertedOutputCircleCenter, 
            OutputConnectionModel.InvertedOutputCircleRadius, parent=self._connectorGroup)
        
        # Reset Line
        self.setLine(QLineF(*OutputConnectionModel.InvertedOutputLinePoints))

    def drawLabel(self):
        # Label
        self._label: Text = Text(
            self._text, QPointF(AbstractConnectionModel.ItemWidth+3, 0), 
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
            font=MuphynFonts.IOConnectorFont, parent=self
        )
        
        # Hide label
        self._label.hide()

    def drawNormalOutput(self):
        # Undraw Circle
        if hasattr(self, "_circle") and self._circle is not None:
            self._circle.setParentItem(None)
            self._circle.deleteLater()

        # Reset Line
        self.setLine(QLineF(*OutputConnectionModel.LinePoints))

    def drawOutput(self):
        # Draw Connector
        if not hasattr(self, "_connector") or self._connector is None:
            self.drawConnector()

        # Draw Label
        if not hasattr(self, "_label") or self._label is None:
            self.drawLabel()

        # Draw rest of Output
        if self._connectionType == AbstractConnectionModel.ConnectionType.Normal:
            self.drawNormalOutput()
        elif self._connectionType == AbstractConnectionModel.ConnectionType.Inverted:
            self.drawInvertedOutput()
        else:
            self.drawNormalOutput()

    def setLine(self, newLine: QLineF):
        if not hasattr(self, "_line") or self._line is None:
            self._line = Line(newLine, parent=self._connectorGroup)
        else:
            self._line.line = newLine

    def setConnectionType(self, newConnectionType: AbstractConnectionModel.ConnectionType):
        if type(newConnectionType) == int:
            newConnectionType = AbstractConnectionModel.ConnectionType(newConnectionType)

        if self._connectionType != newConnectionType:
            super().setConnectionType(newConnectionType)

            # Redraw Output
            self.drawOutput()

    # -------------
    # Event Methods
    # -------------
    def connectorHoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        self._label.show()
        return super().hoverEnterEvent(event)

    def connectorHoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        self._label.hide()
        return super().hoverLeaveEvent(event)

    def on_is_connected_changed(self):
        self._connector.background_color = Qt.GlobalColor.black if self.is_connected else Qt.GlobalColor.white

    def mousePressEvent (self, event: QGraphicsSceneMouseEvent) -> None :
        if (event.button() == Qt.MouseButton.LeftButton and self.isUnderMouse()) :
            # self._tempLink = TemporaryLinkModel(self)
            # self.diagram_model.add_element(self._tempLink)
            startDrag(self, event)
            event.accept() 
        else:
            return super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        if hasattr(self, "_tempLink") and self._tempLink is not None:
            # self.diagram_model.remove_element(self._tempLink)
            # startDrag(self, event)
            event.accept()
        else:
            super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if hasattr(self, "_tempLink") and self._tempLink is not None:
            self._tempLink.mouseMoveEvent(event)
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def has_link(self) -> bool:
        return len(self._links) > 0
        
    def to_dict(self) -> dict:
        output_dict = {
            "text": self.text,
            "signal_indices": [],
            "connectionType": self._connectionType.value
        }

        return output_dict
    
    def onParamChanged(self, connection_model: AbstractConnectionModel, param_name: str, old_value: Any, new_value: Any):
        if param_name == "text":
            self._label.text = new_value

class OutputConnectionGroupModel(AbstractGraphicalElement):
    
    def __init__(self, name: str, is_infinite: bool, data_type: DataType, minimum_count: int, maximum_count: int, 
            default_count: int=0, group_position: QPointF = QPointF(), rotation: float = 0, text: str = '', parent: QGraphicsItem = None) -> None:
        super().__init__(name, group_position, rotation, text, parent)

        # Save group parameters
        self._name: str = name
        self._is_infinite = is_infinite
        self._data_type: DataType = data_type
        self._minimum_count: int = minimum_count if minimum_count >= 0 else 0
        self._maximum_count: int = maximum_count if maximum_count >= minimum_count else minimum_count+1

        # Init outputs list
        self._outputs: list[OutputConnectionModel] = []

        for _ in range(default_count):
            self.append_output()

    
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
        return len(self._outputs)

    @count.setter
    def count(self, new_count: str) -> None:
        if new_count != self._count:
            self._count = new_count

    @property
    def outputs(self) -> list[OutputConnectionModel]:
        return self._outputs

    @property
    def diagram_model (self) :
        return self.parent().diagram_model

        
    # -------------
    # Methods
    # -------------
    def connectors_bounding_rect(self):
        if len(self._outputs) == 0:
            return QRectF()
        elif len(self._outputs) == 1:
            return self._outputs[0].connector_bounding_rect()
        else:
            # Init connectors bounding rect
            connectors_bounding_rect = self._outputs[0].connector_bounding_rect()
            for output in self._outputs:
                connectors_bounding_rect = connectors_bounding_rect.united(output.connector_bounding_rect())

            return connectors_bounding_rect

    def append_output(self) -> OutputConnectionModel:
        # Add new graphical item in the group
        new_output = OutputConnectionModel(
            name = self._name, 
            data_type = self._data_type, 
            position = QPointF(0, len(self._outputs) * (AbstractConnectionModel.ItemHeight + 10)), 
            text = f"{self._name}_{len(self._outputs)}", 
            is_infinite = self._is_infinite, 
            parent=self
        )
        new_output.action_param_semaphore = False

        # Append output in the list
        self._outputs.append(new_output)

        return new_output

    def insert_output(self, output_index) -> OutputConnectionModel:
        # Recompute all outputs positions
        new_output = OutputConnectionModel(
            name = self._name, 
            data_type = self._data_type, 
            position = QPointF(0, len(self._outputs) * (AbstractConnectionModel.ItemHeight + 10)), 
            text = f"{self._name}_{len(self._outputs)}", 
            is_infinite = self._is_infinite, 
            parent=self
        )
        new_output.action_param_semaphore = False
        
        # Recompute all outputs positions
        self._outputs.insert(output_index, new_output)

        # Recompute all outputs positions
        self.recompute(from_index=output_index)

        return new_output

    @overload
    def remove_output(self, output_index: int) -> OutputConnectionModel:
        ...

    @overload
    def remove_output(self, output: OutputConnectionModel) -> OutputConnectionModel:
        ...

    def remove_output(self, output: Union[int, OutputConnectionModel]) -> OutputConnectionModel:
        if type(output) == int:
            # Get output index
            output_index = output
            
            # Get output item
            output = self._outputs[output_index]
        elif type(output) == OutputConnectionModel:
            # Get output index
            output_index = self._outputs.index(output)
            
            # Get output item
            output = self._outputs[output_index]
        else:
            LogManager().error(f"OutputConnectionGroupModel.remove_output(): given arg is not a supported type '{type(output)}' instead of 'int' or 'OutputConnectionModel'")
            return 
            
        # Remove item from list
        self._outputs.remove(output)

        # Remove from connection group
        output.setParentItem(None)

        # Delete graphical item
        output.deleteLater()

        # Recompute positions
        self.recompute(from_index=output_index)

    def clear_outputs(self):
        if self._is_infinite:
            # Remove only if this group is infinite
            while len(self._outputs) > 0:
                # Pop output from the list
                output = self._outputs.pop(0)

                # Remove graphical item
                output.deleteLater()

    def recompute(self, from_index: int = 0):
        # If index is out of list limit → don't do anything
        if from_index < 0 or from_index >= len(self._outputs):
            return

        # Recompute positions
        for output_index, output in enumerate(self._outputs[from_index:]):
            output.setPos(QPointF(0, output_index * (AbstractConnectionModel.ItemHeight + 10)))
            
    def to_dict(self) -> dict:
        outputs_group_dict = {
            "name": self.name,
            "isInfinite": self.is_infinite,
            "data_type": str(self.data_type),
            "outputs": [output.to_dict() for output in self._outputs]
        }

        return outputs_group_dict