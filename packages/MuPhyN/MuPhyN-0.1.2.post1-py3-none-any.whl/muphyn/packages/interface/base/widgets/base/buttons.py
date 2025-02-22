import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QWidget

from muphyn.utils.paths import ROOT_DIR
from muphyn.packages.core.base import Enum

class PlainButton(QPushButton):
    pass

class ArrowButton(PlainButton):

    SvgDirectory = "assets\GeneralIcons"
    
    class Direction(Enum):
        Up = "up_arrow.svg"
        Right = "right_arrow.svg"
        Down = "down_arrow.svg"
        Left = "left_arrow.svg"

    def __init__(self, direction: Direction, parent: QWidget = None):
        file = os.path.join(ROOT_DIR, ArrowButton.SvgDirectory, direction.value)
        super().__init__(icon=QIcon(os.path.join(ROOT_DIR, ArrowButton.SvgDirectory, direction.value)), text = "", parent = parent)