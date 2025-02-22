#-----------------------------------
# Imports
#-----------------------------------

# General Imports
from datetime import date
from typing import Iterable

# Project Imports
from ..graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ..graphicalmodels.boxmodel.boxinputmodel import BoxInputModel
from ..graphicalmodels.boxmodel.boxoutputmodel import BoxOutputModel
from ..graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from .abstractdiagrammodel import AbstractDiagramModel

#-----------------------------------
# Class
#-----------------------------------

class BoxCompositeModel (AbstractBoxModel, AbstractDiagramModel) :
    """Est le modèle pour l'éditeur de box composite."""

    # -------------
    # Constructors
    # -------------

    def __init__(self, name : str, path : str, creator : str, date : date, version : float, inputs : Iterable[BoxInputModel] = [], outputs : Iterable[BoxOutputModel] = [], graphical_elements : Iterable[AbstractGraphicalElement] = []) :
        
        AbstractBoxModel.__init__(self, name, path, creator, date, version, inputs, outputs)
        AbstractDiagramModel.__init__(self, graphical_elements)