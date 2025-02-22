#-----------------------------------
# Imports
#-----------------------------------
from typing import Dict

#-----------------------------------
# Class
#-----------------------------------

class SchedulerParams :
    """Est la classe qui permet de maintenir les paramètres de la simulation dans une classe."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, stop_time : float = 10.0, step_time : float = 0.1) :
        self._stop_time = stop_time
        self._step_time = step_time

    # -------------
    # Properties
    # -------------

    @property 
    def step_time (self) -> float : 
        """Permet de récuperer le pas de temps pour la simulation."""
        return self._step_time

    @property 
    def stop_time (self) -> float :
        """Permet de récuperer le temps de fin de simulation."""
        return self._stop_time
    
    # ---------------
    # Methods
    # ---------------
    def toDict(self) -> Dict:
        return {
            "stop_time": self._stop_time,
            "step_time": self._step_time
        }
    
    def __str__(self) -> str:
        return str(self.toDict())

    # ---------------
    # Static methods
    # ---------------
    def fromDict(schedulerParamsDict: Dict) -> "SchedulerParams":
        if all([key in schedulerParamsDict for key in ["stop_time", "step_time"]]):
            try:
                stopTime = float(schedulerParamsDict['stop_time'])
                stepTime = float(schedulerParamsDict['step_time'])
                return SchedulerParams(stopTime, stepTime)
            except:
                return SchedulerParams()
        else:
            return SchedulerParams()