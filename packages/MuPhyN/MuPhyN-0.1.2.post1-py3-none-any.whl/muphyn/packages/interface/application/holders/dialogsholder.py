#-----------------------------------
# Imports
#-----------------------------------

from typing import Callable, List, Any

from PyQt6.QtGui import QWindow

from muphyn.packages.core.base import LogManager
from ..userdata import UserData

from ..models.editablemodels.simulationmodel import SimulationModel
from ..widgets.dialogs.abstract_dialog import AbstractDialog
from ..widgets.dialogs.documentation_dialog import DocumentationDialog
from ..widgets.dialogs.errordialog import ErrorDialog
from ..widgets.dialogs.library_dialog import LibraryDialog
from ..widgets.dialogs.new_box_dialog import NewBoxDialog
from ..widgets.dialogs.new_simulation_dialog import NewSimulationDialog
from ..widgets.dialogs.simulation_parameters_dialog import SimulationParametersDialog

#-----------------------------------
# Class
# #-----------------------------------

class DialogsHolder :
    """Est la classe qui permet à une classe de fenêtre principale d'afficher des dialogues."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, main_window : QWindow) :
        self._dialogs : List[AbstractDialog] = []
        self._main_window : QWindow = main_window

        self._dialog_opened_listner : List[Callable[[Any], None]] = []
        self._dialog_closed_listner : List[Callable[[Any, Any], None]] = []
        self._dialog_closed_all_listener : List[Callable[[Any], None]] = []

    # -------------
    # Properties
    # -------------

    @property
    def dialogs (self) -> List[AbstractDialog] :
        """Permet de récuperer la liste des boîtes de dialogues actuellement affichées."""
        return self._dialogs

    @property
    def len (self) -> int :
        """Permet de récuperer le nombre de dialogues actuellement affichées."""
        return self._dialogs.__len__()

    @property
    def main_window (self) -> QWindow :
        """Permet de récuperer la fenêtre principale qui détient le dialog holder"""
        return self._main_window

    @property
    def dialog_opened_listener (self) -> List[Callable[[Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à l'ouverture d'une boite dialogue."""
        return self._dialog_opened_listner

    @property
    def dialog_closed_listener (self) -> List[Callable[[Any, Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à la fermeture d'une boite dialogue."""
        return self._dialog_closed_listner

    @property
    def dialog_closed_all_listener (self) -> List[Callable[[Any], None]] :
        """Permet de récuperer les écouteurs de l'événement appelés à l'ouverture d'une boite dialogue."""
        return self._dialog_closed_all_listener

    # -------------
    # Methods
    # -------------

    def _dialog_closed (self, dialog : AbstractDialog, answer : Any) -> None :
        """Est la méthode appelée par les boite de dialogue quand elle sont fermées."""
        
        if dialog in self._dialogs: 

            self._dialogs.remove(dialog)

            for dialog_listener in self._dialog_closed_listner :
                dialog_listener(dialog, answer)

    def __len__ (self) -> int :
        """Permet de récuperer le nombre de dialogues actuellement affichées."""
        return self._dialogs.__len__()

    def show_dialog (self, name : str, modal : bool, **kwargs) -> None : 
        """Permet d'afficher une nouvelle boite de dialogue."""
        
        dialog = None

        if name == 'library' :
            dialog = LibraryDialog(self)

        elif name == 'about' :
            LogManager().error('Not implemented : show about dialog')

        elif name == 'documentation' :
            if 'libraryItemPath' in kwargs:
                dialog = DocumentationDialog(self, libraryItemPath=kwargs['libraryItemPath'])
            
        elif name == 'new_simulation' : 
            dialog = NewSimulationDialog(self)

        elif name == 'new_box' :
            if 'user_data' in kwargs and isinstance(kwargs['user_data'], UserData):
                dialog = NewBoxDialog(self, kwargs['user_data'])

        elif name == 'new_scheduler' :

            LogManager().error('Not implemented : show new scheduler dialog')
            """if 'user_data' in kwargs :

                if isinstance(kwargs['user_data'], UserData) :
                    
                    dialog = NewSchedulerDialog(self, kwargs['user_data'])
            """

        elif name == 'simulation_parameters_dialog' : 
            if 'current_simulation' in kwargs: 
                if isinstance(kwargs['current_simulation'], SimulationModel):
                    dialog = SimulationParametersDialog(self, kwargs['current_simulation'])

        elif name == 'errors_dialog' : 
            if 'errorMessage' in kwargs: 
                if isinstance(kwargs['errorMessage'], str):
                    dialog = ErrorDialog(self, errorMessage = kwargs['errorMessage'])


        if dialog is None: 
            return

        dialog.setModal(modal)

        self._dialogs.append(dialog)
        for dialog_listener in self._dialog_opened_listner :
            dialog_listener(dialog)

        if modal :
            self._dialog_closed(dialog, dialog.exec())
        else :
            dialog.show()

    def close_all (self) -> None :
        """Permet de fermer toutes les boite de dialogue."""

        for dialog in self._dialogs :
            dialog.close()

        for dialog_listener in self._dialog_closed_all_listener:
            dialog_listener(self)