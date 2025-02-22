# General import
from typing import Optional, Union

# PyQt import
from PyQt6.QtWidgets import QWidget

# Project import
from muphyn.packages.interface.base import DrawingWidget
from muphyn.packages.core.base import LogManager
from simulation.interface.multiphysicsmodel.components import AbstractComponentModel
from simulation.interface.multiphysicsmodel.connectionmodel import ConnectionModel

class AbstractMultiPhysicsModel(DrawingWidget):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.components: list[AbstractComponentModel] = []
        self.links: list[ConnectionModel] = []

    def addItem(self, newItem: Union[AbstractComponentModel, ConnectionModel]):
        if isinstance(newItem, AbstractComponentModel):
            # Test if already added to avoid duplicated item in the scene
            if newItem not in self.components:
                # Add item to list
                self.components.append(newItem)

                # Add item to scene
                self.scene.addItem(newItem)
            else:
                LogManager.debug("Component already added")

        elif isinstance(newItem, ConnectionModel):
            # Test if already added to avoid duplicated item in the scene
            if newItem not in self.links:
                # Add item to list
                self.links.append(newItem)

                # Add item to scene
                self.scene.addItem(newItem)
            else:
                LogManager.debug("Connection already added")
        else:
            raise(TypeError(f"AbstractMultiPhysicsModel.addItems(): newItem is not a AbstractComponentModel → {type(newItem)}"))

        
        