import re

from PyQt6.QtWidgets import QTabWidget, QGridLayout, QWidget, QSplitter, QVBoxLayout

from muphyn.packages.core.application import CodeBoxData
from muphyn.packages.interface.base import CodeEditor
from ..holders.actions_holder import ActionsHolder
from ..models.editablemodels.boxdatamodel import BoxDataModel
from ..widgets.boxdatapropertieswidget import BoxDataPropertiesWidget

from .abstracteditor import AbstractEditor

class BoxDataEditor (AbstractEditor) :

    InitFunctionRegexPattern = "def\s+(?P<functionName>{functionName})\s*\(\s*(?P<boxVarName>\w+)(?:\s*\:\s*Box)?\s*,\s*(?P<schedulerVarName>\w+)(?:\s*\:\s*SchedulerParams)?\s*\)(?:\s*->\s*None)?\s*:\s*"
    SimulationFunctionRegexPattern = "def\s+(?P<functionName>{functionName})\s*\(\s*(?P<boxVarName>\w+)(?:\s*\:\s*Box)?\s*,\s*(?P<schedulerVarName>\w+)(?:\s*\:\s*SchedulerEvent)?\s*\)(?:\s*->\s*None)?\s*:\s*"
    EndFunctionRegexPattern = "def\s+(?P<functionName>{functionName})\s*\(\s*(?P<boxVarName>\w+)(?:\s*\:\s*Box)?\s*\)(?:\s*->\s*None)?\s*:\s*"

    
    def __init__(self, tab_holder : QTabWidget, boxDataModel : BoxDataModel, actions_holder : ActionsHolder) :
        AbstractEditor.__init__(self, tab_holder, boxDataModel, actions_holder)
        
        # Box data
        self._boxData = boxDataModel.boxData

        # Init UI
        self.initUI()

        # Init signals
        self._splitter.splitterMoved.connect(self.onSplitterMoved)
        
    def initUI(self):

        # Init splitter
        self._splitter = QSplitter()

        # Init text browser
        self._codeEditor = CodeEditor()
        self._codeEditor.setMinimumWidth(300)

        # Code Editor layout
        codeEditorLayout = QGridLayout()
        codeEditorViewWidget = QWidget()
        codeEditorLayout.addWidget(self._codeEditor, 0, 0, 2, 2)
        codeEditorLayout.setColumnStretch(0, 1)
        codeEditorLayout.setRowStretch(1, 1)
        codeEditorViewWidget.setLayout(codeEditorLayout)


        # Box data properties view
        self._boxDataPropertiesWidget = BoxDataPropertiesWidget(CodeBoxData.default())
        self._boxDataPropertiesWidget.setMinimumWidth(300)
        self._boxDataPropertiesWidget.initFunctionNameEdited.connect(self._initFunctionNameChanged)
        self._boxDataPropertiesWidget.simulationFunctionNameEdited.connect(self._simulationFunctionNameChanged)
        self._boxDataPropertiesWidget.endFunctionNameEdited.connect(self._endFunctionNameChanged)

        # Add widgets
        self._splitter.addWidget(codeEditorViewWidget)
        self._splitter.addWidget(self._boxDataPropertiesWidget)
        self._splitter.setStretchFactor(0, 1)

        # Set children widget parameters
        self._splitter.setCollapsible(0, False)
        self._splitter.setCollapsible(1, False)

        #
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self._splitter)

        self.setLayout(mainLayout)


    def _initFunctionNameChanged(self, oldName: str, newName: str):

        # Get code editor text
        codeEditorText = str(self._codeEditor.text())

        # Get matches list
        BoxDataEditor.InitFunctionRegexPattern.format(functionName = oldName)

        compiledPattern = re.compile(BoxDataEditor.InitFunctionRegexPattern.format(functionName = oldName))
        initFunctionMatches = [find for find in compiledPattern.finditer(codeEditorText)]
    
        if len(initFunctionMatches) > 0:
            
            for initFunctionMatch in initFunctionMatches:
                matchString = initFunctionMatch.string[initFunctionMatch.start():initFunctionMatch.end()].strip()
                groupDict = initFunctionMatch.groupdict()
                boxParamName = groupDict["boxVarName"]
                schedulerParamName = groupDict["schedulerVarName"]
                self._codeEditor.setText(
                    codeEditorText.replace(
                        matchString, 
                        f"def {newName}({boxParamName}: Box, {schedulerParamName}: SchedulerParams) -> None:"
                    )
                )

        else:
            if newName != "":
                # Add init function
                self._codeEditor.append(f"\r\ndef {newName}(box: Box, schedulerParams: SchedulerParams) -> None:\r\n    pass")

    def _simulationFunctionNameChanged(self, oldName: str, newName: str):

        # Get code editor text
        codeEditorText = str(self._codeEditor.text())

        # Get matches list
        BoxDataEditor.SimulationFunctionRegexPattern.format(functionName = oldName)

        compiledPattern = re.compile(BoxDataEditor.SimulationFunctionRegexPattern.format(functionName = oldName))
        simulationFunctionMatches = [find for find in compiledPattern.finditer(codeEditorText)]
    
        if len(simulationFunctionMatches) > 0:
            
            for simulationFunctionMatch in simulationFunctionMatches:
                matchString = simulationFunctionMatch.string[simulationFunctionMatch.start():simulationFunctionMatch.end()].strip()
                groupDict = simulationFunctionMatch.groupdict()
                boxParamName = groupDict["boxVarName"]
                schedulerParamName = groupDict["schedulerVarName"]
                self._codeEditor.setText(
                    codeEditorText.replace(
                        matchString, 
                        f"def {newName}({boxParamName}: Box, {schedulerParamName}: SchedulerEvent) -> None:"
                    )
                )

        else:
            if newName != "":
                # Add simulation function
                self._codeEditor.append(f"\r\ndef {newName}(box: Box, schedulerParams: SchedulerEvent) -> None:\r\n    pass")

    def _endFunctionNameChanged(self, oldName: str, newName: str):

        # Get code editor text
        codeEditorText = str(self._codeEditor.text())

        # Get matches list
        BoxDataEditor.EndFunctionRegexPattern.format(functionName = oldName)

        compiledPattern = re.compile(BoxDataEditor.EndFunctionRegexPattern.format(functionName = oldName))
        endFunctionMatches = [find for find in compiledPattern.finditer(codeEditorText)]
    
        if len(endFunctionMatches) > 0:
            
            for endFunctionMatch in endFunctionMatches:
                matchString = endFunctionMatch.string[endFunctionMatch.start():endFunctionMatch.end()].strip()
                groupDict = endFunctionMatch.groupdict()
                boxParamName = groupDict["boxVarName"]
                self._codeEditor.setText(
                    codeEditorText.replace(
                        matchString, 
                        f"def {newName}({boxParamName}: Box) -> None:"
                    )
                )

        else:
            if newName != "":
                # Add end function
                self._codeEditor.append(f"\r\ndef {newName}(box: Box) -> None:\r\n    pass")


    def collapseAssistant(self):
        self.setSizes([1, 0])
        self.setAssistantIsCollapse(True)

    def unCollapseAssistant(self):
        self.setSizes([self.size().width(), 300])
        self.setAssistantIsCollapse(False)

    def setAssistantIsCollapse(self, newAssistantIsCollapsed: bool):
        if self._assistantIsCollapsed != newAssistantIsCollapsed:
            # Update value
            self._assistantIsCollapsed = newAssistantIsCollapsed

            # Update Button icon

    def toggleAssistantCollapse(self):
        if self._assistantIsCollapsed:
            self.unCollapseAssistant()
        else:
            self.collapseAssistant()

    def onSplitterMoved(self, pos: int, index: int):
        self.setAssistantIsCollapse(self.sizes()[1] == 0)
    