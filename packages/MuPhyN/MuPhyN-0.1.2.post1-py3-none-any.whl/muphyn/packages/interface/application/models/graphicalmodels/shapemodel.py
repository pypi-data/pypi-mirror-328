#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import typing

# PyQt6 Imports
from PyQt6 import QtGui
from PyQt6.QtCore import QPointF, QSizeF
from PyQt6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget

# Project Imports
from muphyn.packages.core.base import LogManager
from .abstractmoveablegraphicalelement import AbstractMoveableGraphicalElement

#-----------------------------------
# Class
#-----------------------------------

class ShapeModel (AbstractMoveableGraphicalElement) :
    """Est le modèle pour afficher des formes à l'écran."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, position : QPointF, size : QSizeF, rotation : float = 0.0, text : str = '', parent : QGraphicsItem = None) :

        AbstractMoveableGraphicalElement.__init__(self, name, position, size, rotation, text, parent)
    
    # -------------
    # Methods
    # -------------

    def paint (self, painter: QtGui.QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = ...) -> None :

        super().render()

        LogManager().error('Not implemented : Render shape')
