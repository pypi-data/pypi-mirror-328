#-----------------------------------
# Imports
#-----------------------------------

#-----------------------------------
# Class
#-----------------------------------
import os
from typing import Dict

from ..models.editablemodels.abstracteditablemodel import AbstractEditableModel
from .dumpndumper import dump, supportedExtensions

class AbstractExporter :
    """Est la classe abstraite commune aux classes capables d'exporter des modèles."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def buildDict(self, model : AbstractEditableModel) -> Dict:
        raise Exception(f"{self.__class__.__name__}.buildDict() is an abstract method and must be overloaded.")

    def save (self, model : AbstractEditableModel, path : str) -> bool :
        # Get extension
        fileExtension = os.path.splitext(path)[-1]

        # Determine if supported extension
        if fileExtension not in supportedExtensions:
            raise(ValueError(f"Not a supported file format '{fileExtension}':\n\t[{', '.join([supportedExtension for supportedExtension in supportedExtensions])}]"))

        # Build exporter dictionnary
        modelDict = self.buildDict(model)

        # Dump model
        dump(modelDict, path, fileExtension)