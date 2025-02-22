# General import
from typing import Optional

# PyQt imports
from PyQt6.QtCore import QRect,QSize, Qt
from PyQt6.QtGui import QPainter, QWheelEvent, QBrush
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QWidget, QApplication

# Project imports
from .patternbuilder import PatternBuilder

class DrawingScene(QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)

class DrawingView(QGraphicsView):

    def __init__(self, scene: QGraphicsScene, parent):

        super().__init__(scene, parent)

        # General View Parameters
        self.setGeometry(self.geometry())
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        # Init zoom
        self.zoomLevel = 5

    def setSize(self, newSize: QSize) -> None:
        # Update geometry
        self.setGeometry(QRect(self.pos(), newSize))

    def wheelEvent(self, event: QWheelEvent):
        if Qt.KeyboardModifier.ControlModifier == QApplication.keyboardModifiers():
            if  event.angleDelta().y() > 0:
                factor = 1.25
                self.zoomLevel += 1
            else:
                if self.zoomLevel > 0:
                    factor = 0.8
                    self.zoomLevel -= 1

            if self.zoomLevel > 0:
                self.scale(factor, factor)

class DrawingWidget(QWidget):

    def __init__(self, parent: Optional[QWidget] = None) -> None:

        # Widget flag
        super().__init__(parent)

        # Create board scene
        self.scene = DrawingScene(self)

        # Create Board View
        self.view = DrawingView(self.scene, self)

        # Draw background
        self.view.setBackgroundBrush(QBrush(PatternBuilder.buildPixmap(50, PatternBuilder.PatternType.CrossPattern)))

    def setSize(self, newSize: QSize):
        # Set this item size
        self.setGeometry(QRect(self.pos(), newSize))

        # Update view size
        self.view.setSize(newSize)