#-----------------------------------
# Imports
#-----------------------------------
from os import path
from typing import List, Any, Dict

from muphyn.packages.core.base import ManagerMetaClass, LogManager
from muphyn.utils.paths import ROOT_DIR

from .plci_core_box import Box
from .box_library_data import AbstractBoxData
from ..data.plci_core_data_type import DataType
from ..diagram.plci_core_diagram import Diagram
from ..importers.box.abstract_box_library_importer import AbstractBoxLibraryImporter
from ..importers.box.box_library_importer_1_1_0 import BoxLibraryImporter
from ..libraries.abstractlibrariesmanager import LibraryImportError, AbstractLibraryItem

#-----------------------------------
# Classes
#-----------------------------------
class BoxLibraryItem(AbstractLibraryItem) : 
    """Est la classe qui permet de stocker les éléments de bibliothèque dans la classe boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, path : str) :
        super().__init__(path)
        self._boxes : Dict[str, AbstractBoxData] = {}

    # -------------
    # Properties
    # -------------
    @property
    def boxes (self) -> Dict[str, AbstractBoxData] :
        """Permet de récuperer le dictionnaire des nom de bibliothèque et leur éléments de création de boxes."""
        return self._boxes

    # -------------
    # Methods
    # -------------
    def _loadItem(self, box_importer: AbstractBoxLibraryImporter, fileName: str) -> LibraryImportError:
        # Build absolute yaml file path
        absolute_yaml_file = self.path + '/' + fileName + '.yaml'
        
        imported_box_data = box_importer.import_box(self.path, fileName, absolute_yaml_file, self._boxes)

        if imported_box_data is None : 
            return

        if imported_box_data['box_data'] is None :
            return

        self._boxes[imported_box_data['library_name']] = imported_box_data['box_data']

class BoxesLibrariesManager(metaclass=ManagerMetaClass) :
    """Est la classe qui permet de construire les boxes.""" 

    BoxIndex = 0
    DefaultLibraries: List[str] = [
        ROOT_DIR + "/libraries/box_library",
        ROOT_DIR + "/libraries/scheduler_library"
    ]

    # -------------
    # Constructors
    # -------------
    def __init__ (self) :
        self._libraries : List[BoxLibraryItem] = []
        self._current_box_index = 0
        self._boxImporter = BoxLibraryImporter()
        self._importErrors: List[LibraryImportError] = []

        # Init default libraries list
        self._addDefaultLibraries()
    
    # -------------
    # Properties
    # -------------

    @property
    def libraries (self) -> List[BoxLibraryItem] :
        """Permet de retourner la liste des libraries."""
        return self._libraries

    @property 
    def box_importer (self) -> AbstractBoxLibraryImporter :
        """Permet de retourner l'importeur utilisé pour importer des boxes."""
        return self._boxImporter

    @property
    def boxes (self) -> List[AbstractBoxData] :
        """Permet de retourner l'intégralité des boxes importées."""

        for library in self._libraries :
            for box_name in library.boxes :
                yield library.boxes[box_name]

    @property
    def importErrors(self) -> List[LibraryImportError]:
        return self._importErrors

    # -------------
    # Methods
    # -------------
    def _addDefaultLibraries(self):
        for library in BoxesLibrariesManager.DefaultLibraries:
            self.add_library(library)
        
    def _name_library (self, box_library : str, box_name : str) -> str :
        """Permet de rassembler le nom et la libraire en un seul string."""
        return box_library + "." + box_name

    def add_library (self, libraryFolder : str) -> bool :
        """Permet d'ajouter une bibliothèque dans le répertoire des bibliothèque."""
        
        # Test if libraryFolder path format is string 
        if not (isinstance(libraryFolder, str)) :
            LogManager().error(f"Wrong path variable format {type(libraryFolder)} instead of str", is_global_message=True)
            return False

        # Test if library folder path exists
        if not path.exists(libraryFolder):
            LogManager().error(f"Library Path doesn't exists: {libraryFolder}", is_global_message=True)
            return False

        # Check if library has already been added
        if any(libraryElement.path == libraryFolder for libraryElement in self._libraries):
            LogManager().error(f"Library Folder already added: {libraryFolder}", is_global_message=True)
            return False
        
        # Append Scheduler Library
        self._libraries.append(BoxLibraryItem(libraryFolder))

        # Increase box index
        BoxesLibrariesManager.BoxIndex += 1

        return True

    def load_libraries (self) -> list :
        """Permet de charger toutes les bibliothèques du répertoire."""


        # Load all libraries
        for libraryElement in self._libraries :
            if not libraryElement.loaded:
                errors = libraryElement.loadLibrary(self.box_importer)
                if not errors.isEmpty():
                    self._importErrors.append(errors)


    def construct_box (self, box_library : str, box_name : str, **box_params) -> Any:
        """Permet de construire une box suivant son nom et sa librairie."""

        if not (isinstance(box_library, str) and isinstance(box_name, str)) :
            return None

        box_access = self._name_library(box_library, box_name)

        for libraryElement in self._libraries :
            
            if box_access in libraryElement.boxes :
                box = libraryElement.boxes[box_access].construct_box(self._current_box_index, box_params, self)
                
                if isinstance(box, Diagram) :
                    self._current_box_index = box._boxes[box._boxes.__len__() - 1].index + 1

                elif isinstance(box, Box) :
                    self._current_box_index += 1

                return box

    def get_required_params (self, box_library : str, box_name : str) -> Dict[str, DataType] :
        """Permet de retourner les paramètres nécessaires pour instancier une box dans une bibliothèque."""

        if not (isinstance(box_library, str) and isinstance(box_name, str)) :
            return None

        box_access = self._name_library(box_library, box_name)

        for libraryElement in self._libraries :
            
            if box_access in libraryElement.boxes :
                boxElement = libraryElement.boxes[box_access]
                return boxElement.params

        return None

    def clear (self) -> None :
        """Permet d'éffacer le contenu des boxes chargées."""
        for libraryElement in self._libraries :

            libraryElement.boxes.clear()
            del libraryElement
        
        del self._libraries
        self._libraries : List[BoxLibraryItem] = []

    def get_box_data (self, box_library : str, box_name : str) -> AbstractBoxData : 
        """Permet de récuperer les données de construction d'une box en fonction de sa bibliothèque et de son nom."""

        for box_data in self.boxes :

            if box_data.box_library == box_library and box_data.box_name == box_name :
                return box_data

        return None