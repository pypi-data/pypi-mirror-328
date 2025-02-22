#-----------------------------------
# Imports
#-----------------------------------
from typing import Dict

from muphyn.packages.core.application import SchedulerParams

#-----------------------------------
# Class
#-----------------------------------

class SchedulerModel :
    """Est le model de données pour l'éditeur des planificateurs."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, library: str, name: str, params: SchedulerParams = SchedulerParams()) :

        self._library : str = library
        self._name : str = name
        self._params = params

    # -------------
    # Properties
    # -------------
    @property
    def completeName(self) -> str:
        return f"{self._library}.{self._name}"
    
    @property
    def library (self) -> str :
        """Permet de récuperer le bibliothèque dans laquelle se trouve le planificateur."""
        return self._library
    
    @library.setter 
    def library (self, library_ : str) -> None :
        """Permet de modifier la bibliothèque dans laquelle se trouve le planificateur."""
        self._library = library_

    @property
    def name (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return self._name
    
    @name.setter
    def name (self, name_ : str) -> None :
        """Permet de modifier le nom du planificateur."""
        self._name = name_

    @property
    def params (self) -> SchedulerParams :
        """Permet de récuperer les paramètres du planificateur."""
        return self._params
    
    @params.setter
    def params (self, params_ : SchedulerParams) -> None :
        """Permet de modifier les paramètres du planificateur."""
        self._params = params_

    # ---------------
    # Methods
    # ---------------
    def toDict(self) -> Dict:
        return {
            "library": self._library,
            "name": self._name,
            "params": self._params.toDict(),
        }
    
    def __str__(self) -> Dict:
        return str(self.toDict())

    # ---------------
    # Static methods
    # ---------------
    @staticmethod
    def default(schedulerParams: SchedulerParams = SchedulerParams()) -> "SchedulerModel":
        return SchedulerModel("Schedulers", "Default", schedulerParams)

    @staticmethod
    def fromDict(schedulerModelDict: Dict) -> "SchedulerModel":
        # Scheduler parameters
        if "parameters" in schedulerModelDict:
            schedulerParams = SchedulerParams.fromDict(schedulerModelDict["parameters"])
        else:
            schedulerParams = SchedulerParams()

        # Scheduler model
        if all([key in schedulerModelDict for key in ["library", "name"]]):
            # Scheduler library & name
            schedulerLibrary = schedulerModelDict['library']
            schedulerName = schedulerModelDict['name']

            return SchedulerModel(schedulerLibrary, schedulerName, schedulerParams)
        else:
            return SchedulerModel.default(schedulerParams)
