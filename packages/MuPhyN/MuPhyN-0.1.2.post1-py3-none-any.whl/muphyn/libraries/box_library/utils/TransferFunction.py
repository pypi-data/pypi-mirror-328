# -----------------------------------
# Imports
# -----------------------------------
from __future__ import annotations
import numbers
import re
import numpy as np
import matplotlib.pyplot as plt

from typing import Any, List, Union
from scipy.integrate import solve_ivp, RK45

DotFloatRegex = r"[-+]?[0-9]+\.[0-9]*|\.[0-9]+|[0-9]+"
DotScientificNumberRegex = r"[-+]?[1-9](?:\.\d+)?[Ee][-+]?\d+"

def isDotFloat(value: str) -> bool:
    return re.match(DotFloatRegex, value) is not None or re.match(DotScientificNumberRegex, value)

def findAll(value: str, pattern: Union[str, List[str]]) -> List[str]:
    if type(pattern) == list:
        pattern = '|'.join(pattern)
    return re.findall(pattern, value)

class TransferFunction:

    def __init__(self, numCoeffs: List[float], denomCoeffs: List[float], initialValue: float = 0.0, time: float = 10.0, stepTime: float = 0.1) -> None:
        assert type(numCoeffs) == list, ("Please provide a list of float values as numCoeffs")
        assert type(denomCoeffs) == list, ("Please provide a list of float values as denomCoeffs")
        assert isinstance(initialValue, numbers.Real), ("Please provide a float value as initialValue")

        self._targetValue = 1

        # General value
        self._numCoeffs = numCoeffs
        self._numOrder = len(numCoeffs) - 1

        self._denomCoeffs = denomCoeffs
        self._denomOrder = len(denomCoeffs) - 1

        self._initialValue = initialValue
        
        self._time = time
        self._stepTime = stepTime

        # Process values
        self._lastY = [self._initialValue] + [0.0] * (self._denomOrder - 1)
        self._lastTime = -1

        # Init solver
        self._interpolants = []
        t_eval = (0, time)
        t0, tf = map(float, t_eval)
        t_eval = np.asarray(t_eval)
        if t_eval.ndim != 1:
            raise ValueError("`t_eval` must be 1-dimensional.")

        if np.any(t_eval < min(t0, tf)) or np.any(t_eval > max(t0, tf)):
            raise ValueError("Values in `t_eval` are not within `t_span`.")

        d = np.diff(t_eval)
        if tf > t0 and np.any(d <= 0) or tf < t0 and np.any(d >= 0):
            raise ValueError("Values in `t_eval` are not properly sorted.")

        self._solver = RK45(self.f, 0, self._lastY, t_bound = tf, max_step=self._stepTime)

    @property
    def lastTime(self) -> float:
        return self._lastTime
    
    @lastTime.setter
    def lastTime(self, newLastTime: float):
        if self._lastTime != newLastTime:
            self._lastTime = newLastTime

    @property
    def lastY(self) -> float:
        return self._lastY
    
    @lastY.setter
    def lastY(self, newLastY: float):
        if self._lastY != newLastY:
            self._lastY = newLastY

    @property
    def time(self) -> float:
        return self._time
    
    @time.setter
    def time(self, newTime: float):
        if self._time != newTime:
            self._time = newTime

    @property
    def stepTime(self) -> float:
        return self._stepTime
    
    @stepTime.setter
    def stepTime(self, newStepTime: float):
        if self._stepTime != newStepTime:
            self._stepTime = newStepTime
    
    @property
    def isFinished(self) -> bool:
        return self._solver.status == "finished"
    
    @property
    def hasFailed(self) -> bool:
        return self._solver.status == "failed"
    
    @property
    def canRun(self) -> bool:
        return not self.isFinished and not self.hasFailed

    def f(self, t, y):
        # Closed loop
        value = self._targetValue

        # Init out value
        out = self._numCoeffs[0] * value

        for j, coeff_y  in enumerate(self._denomCoeffs[:-1]):
            out -= coeff_y * y[j]
        
        for j, coeff_y in enumerate(self._numCoeffs[1:]):
            out += coeff_y * y[j+1]
        
        out_vector = [y[self._denomOrder - 1 - x] for x in range(self._denomOrder)]
        out_vector[-1] = out/self._denomCoeffs[-1]

        return out_vector
    
    def getValue(self, timing: float) -> float:
        return self._solver.dense_output()(timing)[0]
    
    def solve(self) -> List[float]:
        timings = (0, self._time)
        sol = solve_ivp(self.f, timings, self.lastY, t_eval=np.arange(*timings, self._stepTime))

        self._lastSolution = sol
        return sol
    
    def stepSolve(self, setPoint: float = None):
        # Update 
        if setPoint is not None:
            self._targetValue = setPoint

        # Solve point
        solver: RK45 = self._solver

        # Make step
        solver.step()

        # Check status
        status = 0
        if solver.status == 'finished':
            status = 1
        elif solver.status == 'failed':
            status = -1

        self._lastTime = solver.t
        
        return status, solver.t, solver.y[0]

    def __str__(self):
        pass

    @staticmethod
    def coefFromString(coefficientsVectorString: str) -> List[float]:

        if coefficientsVectorString is None or coefficientsVectorString == "":
            return [0]
        else:
            coeffs = [float(val) for val in findAll(coefficientsVectorString, DotFloatRegex)]
            coeffs.reverse()
            return coeffs
        
    @staticmethod
    def equationStringFromCoeffs(coeffs: List[float]):
        return" + ".join(reversed([(f"{coeff} s^{degree}" if degree > 1 else f"{coeff} s" if degree > 0 else f"{coeff}") for degree, coeff in enumerate(coeffs)]))
        
    @staticmethod
    def fromString(numString: str, denomString: str, initialValue: Any = 0.0, time: float = 10.0, stepTime: float = 0.1) -> TransferFunction:
        numCoeffs = TransferFunction.coefFromString(numString)
        denomCoeffs = TransferFunction.coefFromString(denomString)

        return TransferFunction(numCoeffs, denomCoeffs, initialValue, time, stepTime)

# -----------------------------------
# Functions
# -----------------------------------
if __name__ == "__main__":
    import time


    setPoint = 2
    initialValue = 0

    transferFunction = TransferFunction.fromString(" 5 ", "300 40 1", initialValue=initialValue, time=300.0, stepTime=0.003)
    transferFunction._targetValue = setPoint

    startTime = time.time()
    
    sol = []

    status = 0
    lastValue = initialValue
    while status == 0:
        targetValue = setPoint - lastValue
        status, time_, value = transferFunction.stepSolve(targetValue)
        sol.append([time_, value])
        lastValue = value

    print(time.time() - startTime)


    sol = np.array(sol)

    print(sol.shape)

    # Plot the result
    plt.plot(sol[:, 0], sol[:, 1])
    plt.show()
