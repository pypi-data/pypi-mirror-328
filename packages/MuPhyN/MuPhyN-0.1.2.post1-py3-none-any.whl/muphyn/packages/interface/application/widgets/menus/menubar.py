

from PyQt6.QtWidgets import QMenuBar, QWidget
from PyQt6.QtGui import QKeySequence, QAction

from muphyn.packages.interface.application.actions import *


class MenuBar(QMenuBar):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def _initActions (self) -> None :
        """Permet de créer les actions que la fenêtres peut réaliser."""

        # File
        self._fileNewSimulationAction = QAction('&Simulation', self)
        self._fileNewSimulationAction.setShortcut(QKeySequence('Ctrl+N'))

        self._fileNewBoxAction = QAction('&Box', self)
        self._fileNewBoxAction.setShortcut(QKeySequence('Ctrl+Shift+N'))

        self._fileNewSolverAction = QAction('Sche&duler', self)

        self._fileOpenAction = QAction('&Open', self)
        self._fileOpenAction.setShortcut(QKeySequence('Ctrl+O'))
        
        self._fileSaveAction = QAction('&Save', self)
        self._fileSaveAction.setShortcut(QKeySequence('Ctrl+S'))

        self._fileSaveAsAction = QAction('S&ave as', self)
        self._fileSaveAsAction.setShortcut(QKeySequence('Ctrl+Shift+S'))

        self._fileExportAction = QAction('&Export', self)
        self._fileExportAction.setShortcut(QKeySequence('Ctrl+E'))

        self._fileCloseAction = QAction('&Close', self)
        self._fileCloseAction.setShortcut(QKeySequence('Ctrl+W'))

        self._fileExitAction = QAction('&Quit', self)
        self._fileExitAction.setShortcut(QKeySequence('Alt+F4'))

        # Edit
        self._editUndoAction = UndoAction('&Undo', self)
        self._editUndoAction.setShortcut(QKeySequence('Ctrl+Z'))

        self._editRedoAction = RedoAction('&Redo', self)
        self._editRedoAction.setShortcut(QKeySequence('Ctrl+Y'))

        self._editCutAction = QAction('C&ut', self)
        self._editCutAction.setShortcut(QKeySequence('Ctrl+X'))

        self._editCopyAction = QAction('&Copy', self)
        self._editCopyAction.setShortcut(QKeySequence('Ctrl+C'))

        self._editPasteAction = QAction('&Paste', self)
        self._editPasteAction.setShortcut(QKeySequence('Ctrl+V'))

        self._rotClock_90Action = RotateRightAction('Rotate right', self)

        self._rotAntiClock_90Action = RotateLeftAction('Rotate left', self)

        self._rotReverseAction = QAction('Flip', self)

        self._selectAllAction = QAction('Select all', self)
        self._selectAllAction.setShortcut(QKeySequence('Ctrl+A'))

        self._reverseSelectionAction = QAction('Invert selection', self)
        self._reverseSelectionAction.setShortcut(QKeySequence('Ctrl+Shift+A'))

        self._editNewSimulationFromSelectionAction = QAction('Create simulation from selection', self)

        self._editNewCompositeBoxFromSelectionAction = QAction('Create composite box from selection', self)

        self._editEraseSelectionAction = DeleteAction('Delete', self)
        self._editEraseSelectionAction.setShortcut(QKeySequence('Delete'))

        self._windowZoomAction = QAction('Zoom +', self)
        self._windowZoomAction.setShortcut(QKeySequence('Ctrl++'))

        self._windowDezoomAction = QAction('Zoom -', self)
        self._windowDezoomAction.setShortcut(QKeySequence('Ctrl+-'))

        self._windowCloseAllAction = QAction('Close dialog windows', self)
        self._windowCloseAllAction.triggered.connect(self._dialogsHolder.closeAll)
        self._windowCloseAllAction.setEnabled(self._dialogsHolder.len > 0)

        self._windowLibrariesAction = QAction('Libraries', self)
        self._windowLibrariesAction.triggered.connect(self._windowLibrariesMethod)
        
        self._windowOptionsAction = QAction('Options', self)

        self._simulationParametersAction = QAction('Parameters', self)

        self._simulationLaunchAction = StartAction('Start simulation', self)
        self._simulationLaunchAction.setShortcut(QKeySequence('F5'))

        self._simulationStopAction = StopAction('Stop simulation', self)
        self._simulationStopAction.setShortcut(QKeySequence('Shift+F5'))

        self._helpDocumentationAction = QAction('&Documentation', self)
        self._helpDocumentationAction.setShortcut(QKeySequence('F1'))
        
        self._helpAboutAction = QAction('&About', self)

    def _initMenu (self) -> None : 
        """Permet de créer le menu afficher dans la fenêtre."""

        self._menuBar = QMenuBar()
        self.setMenuBar(self._menuBar)

        self._mnFile = self._menuBar.addMenu('&Files')
        self._mnFileNew = self._mnFile.addMenu('&New')
        self._mnFileNew.addAction(self._fileNewSimulationAction)
        self._mnFileNew.addAction(self._fileNewBoxAction)
        self._mnFileNew.addAction(self._fileNewSolverAction)
        self._mnFile.addAction(self._fileOpenAction)
        self._mnFile.addAction(self._fileSaveAction)
        self._mnFile.addAction(self._fileSaveAsAction)
        self._mnRecentFiles = self._mnFile.addMenu("Recent Files")
        self._mnFile.addSeparator()
        self._mnFile.addAction(self._fileExportAction)
        self._mnFile.addSeparator()
        self._mnFile.addAction(self._fileCloseAction)
        self._mnFile.addSeparator()
        self._mnFile.addAction(self._fileExitAction)

        self._mnEdit = self._menuBar.addMenu('&Edit')
        self._mnEdit.addAction(self._editUndoAction)
        self._mnEdit.addAction(self._editRedoAction)
        self._mnEdit.addSeparator()
        self._mnEdit.addAction(self._editCutAction)
        self._mnEdit.addAction(self._editCopyAction)
        self._mnEdit.addAction(self._editPasteAction)
        self._mnEdit.addSeparator()
        self._mnEditRotation = self._mnEdit.addMenu('Rotate')
        self._mnEditRotation.addAction(self._rotClock_90Action)
        self._mnEditRotation.addAction(self._rotAntiClock_90Action)
        self._mnEditRotation.addAction(self._rotReverseAction)
        self._mnEdit.addSeparator()
        self._mnEdit.addAction(self._selectAllAction)
        self._mnEdit.addAction(self._reverseSelectionAction)
        self._mnEdit.addSeparator()
        self._mnEdit.addAction(self._editNewSimulationFromSelectionAction)
        self._mnEdit.addAction(self._editNewCompositeBoxFromSelectionAction)
        self._mnEdit.addSeparator()
        self._mnEdit.addAction(self._editEraseSelectionAction)

        self._mnWindow = self._menuBar.addMenu('&View')
        self._mnWindow.addAction(self._windowZoomAction)
        self._mnWindow.addAction(self._windowDezoomAction)
        self._mnWindow.addSeparator()
        self._mnWindowDialogues = self._mnWindow.addMenu('Opened dialog windows')
        self._mnWindowDialogues.setEnabled(self._dialogsHolder.len > 0)
        self._mnWindow.addAction(self._windowCloseAllAction)
        self._mnWindow.addSeparator()
        self._mnWindow.addAction(self._windowLibrariesAction)
        self._mnWindow.addAction(self._windowOptionsAction)
        
        self._mnSimulation = self._menuBar.addMenu('&Simulation')
        self._mnSimulation.addAction(self._simulationParametersAction)
        self._mnSimulation.addSeparator()
        self._mnSimulation.addAction(self._simulationLaunchAction)
        self._mnSimulation.addAction(self._simulationStopAction)

        self._mnHelp = self._menuBar.addMenu('&?')
        self._mnHelp.addAction(self._helpDocumentationAction)
        self._mnHelp.addSeparator()
        self._mnHelp.addAction(self._helpAboutAction)