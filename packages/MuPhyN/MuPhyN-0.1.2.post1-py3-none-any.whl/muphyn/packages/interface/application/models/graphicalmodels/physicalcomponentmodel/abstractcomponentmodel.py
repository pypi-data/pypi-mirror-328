

# PyQt6 Imports
from PyQt6.QtCore import QPointF, QSizeF
from PyQt6.QtWidgets import QGraphicsItem

# Project Imports
from ..abstractmoveablegraphicalelement import AbstractMoveableGraphicalElement

class AbstractComponentModel(AbstractMoveableGraphicalElement):

    def __init__(self, name: str, position: QPointF, size: QSizeF, rotation: float = 0.0, 
        text: str = '', parent: QGraphicsItem = None, symbol_path: str = None):

        AbstractMoveableGraphicalElement.__init__(name, position, size, rotation, text, parent)

        self._should_recompute = False
