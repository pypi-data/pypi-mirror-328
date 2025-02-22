#-----------------------------------
# Imports
#-----------------------------------

from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QSlider, QWidget

#-----------------------------------
# Class
#-----------------------------------

class RotationSlider (QSlider) :
    """Est l'élément graphique qui permet de modifier l'angle d'un élément graphique."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, parent : QWidget = None) :
        super().__init__(parent)

        self.setMaximum(270)
        self.setMinimum(0)
        self.setTickInterval(90)
        self.setSingleStep(90)

    # -------------
    # Methods
    # -------------

    def change_value (self, pos_x : float) :
        old_value = (pos_x / self.geometry().width()) * (self.maximum() - self.minimum())
        value = 0

        if old_value < 45 :
            value = 0

        elif old_value < 135 :
            value = 90

        elif old_value < 225 :
            value = 180 

        else :
            value = 270

        self.setValue(int(value))

    def mousePressEvent (self, event : QMouseEvent) -> None :
        self.change_value(event.pos().x())
        event.accept()

    def mouseMoveEvent (self, event : QMouseEvent) -> None :
        self.change_value(event.pos().x())
        event.accept()

    def setValue (self, rotation) -> None :

        if isinstance(rotation, float) :
            super().setValue(int(rotation))

        elif isinstance(rotation, int) :
            super().setValue(rotation)