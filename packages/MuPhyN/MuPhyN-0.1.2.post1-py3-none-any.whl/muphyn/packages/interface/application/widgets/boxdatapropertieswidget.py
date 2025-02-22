from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QCheckBox, QGridLayout, QFormLayout, QLineEdit, \
    QScrollArea, QVBoxLayout, QWidget

from muphyn.packages.core.application import AbstractBoxData, CodeBoxData
from muphyn.packages.interface.base import CollapsibleGroupBox, IconSelector

from .iogroupswidget import IOGroupsWidget

class BoxDataPropertiesWidget(QScrollArea):

    FormColumnSpacing = 20

    initFunctionNameEdited = pyqtSignal(str, str)
    simulationFunctionNameEdited = pyqtSignal(str, str)
    endFunctionNameEdited = pyqtSignal(str, str)

    def __init__(self, boxData: AbstractBoxData, parent: QWidget = None) -> None:
        super().__init__(parent)

        self._boxData: AbstractBoxData = boxData

        if isinstance(boxData, CodeBoxData):
            self._oldInitFunctionName = boxData.init_method
            self._oldSimulationFunctionName = boxData.box_function
            self._oldEndFunctionName = boxData.end_method

        self.initUI()

    def initUI(self):
        # Scroll area parameters
        self.setWidgetResizable(True)

        # Box name
        self._pathLineEdit = QLineEdit(self._boxData.path)

        # Box name
        self._boxNameLineEdit = QLineEdit(self._boxData.box_name)

        # Box library
        self._boxLibraryLineEdit = QLineEdit(self._boxData.box_library)

        # Box type
        self._boxTypeLineEdit = QLineEdit(self._boxData.box_type)

        # Creator
        self._boxAuthorLineEdit = QLineEdit(self._boxData.creator)

        # Creation date
        self._boxCreationDateLabel = QLineEdit(self._boxData.date_created.strftime("%Y-%m-%d"))

        # Description
        self._boxDescriptionLineEdit = QLineEdit(self._boxData.description)

        # Icon
        """
        To manage the icon path, there are 2 cases:
        - If icon path is child box path
            → Save relative path
        - Else 
            - Ask to create a copy in box directory
            - If "YES" is selected
                → Create a copy in subdirectory
                → Save relative path
            - Else
                → Save full path
        """
        # self._boxIconSelector = QLineEdit(self._boxData.icon)
        self._boxIconSelector = IconSelector(self._boxData.icon)
        # self._boxIconSelector.iconPathChanged.connect(self.setIconPath)

        # 
        metadataLayout = QFormLayout()
        metadataLayout.addRow("Path", self._pathLineEdit)
        metadataLayout.addRow("Name", self._boxNameLineEdit)
        metadataLayout.addRow("Library", self._boxLibraryLineEdit)
        metadataLayout.addRow("Type", self._boxTypeLineEdit)
        metadataLayout.addRow("Author", self._boxAuthorLineEdit)
        metadataLayout.addRow("Creation date", self._boxCreationDateLabel)
        metadataLayout.addRow("Description", self._boxDescriptionLineEdit)
        metadataLayout.addRow("Icon", self._boxIconSelector)
        metadataLayout.setHorizontalSpacing(BoxDataPropertiesWidget.FormColumnSpacing)
        metadataGroupBox = CollapsibleGroupBox("General")
        metadataGroupBox.setLayout(metadataLayout)

        if isinstance(self._boxData, CodeBoxData):
            # Init funtion
            self._initFunctionLineEdit = QLineEdit(self._boxData.init_method)
            self._initFunctionLineEdit.editingFinished.connect(self.initFunctionLineEditTextEdited)

            # Simulation function
            self._simulationFunctionLineEdit = QLineEdit(self._boxData.box_name)
            self._simulationFunctionLineEdit.editingFinished.connect(self.simulationFunctionLineEditTextEdited)

            # End function
            self._endFunctionLineEdit = QLineEdit(self._boxData.box_name)
            self._endFunctionLineEdit.editingFinished.connect(self.endFunctionLineEditTextEdited)

            # Functions group
            functionsLayout = QFormLayout()
            functionsLayout.addRow("Init function", self._initFunctionLineEdit)
            functionsLayout.addRow("Simulation function", self._simulationFunctionLineEdit)
            functionsLayout.addRow("End function", self._endFunctionLineEdit)
            functionsLayout.setHorizontalSpacing(BoxDataPropertiesWidget.FormColumnSpacing)
            functionsGroupBox = CollapsibleGroupBox("Functions")
            functionsGroupBox.setLayout(functionsLayout)

        if isinstance(self._boxData, CodeBoxData):
            # Wait for any events
            self._waitForAnyEventCheckBox = QCheckBox()
            self._waitForAnyEventCheckBox.setChecked(self._boxData.wait_for_event)

            # Wait for all events
            self._waitForAllEventCheckBox = QCheckBox()
            self._waitForAllEventCheckBox.setChecked(self._boxData.wait_for_all_signal_events)

            waitForEventsLayout = QFormLayout()
            waitForEventsLayout.addRow("Wait for event", self._waitForAnyEventCheckBox)
            waitForEventsLayout.addRow("Wait for all events", self._waitForAllEventCheckBox)
            eventsGroupBox = CollapsibleGroupBox("Events")
            eventsGroupBox.setLayout(waitForEventsLayout)

        # Inputs
        inputsLayout = QGridLayout()
        inputsLayout.addWidget(IOGroupsWidget(self._boxData.inputs))
        inputsGroupBox = CollapsibleGroupBox("Inputs")
        inputsGroupBox.setLayout(inputsLayout)

        # Outputs
        outputsLayout = QGridLayout()
        outputsLayout.setRowStretch(outputsLayout.count()//2, 1)
        outputsLayout.setColumnMinimumWidth(0, 80)
        outputsGroupBox = CollapsibleGroupBox("Outputs")
        outputsGroupBox.setLayout(outputsLayout)

        # Parameters
        if isinstance(self._boxData, CodeBoxData):

            parametersLayout = QVBoxLayout()

            for parameterName, parameter in self._boxData.params.items():
                parameterLayout = QFormLayout()
                parameterLayout.addRow("Name", QLineEdit(parameterName))
                parameterLayout.addRow("Type", QLineEdit(parameter["type"]))
                parameterLayout.addRow("Value", QLineEdit(str(parameter["value"])))
                parameterLayout.setHorizontalSpacing(BoxDataPropertiesWidget.FormColumnSpacing)

                parametersLayout.addLayout(parameterLayout)



            parametersLayout.setStretch(parametersLayout.count()//2, 1)
            # parametersLayout.setColumnMinimumWidth(0, 80)
            parametersGroupBox = CollapsibleGroupBox("Parameters")
            parametersGroupBox.setLayout(parametersLayout)


        # Set main layout
        mainLayout = QVBoxLayout()
        
        # Add metadata group
        mainLayout.addWidget(metadataGroupBox)

        # Add functions group
        if isinstance(self._boxData, CodeBoxData):
            mainLayout.addWidget(functionsGroupBox)

        # Add events group
        if isinstance(self._boxData, CodeBoxData):
            mainLayout.addWidget(eventsGroupBox)

        # Add inputs group
        mainLayout.addWidget(inputsGroupBox)

        # Add outputs group
        mainLayout.addWidget(outputsGroupBox)

        # Add parameters group
        if isinstance(self._boxData, CodeBoxData):
            mainLayout.addWidget(parametersGroupBox)
        mainLayout.addWidget(QWidget())
        mainLayout.setStretch(mainLayout.count()-1, 1)

        scrollWidget = QWidget()
        self.setWidget(scrollWidget)
        scrollWidget.setLayout(mainLayout)

    def initFunctionLineEditTextEdited(self):
        # Get new function name
        newInitFunctionName = self._initFunctionLineEdit.text().strip()

        if newInitFunctionName != "":

            # Send signal
            self.initFunctionNameEdited.emit(self._oldInitFunctionName, newInitFunctionName)

            # Replace old value
            self._oldInitFunctionName = newInitFunctionName

    def simulationFunctionLineEditTextEdited(self):
        # Get new function name
        newSimulationFunctionName = self._simulationFunctionLineEdit.text().strip()

        if newSimulationFunctionName != "":

            # Send signal
            self.simulationFunctionNameEdited.emit(self._oldSimulationFunctionName, newSimulationFunctionName)

            # Replace old value
            self._oldSimulationFunctionName = newSimulationFunctionName

    def endFunctionLineEditTextEdited(self):
        # Get new function name
        newEndFunctionName = self._endFunctionLineEdit.text().strip()

        if newEndFunctionName != "":

            # Send signal
            self.endFunctionNameEdited.emit(self._oldEndFunctionName, newEndFunctionName)

            # Replace old value
            self._oldEndFunctionName = newEndFunctionName