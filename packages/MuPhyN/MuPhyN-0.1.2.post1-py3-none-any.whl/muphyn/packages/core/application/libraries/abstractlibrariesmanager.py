import os
import traceback
from dataclasses import dataclass, field
from typing import Any, List

from PyQt6.QtCore import QFileInfo

from muphyn.packages.core.base import ManagerMetaClass, LogManager

@dataclass
class ImportError:
    name: str
    error: Exception

    def __str__(self) -> str:
        return f"""
        \t- Name: {self.name}
        \t- Error: {''.join(traceback.format_exception(self.error))}
        """

@dataclass
class LibraryImportError:
    library: str
    importErrors: List[ImportError] = field(default_factory=list)

    def append(self, importError: ImportError):
        if importError not in self.importErrors:
            self.importErrors.append(importError)

    def isEmpty(self) -> bool:
        return not bool(self.importErrors)

    def __str__(self) -> str:
        count = len(self.importErrors)
        importErrorsString = '\n'.join([str(importError) for importError in self.importErrors])
        return f"""Library: {self.library} {count} fails:
        {importErrorsString}
        """

class AbstractLibraryItem : 
    """Est la classe qui permet de stocker les éléments de bibliothèque dans la classe boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, path : str) :
        self._path = path
        self._loaded = False

    # -------------
    # Properties
    # -------------
    
    @property
    def path (self) -> str : 
        """Permet de récuperer le lien vers le dossier de la bibliothèque de boxes.""" 
        return self._path

    @property
    def loaded (self) -> bool :
        """Permet de récuperer l'état de chargement de la bibliothèque de boxes."""
        return self._loaded

    # -------------
    # Methods
    # -------------

    def _loadItem (self, file_name : str) -> LibraryImportError :
        """Permet de charger la bibliothèque."""
        # Récuperation des fichiers dans le dossier
        raise(NotImplementedError(f"{self.__class__.__name__}.load() not implemented yet!"))
    
    def loadLibrary (self, itemImporter : Any) -> LibraryImportError :
        """Permet de charger la bibliothèque."""
        # Récuperation des fichiers dans le dossier

        libraryImportErrors = LibraryImportError(self.path)
        for current_file in os.listdir(self.path):

            if current_file.endswith('.yaml'):
                # Get base file name
                file_name = QFileInfo(current_file).completeBaseName()
                try:
                    # Load item
                    self._loadItem(itemImporter, file_name)
                    
                except Exception as e: 
                    # Build error object
                    importError = ImportError(file_name, e)
                    libraryImportErrors.append(importError)

        return libraryImportErrors


# class AbstractLibrariesManager(metaclass=ManagerMetaClass) :
#     """Est la classe qui permet de construire les boxes.""" 

#     BoxIndex = 0
#     DefaultLibraries: List[str] = []

#     # -------------
#     # Constructors
#     # -------------
#     def __init__ (self) :
#         self._libraries : List[AbstractLibraryItem] = []
#         self._boxImporter = BoxLibraryImporter()

#         # Init default libraries list
#         self._addDefaultLibraries()
    
#     # -------------
#     # Properties
#     # -------------

#     @property
#     def libraries (self) -> List[AbstractLibraryItem] :
#         """Permet de retourner la liste des libraries."""
#         return self._libraries

#     @property 
#     def box_importer (self) -> AbstractBoxLibraryImporter :
#         """Permet de retourner l'importeur utilisé pour importer des boxes."""
#         return self._boxImporter

#     @property
#     def boxes (self) -> List[AbstractLibraryItem] :
#         """Permet de retourner l'intégralité des boxes importées."""

#         for library in self._libraries :
#             for box_name in library.boxes :
#                 yield library.boxes[box_name]

#     # -------------
#     # Methods
#     # -------------
#     def _addDefaultLibraries(self):
#         for library in BoxesLibrariesManager.DefaultLibraries:
#             self.add_library(library)
        
#     def _name_library (self, box_library : str, box_name : str) -> str :
#         """Permet de rassembler le nom et la libraire en un seul string."""
#         return box_library + "." + box_name

#     def add_library (self, libraryFolder : str) -> bool :
#         """Permet d'ajouter une bibliothèque dans le répertoire des bibliothèque."""
        
#         # Test if libraryFolder path format is string 
#         if not (isinstance(libraryFolder, str)) :
#             LogManager().error(f"Wrong path variable format {type(libraryFolder)} instead of str", is_global_message=True)
#             return False

#         # Test if library folder path exists
#         if not path.exists(libraryFolder):
#             LogManager().error(f"Library Path doesn't exists: {libraryFolder}", is_global_message=True)
#             return False

#         # Check if library has already been added
#         if any(libraryElement.path == libraryFolder for libraryElement in self._libraries):
#             LogManager().error(f"Library Folder already added: {libraryFolder}", is_global_message=True)
#             return False
        
#         # Append Scheduler Library
#         self._libraries.append(BoxLibraryItem(libraryFolder))

#         # Increase box index
#         BoxesLibrariesManager.BoxIndex += 1

#         return True

#     def load_libraries (self) -> list :
#         """Permet de charger toutes les bibliothèques du répertoire."""

#         # Init library errors 
#         libraryErrors = []

#         # Load all libraries
#         for libraryElement in self._libraries :
#             if not libraryElement.loaded:
#                 errors = libraryElement.load(self.box_importer)
#                 if not errors.isEmpty():
#                     libraryErrors.append(errors)

#         return libraryErrors

#     def construct_box (self, box_library : str, box_name : str, **box_params) -> Any:
#         """Permet de construire une box suivant son nom et sa librairie."""

#         if not (isinstance(box_library, str) and isinstance(box_name, str)) :
#             return None

#         box_access = self._name_library(box_library, box_name)

#         for libraryElement in self._libraries :
            
#             if box_access in libraryElement.boxes :
#                 box = libraryElement.boxes[box_access].construct_box(self._current_box_index, box_params, self)
                
#                 if isinstance(box, Diagram) :
#                     self._current_box_index = box._boxes[box._boxes.__len__() - 1].index + 1

#                 elif isinstance(box, Box) :
#                     self._current_box_index += 1

#                 return box

#     def get_required_params (self, box_library : str, box_name : str) -> Dict[str, DataType] :
#         """Permet de retourner les paramètres nécessaires pour instancier une box dans une bibliothèque."""

#         if not (isinstance(box_library, str) and isinstance(box_name, str)) :
#             return None

#         box_access = self._name_library(box_library, box_name)

#         for libraryElement in self._libraries :
            
#             if box_access in libraryElement.boxes :
#                 boxElement = libraryElement.boxes[box_access]
#                 return boxElement.params

#         return None

#     def clear (self) -> None :
#         """Permet d'éffacer le contenu des boxes chargées."""
#         for libraryElement in self._libraries :

#             libraryElement.boxes.clear()
#             del libraryElement
        
#         del self._libraries
#         self._libraries : List[BoxLibraryItem] = []

#     def get_box_data (self, box_library : str, box_name : str) -> AbstractBoxData : 
#         """Permet de récuperer les données de construction d'une box en fonction de sa bibliothèque et de son nom."""

#         for box_data in self.boxes :

#             if box_data.box_library == box_library and box_data.box_name == box_name :
#                 return box_data

#         return None