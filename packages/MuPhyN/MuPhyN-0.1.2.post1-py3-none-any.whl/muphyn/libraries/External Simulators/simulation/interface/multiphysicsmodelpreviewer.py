from typing import Optional, Union

from PyQt6.QtCore import Qt, QEvent, QRect
from PyQt6.QtGui import QCursor, QGuiApplication
from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout

from simulation.interface.multiphysicsmodel.abstractmultiphysicsmodel import AbstractMultiPhysicsModel

class MultiphysicsModelPreviewer(QDialog):

    # Constants
    DefaultRect = QRect(100, 100, 640, 480)

    def __init__(self, model: AbstractMultiPhysicsModel, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent, Qt.WindowType.Dialog)
        
        # Get Mouse position 
        globalCursorPosition = QCursor.pos()

        # Get current screen 
        screenRect = QGuiApplication.screenAt(globalCursorPosition).availableGeometry()
        appRect = MultiphysicsModelPreviewer.DefaultRect

        # Calculate centered geometry
        offset = screenRect.center() - appRect.center()
        appRect.translate(offset)

        # General Parameters
        self.setMinimumSize(appRect.size())
        self.setGeometry(appRect)

        # 
        self._model = model

    def initUi(self):
        # Init main layout
        mainLayout = QVBoxLayout()

        # Add model previewer
        mainLayout.addWidget(self._model)

        # Set main layout
        self.setLayout(mainLayout)

    def event(self, a0: QEvent) -> bool:
        if a0.type() == QEvent.Type.Resize:
            self.openModelicaModelPreviewer.setSize(self.size())
        return super().event(a0)