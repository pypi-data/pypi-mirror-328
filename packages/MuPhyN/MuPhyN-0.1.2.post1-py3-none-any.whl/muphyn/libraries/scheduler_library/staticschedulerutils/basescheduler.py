

import numpy as np

from typing import Tuple

from staticschedulerutils.abstractscheduler import AbstractScheduler

class BaseScheduler(AbstractScheduler):
    def f(self, t):

        res = {}

        for box in self._orderedBoxes:
            if box.isSource:
                res[str(self._boxes.index(box))] = box.f(t, 0)
            else:
                res[str(self._boxes.index(box))] = box.f(t, [res[str(self._boxes.index(inputBox))] for inputBox in box.inputs])

        return np.array([resValue for resValue in dict(sorted(res.items())).values()])

    def solve(self) -> Tuple[np.ndarray, np.ndarray]:
        # Compile model
        self.compile()

        # Test if compile has been properly done
        if self._orderedBoxes is None:
            raise(ValueError("Model has not been compiled properly"))
        
        # Generate all times
        times = np.arange(self._startTime, self._stopTime, self._stepTime)

        # Calculate all values
        return times, np.array(list(map(self.f, times)))
