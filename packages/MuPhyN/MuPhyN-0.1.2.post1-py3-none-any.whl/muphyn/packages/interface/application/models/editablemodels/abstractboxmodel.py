#-----------------------------------
# Imports
#-----------------------------------

from datetime import date
from typing import Iterable, List, Any, Dict

from .abstracteditablemodel import AbstractEditableModel
from ..graphicalmodels.boxmodel.boxinputmodel import BoxInputModel
from ..graphicalmodels.boxmodel.boxoutputmodel import BoxOutputModel

#-----------------------------------
# Class
#-----------------------------------

class AbstractBoxModel (AbstractEditableModel) : 
    """Est la classe abstraite commune aux classes capables de garder les informations de bases des boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, path : str, creator : str, date_creation : date, version : float, inputs : Iterable[BoxInputModel] = [], outputs : Iterable[BoxOutputModel] = [], properties : Dict[str, Any] = {}) :
        
        AbstractEditableModel.__init__(self, name, path, creator, date_creation, version)

        self._inputs : List[BoxInputModel] = list(inputs)
        self._outputs : List[BoxOutputModel] = list(outputs)
        self._properties : Dict[str, Any] = {}

    # -------------
    # Properties
    # -------------

    @property
    def inputs (self) -> Iterable[BoxInputModel] :
        """Permet de récuperer la liste des entrées."""
        return self._inputs

    @property
    def outputs (self) -> Iterable[BoxOutputModel] :
        """Permet de récuperer la liste des sorties."""
        return self._outputs