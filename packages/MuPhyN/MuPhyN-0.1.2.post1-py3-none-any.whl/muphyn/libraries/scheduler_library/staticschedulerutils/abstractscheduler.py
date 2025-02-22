import numpy as np
from typing import Dict, List, Optional, Tuple

from muphyn.packages.core.application.box.plci_core_box import Box

class AbstractScheduler:

    def __init__(self, stopTime: float = 10.0, stepTime: float = 0.001):

        # Simulation parameters
        self._startTime = 0.0
        self._stopTime = stopTime
        self._stepTime = stepTime

        # Initial value
        self._initValue = 0.0

        self._boxes: List[Box] = []
        self._orderedBoxes: Optional[List[Box]] = None

        self._connections: Dict[Box, List[Box]] = {}

    @property
    def startTime(self) -> float:
        return self._startTime

    @property
    def stoptTime(self) -> float:
        return self._stopTime

    @property
    def timeSpan(self) -> float:
        return (self._startTime, self._stopTime)

    @property
    def initValue(self) -> float:
        return self._initValue
    
    def addBox(self, box: Box):
        if isinstance(box, Box):
            self._boxes.append(box)
        else:
            raise(TypeError(f"Wrong type for box object: {type(box)} is not an instance of Box"))
        
    def addConnection(self, fromBox: Box, toBox: Box):
        if not toBox in self._connections:
            self._connections[toBox] = [fromBox]
        else:
            self._connections[toBox].append(fromBox)

        toBox.addInputBox(fromBox)

    def buildOrderedBoxes(self):
        # Init box order list
        orderedBoxes = [box for box in self._boxes if box.isSource]

        # Connect other boxes
        boxes = [box for box in self._boxes]
        oldSize = len(boxes)

        # Remove source boxes from temp boxes list
        for box in orderedBoxes:
            # Pop box
            boxes.remove(box)
            
        while oldSize > len(boxes):
            oldSize = len(boxes)
            for box in boxes:

                # Check if box has been already added in ordered
                if box in orderedBoxes:
                    boxes.remove(box)

                # Check if all inputBox are already in 
                if all([inputBox in orderedBoxes for inputBox in box.inputs]):
                    # Remove box from temp boxes list
                    boxes.remove(box)

                    # Add box in ordered boxes list
                    orderedBoxes.append(box)
                    

        self._orderedBoxes = orderedBoxes

    def compile(self):
        # Compile scheme to get ordered boxes
        self.buildOrderedBoxes()

    def solve(self) -> Tuple[np.ndarray, np.ndarray]:
        raise(NotImplementedError(f"{self.__class__.__name__}.solve not implemented yet!"))