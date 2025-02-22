from PyQt6.QtCore import QSize, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QToolBar, QProgressBar, QHBoxLayout, QWidget

from muphyn.packages.interface.base import StartAction, StopAction

class SimulationControlToolbar(QWidget):

    # Constants
    MinimumProgressValue = 7 # Avoid graphical bug
    TerminationProportion = 0.99

    # Signals
    playButtonClicked = pyqtSignal(object)
    stopButtonClicked = pyqtSignal(object)

    def __init__(self, parent = None) -> None:
        super().__init__(parent=parent)

        # Init actions
        self.initActions()

        # Init UI
        self.initUI()

    @pyqtSlot()
    def onPlayButtonClicked(self):
        self.playButtonClicked.emit(self)

    @pyqtSlot()
    def onStopButtonClicked(self):
        self.stopButtonClicked.emit(self)

    def updateProgression(self, progress: int):
        if progress > 0:
            progress = round(SimulationControlToolbar.TerminationProportion * progress)
            progress = progress if progress > SimulationControlToolbar.MinimumProgressValue else SimulationControlToolbar.MinimumProgressValue
            self._progressBar.setValue(progress)
        else:
            self._progressBar.setValue(0)

    def progressionFinished(self):
        self._progressBar.setValue(100)
    
    def initActions(self):
        # Add Start Simulation Action
        self.startAction = StartAction()
        self.startAction.triggered.connect(self.onPlayButtonClicked)

        # Add Stop Simulation Action
        self.stopAction = StopAction()
        self.stopAction.triggered.connect(self.onStopButtonClicked)

    def initUI(self):
        # Init Tool Bar
        self._toolbar = QToolBar()
        self._toolbar.setIconSize(QSize(16, 16))
        
        # Add actions
        self._toolbar.addActions([
            self.startAction,
            self.stopAction
        ])

        # Init Progress Bar
        self._progressBar = QProgressBar()
        self._progressBar.setTextVisible(False)
        self._progressBar.setValue(0)

        # Add Simulation Controler
        controlButtonsLayout = QHBoxLayout()
        controlButtonsLayout.addWidget(self._toolbar)
        controlButtonsLayout.addWidget(self._progressBar, 1)

        # 
        self.setLayout(controlButtonsLayout)