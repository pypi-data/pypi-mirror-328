#-----------------------------------
# Imports
#-----------------------------------

from datetime import date
from typing import Iterable
from ..graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ..graphicalmodels.boxmodel.boxinputmodel import BoxInputModel
from ..graphicalmodels.boxmodel.boxoutputmodel import BoxOutputModel
from .abstractcodemodel import AbstractCodeModel

#-----------------------------------
# Class
#-----------------------------------

class BoxCodeModel (AbstractBoxModel, AbstractCodeModel) :
    """Est le model des boxes dont le comportement est décrit par du code."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, name : str, path : str, creator : str, date : date, version : float, code : str = '', inputs : Iterable[BoxInputModel] = [], outputs : Iterable[BoxOutputModel] = []) : 
        
        AbstractBoxModel.__init__(self, name, path, creator, date, version, inputs, outputs)
        AbstractCodeModel.__init__(self, code)