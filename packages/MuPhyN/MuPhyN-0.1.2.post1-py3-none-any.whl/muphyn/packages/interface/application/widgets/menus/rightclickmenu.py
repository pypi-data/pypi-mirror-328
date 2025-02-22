from enum import Enum
from typing import Dict, Iterable, Union

from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QWidget

from muphyn.packages.interface.base import RotateLeftAction, RotateRightAction, DeleteAction

from ...models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ...models.linksmodel.abstractlinkmodel import AbstractLinkModel

class RightClickContextMenu(QMenu):

    class Type(Enum):
        NoAction = 0
        DeleteItem = 1
        RotateLeftItem = 2
        RotateRightItem = 3
        RemoveSelectedItems = 4
        OpenMultiPhysicsModel = 5
        OpenBoxDocumentation = 6

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        # Init actions dict
        self._actions: Dict[QAction, RightClickContextMenu.Type] = {}

        # Delete Selected Items action
        self._removeSelectedItems = DeleteAction("Remove selected items")

        # 
        self.addAction(self._removeSelectedItems, RightClickContextMenu.Type.RemoveSelectedItems)

    def addAction(self, action: QAction, type_: Type):
        # 
        self._actions[action] = type_       
        super().addAction(action)

    def addActions(self, actions: QAction, types: Iterable[Type]):
        # 
        for actionIndex, action in enumerate(actions):
            self._actions[action] = types[actionIndex]        
        super().addActions(actions)

    def insertAction(self, before: QAction, action: QAction, type_: Type) -> None:
        # Add action to dict
        self._actions[action] = type_
        return super().insertAction(before, action)
    
    def insertActions(self, before: QAction, actions: Iterable[QAction], types: Iterable[Type]) -> None:
        for actionIndex, action in enumerate(actions):
            self._actions[action] = types[actionIndex]  
        return super().insertActions(before, actions)

    def getActionType(self, selectedAction: QAction) -> Type:
        for action in self._actions:
            if action == selectedAction:
                return self._actions[action]
        return RightClickContextMenu.Type.NoAction

    def openContextMenu(self, position: Union[QPoint, QPointF] = QPoint()) -> Type:
        # Convert to QPoint
        if type(position) == QPointF:
            position = position.toPoint()

        # Open context menu
        selectedAction: QAction = self.exec(position)

        return self.getActionType(selectedAction)


class BoxModelRightClickContextMenu(RightClickContextMenu):

    def __init__(self, boxModel: AbstractBoxModel, parent: QWidget = None):
        super().__init__(parent)

        # Init actions
        self._rotateLeft = RotateLeftAction()
        self._rotateRight = RotateRightAction()
        self._deleteItem = DeleteAction("Delete Box")
        self._openDocumentation = QAction("Open Documentation")

        # Append Actions
        self.insertActions(
            self._removeSelectedItems, 
            [self._rotateLeft, self._rotateRight, self._deleteItem, self._openDocumentation],
            [
                RightClickContextMenu.Type.RotateLeftItem, 
                RightClickContextMenu.Type.RotateRightItem, 
                RightClickContextMenu.Type.DeleteItem,
                RightClickContextMenu.Type.OpenBoxDocumentation
            ]
        )

        # Add separator
        self.insertSeparator(self._openDocumentation)

        if boxModel.box_type == "multiphysics-simulation":
            # Open Modelica
            self._openModel = self.insertAction(self._removeSelectedItems, QAction("Open Modelica Model"), RightClickContextMenu.Type.OpenMultiPhysicsModel)

        # Add separator
        self.insertSeparator(self._removeSelectedItems)

class LinkModelRightClickContextMenu(RightClickContextMenu):

    def __init__(self, linkModel: AbstractLinkModel, parent: QWidget = None):
        super().__init__(parent)

        # Init actions
        self._deleteItem = DeleteAction("Delete link")

        # Append Actions
        self.insertAction(self._removeSelectedItems, self._deleteItem, RightClickContextMenu.Type.DeleteItem)

        # # Add separator
        self.insertSeparator(self._removeSelectedItems)

def rightClickContextMenu(graphicalItemUnderMouse, parent: QWidget = None):
    # Init right click context menu
    contextMenu = RightClickContextMenu()

    # Abstract Box Model
    if isinstance(graphicalItemUnderMouse, AbstractBoxModel):
        contextMenu = BoxModelRightClickContextMenu(graphicalItemUnderMouse, parent)
    elif isinstance(graphicalItemUnderMouse, AbstractLinkModel):
        contextMenu = LinkModelRightClickContextMenu(graphicalItemUnderMouse, parent)

    return contextMenu
