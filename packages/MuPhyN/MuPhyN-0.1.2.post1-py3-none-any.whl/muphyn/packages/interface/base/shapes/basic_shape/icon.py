#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import os
from typing import Union

# PyQt6 Imports
from PyQt6.QtCore import QPointF, QSize, QSizeF, Qt
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QGraphicsItem

# Project Imports
from muphyn.packages.interface.application.utils.constants import MuphynFonts
from .grouped_shapes import GroupedShapes
from .shapes import Text
from .image_shapes import ImageShapeFactory, AbstractImage

class Icon(GroupedShapes):
    def __init__(self, icon: Union[str, QImage], description: str = None, position: QPointF = QPointF(), 
            size: QSizeF = None, parent: QGraphicsItem = None) -> None:

        # Init parent class
        super().__init__(position, parent)

        if isinstance(icon, QImage):
            self.imageShape: AbstractImage = ImageShapeFactory(icon, position=position, size=size, parent=self)
        
        elif isinstance(icon, str) and os.path.exists(icon):
            # Icon path
            self.iconPath = icon

            # Build icon shape
            self.imageShape: AbstractImage = ImageShapeFactory(icon, position=position, size=size, parent=self)

        else:
            # Handle description
            if description is None :
                if type(icon) == str:
                    self.description = os.path.basename(icon)
                else:
                    self.description = "icon"

            # Build text flag
            alignementFlag = Qt.AlignmentFlag.AlignVCenter

            # Build Text shape
            self.textShape = Text(self.description, position=QPointF(), 
                font=MuphynFonts.BoxModelDetailsFont, alignment=alignementFlag, parent=self)

    def setWidth(self, new_width: int) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setWidth(new_width)
        else:
            # Resize text area
            pass

    def setHeight(self, new_height: QSizeF) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setHeight(new_height)
        else:
            # Resize text area
            pass

    def setSize(self, new_size: Union[QSize, QSizeF]) -> None:
        if hasattr(self, "imageShape"):
            self.imageShape.setSize(new_size)
        else:
            # Resize text area
            pass


