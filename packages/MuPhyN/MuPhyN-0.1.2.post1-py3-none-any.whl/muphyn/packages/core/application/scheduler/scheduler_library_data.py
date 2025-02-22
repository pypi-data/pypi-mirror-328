#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, Any, List

from ..parameter.plci_core_parameter import Parameter

from .plci_core_scheduler import Scheduler
from .plci_core_scheduler_exception import SchedulerException

#-----------------------------------
# Class
#-----------------------------------

class SchedulerData : 
    """Est la classe commune des classes de données de bibliothèque."""

    # -------------
    # Constructors
    # -------------
    def __init__ (
            self,
            path: str,
            scheduler_name : str, 
            scheduler_library : str,
            scheduler_method : Callable[[Scheduler], SchedulerException],
            creator : str,
            date_created : Any,
            version : float,
            parameters: List[Parameter]
        ) :
        
        self._path: str = path
        self._scheduler_name : str = scheduler_name
        self._scheduler_library : str = scheduler_library
        self._scheduler_method : Callable[[Scheduler], SchedulerException] = scheduler_method
        self._creator = creator
        self._dateCreated = date_created
        self._version = version
        self._parameters = parameters

    # -------------
    # Properties
    # -------------
    @property
    def path(self) -> str:
        return self._path

    @property 
    def completeName (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return f"{self._scheduler_library}.{self._scheduler_name}"
    
    @property 
    def scheduler_name (self) -> str :
        """Permet de récuperer le nom du planificateur."""
        return self._scheduler_name

    @property
    def scheduler_library (self) -> str :
        """Pemet de récuperer la bibliothèque du planificateur."""
        return self._scheduler_library

    @property
    def scheduler_method (self) -> Callable[[Scheduler], SchedulerException] :
        """Permet de récuperer la méthode du planificateur."""
        return self._scheduler_method

    @property
    def creator (self) -> str :
        """Permet de récuperer le nom de la personne qui a créé le planificateur."""
        return self._creator

    @property
    def date_created (self) -> Any :
        """Permet de récuperer la date à laquelle le planificateur a été créée."""
        return self._dateCreated

    @property
    def version (self) -> float :
        """Permet de récuperer la version du planificateur."""
        return self.version
    
    @property
    def parameters(self) -> List[Parameter]:
        return self._parameters

    # -------------
    # Methods
    # -------------
    
    def construct_scheduler (self) -> Scheduler :
        """Permet de générer un planificateur."""
        return Scheduler(self._scheduler_name, self._scheduler_method)

    def __str__ (self) -> str :
        """Permet de récuperer l'importeur de planificateur sous la forme de texte."""
        return self._scheduler_library + '.' + self._scheduler_name