#-----------------------------------
# Imports
#-----------------------------------

from typing import Dict

#-----------------------------------
# Class
#-----------------------------------

from ..models.editablemodels.abstracteditablemodel import AbstractEditableModel


class AbstractImporter :
    """Est la classe abstraite capable d'importer des modèles."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def open (self, data : Dict, path : str, name : str) -> AbstractEditableModel :
        """Est la méthode appelée pour ouvrir le modèle éditable."""
        raise Exception("AbstractExporter open is an abstract method and must be overloaded.")