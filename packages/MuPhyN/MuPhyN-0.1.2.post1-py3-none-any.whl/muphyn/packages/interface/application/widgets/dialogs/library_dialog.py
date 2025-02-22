#-----------------------------------
# Imports
#-----------------------------------


import os
from typing import List, Any

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QAbstractItemView, QFileDialog, QListWidgetItem, QVBoxLayout, QGridLayout

from muphyn.packages.core.application import BoxesLibrariesManager, SchedulersLibrariesManager
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import PlainButton, TitlePropertyLabel

from ...actions.graphicalactions.library_dialog_remove_action import LibraryDialogRemoveAction
from ...actions.graphicalactions.library_dialog_add_action import LibraryDialogAddAction, _lst_contains_element
from ...holders.actions_holder import ActionsHolder
from .abstract_dialog import AbstractDialog

from muphyn.utils.paths import ROOT_DIR

#-----------------------------------
# Class
#-----------------------------------

class LibraryDialog (AbstractDialog) :
    """Est la classe permettant d'afficher une boîte de dialogue capable de modifier les bibliothèques des boxes et des solveurs."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any) :
        AbstractDialog.__init__(self, dialog_holder, 'library', 'Libraries')
        
        self._actions_holder = ActionsHolder()
        self.setMinimumSize(480, 360)
        self.resize(640, 480)
        self._init_ui()
        self._lst_libraries_selection_changed_event()

        self._boxes_at_start : List[str] = []
        self._solvers_at_start : List[str] = []

        for library_element in BoxesLibrariesManager().libraries :
            self._boxes_at_start.append(library_element.path)
            if not _lst_contains_element(self._lst_libraries, library_element.path) :
                QListWidgetItem(library_element.path, self._lst_libraries)

        for library_element in SchedulersLibrariesManager().libraries :
            self._solvers_at_start.append(library_element.path)
            if not _lst_contains_element(self._lst_libraries, library_element.path) :
                QListWidgetItem(library_element.path, self._lst_libraries)

        
    # -------------
    # Methods
    # -------------

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(event)

        if event.modifiers() == QtCore.Qt.KeyboardModifier.ControlModifier:

            if event.key() == QtCore.Qt.Key.Key_Z :
                self._actions_holder.undo()

            elif event.key() == QtCore.Qt.Key.Key_Y :
                self._actions_holder.redo()

        elif event.modifiers() == QtCore.Qt.KeyboardModifier.NoModifier :

            if event.key() == QtCore.Qt.Key.Key_Delete :

                if self._lst_libraries.hasFocus():
                    self._remove_method()

    def _init_ui (self) -> None :
        """
        Est la méthode appelée pour déssiner l'interface de la boîte de dialogue
        capable d'afficher l'interface de la boîte de dialogue.
        """

        # Init main Layout
        mainLayout = QVBoxLayout()

        # Init Options Layout
        optionsLayout = QGridLayout()
        optionsLayout.setColumnMinimumWidth(1, 45)
        optionsLayout.setColumnMinimumWidth(2, 45)
        optionsLayout.setSpacing(5)

        # Init Buttons Layout
        buttonsLayout = QGridLayout()
        buttonsLayout.setColumnMinimumWidth(1, 90)
        buttonsLayout.setColumnMinimumWidth(2, 90)
        buttonsLayout.setHorizontalSpacing(5)

        # Library list title
        self._lbl_libraries = TitlePropertyLabel()
        self._lbl_libraries.setObjectName("_lbl_libraries")

        # Add Path Field Text Content to list as Item
        self._add_button = PlainButton()
        self._add_button.setObjectName("_add_button")
        self._add_button.clicked.connect(self._search_method)

        # Remove Item From List Button
        self._remove_button = QtWidgets.QPushButton()
        self._remove_button.setObjectName("_remove_button")
        self._remove_button.clicked.connect(self._remove_method)

        # List of all library pathes
        self._lst_libraries = QtWidgets.QListWidget()
        self._lst_libraries.setObjectName("_lst_libraries")
        self._lst_libraries.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self._lst_libraries.itemSelectionChanged.connect(self._lst_libraries_selection_changed_event)

        # Confirm Button (Update Boxes List)
        self._accept_button = PlainButton()
        self._accept_button.setObjectName("_accept_button")
        self._accept_button.clicked.connect(self._accept_method)

        # Cancel button (just close the library dialog and restore old library list)
        self._cancel_button = QtWidgets.QPushButton()
        self._cancel_button.setObjectName("_cancel_button")
        self._cancel_button.clicked.connect(self._cancel_method)

        # Adding options widget to layout
        optionsLayout.addWidget(self._lbl_libraries, 0, 0)
        optionsLayout.addWidget(self._add_button, 0, 1)
        optionsLayout.addWidget(self._remove_button, 0, 2)
        optionsLayout.addWidget(self._lst_libraries, 1, 0, 1, 3)
        optionsLayout.setRowStretch(1, 1)
        optionsLayout.setColumnStretch(0, 1)

        # Closing action layout
        buttonsLayout.addWidget(self._accept_button, 0, 1)
        buttonsLayout.addWidget(self._cancel_button, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Main Layout
        mainLayout.addItem(optionsLayout)
        mainLayout.addItem(buttonsLayout)
        mainLayout.setSpacing(10)

        # Add Layout to file dialog
        self.setLayout(mainLayout)

        self._retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslate_ui (self, Dialog) -> None :
        _translate = QtCore.QCoreApplication.translate

        self._add_button.setText(_translate("Dialog", "+"))
        self._remove_button.setText(_translate("Dialog", "-"))
        self._accept_button.setText(_translate("Dialog", "Apply"))
        self._cancel_button.setText(_translate("Dialog", "Cancel"))
        self._lbl_libraries.setText(_translate("Dialog", "Libraries"))

    @pyqtSlot()
    def _search_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur veut faire une recherche."""
        path = QFileDialog.getExistingDirectory(self, "Select Libraries Folder", ROOT_DIR)

        if path is None or path == '':
            return
        
        self._addLibrary(path)

    @pyqtSlot()
    def _addLibrary (self, path: str) -> None :
        """Est la méthode appelée pour ajouter un élément dans la liste."""

        if _lst_contains_element(self._lst_libraries, path):
            return

        library_action = LibraryDialogAddAction(self._lst_libraries, path)
        library_action.do()
        self._actions_holder.append(library_action)

    @pyqtSlot()
    def _remove_method (self) -> None :
        """Est la méthode appelée pour supprimer un élément de la liste."""
        
        selected_items : List[str] = []

        for selected_item in self._lst_libraries.selectedItems() :
            selected_items.append(selected_item.text())

        library_action = LibraryDialogRemoveAction(self._lst_libraries, selected_items)
        library_action.do()
        self._actions_holder.append(library_action)

    @pyqtSlot()
    def _accept_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur accepte les modifications apportées."""
        
        BoxesLibrariesManager().clear()
        SchedulersLibrariesManager().clear()

        for i in range(self._lst_libraries.count()) :
            path : str = self._lst_libraries.item(i).text()

            LogManager().debug(f"Adding \"{path}\"...")

            BoxesLibrariesManager().add_library(path)
            SchedulersLibrariesManager().add_library(path)

        
        BoxesLibrariesManager().load_libraries()
        SchedulersLibrariesManager().load_libraries()

        # If error while loading box libraries
        if len(BoxesLibrariesManager().importErrors):
            self._dialog_holder.show_dialog(
                "errors_dialog", True,
                errorMessage = '\n'.join([str(boxLibrariesImportError) for boxLibrariesImportError in BoxesLibrariesManager().importErrors]), 
            )

        # If error while loading scheduler libraries
        if len(SchedulersLibrariesManager().importErrors):
            self._dialog_holder.show_dialog(
                "errors_dialog", True,
                errorMessage = '\n'.join([str(schedulerLibrariesImportError) for schedulerLibrariesImportError in SchedulersLibrariesManager().importErrors])
            )

        self.close()

    @pyqtSlot()
    def _cancel_method (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur annulle les modifications apportées."""
        self.close()

    @pyqtSlot()
    def _lst_libraries_selection_changed_event (self) -> None :
        """Est la méthode appelée lorsque la sélection des bibliothèque change."""
        self._remove_button.setEnabled(self._lst_libraries.selectedItems().__len__() > 0)