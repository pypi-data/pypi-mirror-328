from dataclasses import dataclass
from typing import Dict, List

from PyQt6.QtGui import QAction, QKeySequence

from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import \
    DeleteAction, RedoAction, RefreshAction, RotateLeftAction, RotateRightAction, \
    StartAction, StopAction, UndoAction

@dataclass
class ActionData:
    text: str
    shortcut: str = None
    actionClass: type[QAction] = None

actionsData = [
    # File
    ActionData("&Simulation", shortcut="Ctrl+N", actionClass=None),
    ActionData("&Box", shortcut="Ctrl+shift+N", actionClass=None),
    ActionData("Sche&duler", shortcut=None, actionClass=None),
    ActionData("&Open", shortcut="Ctrl+O", actionClass=None),
    ActionData("&Save", shortcut="Ctrl+S", actionClass=None),
    ActionData("S&ave as", shortcut="Ctrl+Shift+S", actionClass=None),
    ActionData("&Export", shortcut="Ctrl+E", actionClass=None),
    ActionData("&Close", shortcut="Ctrl+W", actionClass=None),
    ActionData("&Quit", shortcut="Alt+F4", actionClass=None),

    # Edit
    ActionData("&Undo", shortcut="Ctrl+Z", actionClass=UndoAction),
    ActionData("&Redo", shortcut="Ctrl+Y", actionClass=RedoAction),
    ActionData("C&ut", shortcut="Ctrl+X", actionClass=None),
    ActionData("&Copy", shortcut="Ctrl+C", actionClass=None),
    ActionData("&Paste", shortcut="Ctrl+V", actionClass=None),
    ActionData("Rotate right", shortcut=None, actionClass=RotateRightAction),
    ActionData("Rotate left", shortcut=None, actionClass=RotateLeftAction),
    ActionData("Flip", shortcut=None, actionClass=None),
    ActionData("Select all", shortcut="Ctrl+A", actionClass=None),
    ActionData("Invert selection", shortcut="Ctrl+Shift+A", actionClass=None),
    ActionData("Create simulation from selection", shortcut=None, actionClass=None),
    ActionData("Create composite box from selection", shortcut=None, actionClass=None),
    ActionData("Delete", shortcut="Delete", actionClass=DeleteAction),
    ActionData("Zoom +", shortcut="Ctrl++", actionClass=None),
    ActionData("Zoom -", shortcut="Ctrl+-", actionClass=None),
    ActionData("Close dialog windows", shortcut=None, actionClass=None),
    ActionData("Libraries", shortcut=None, actionClass=None),
    ActionData("Options", shortcut=None, actionClass=None),
    ActionData("Parameters", shortcut=None, actionClass=None),
    ActionData("Start simulation", shortcut="F5", actionClass=StartAction),
    ActionData("Stop simulation", shortcut="Shift+F5", actionClass=StopAction),
    ActionData("&Documentation", shortcut="F1", actionClass=None),
    ActionData("&About", shortcut=None, actionClass=None)
]

def buildAction(actionData: ActionData) -> QAction:
    # Get class of the action to build
    actionClass = QAction if actionData.actionClass is None else actionData.actionClass

    # Build action object
    action = actionClass(actionData.text)

    # Handle shortcut
    if actionData.shortcut is not None:
        action.setShortcut(QKeySequence(actionData.shortcut))
    return action

def buildAllActions() -> Dict[str, QAction]:
    # Init actions dictionnary
    actions: Dict[str, QAction] = {}

    # Init shortcuts dictionnary
    shortcuts: Dict[str, List[str]] = {}
    for actionData in actionsData:
        # Get action name
        actionName = actionData.text.replace('&', '')

        # Handle shortcut
        if actionData.shortcut is not None:
            if actionData.shortcut in shortcuts:
                shortcuts[actionData.shortcut].append(actionName)
            else:
                shortcuts[actionData.shortcut] = [actionName]

        actions[actionName] = buildAction(actionData)

    # Print all duplicated shortcuts
    for shortcut, actionNames in shortcuts.items():
        if actionNames > 1:
            LogManager().error(f"Duplicated shortcut '{shortcut}' for the following actions: [{', '.join(actionNames)}]")

    return actions

actions = buildAllActions()