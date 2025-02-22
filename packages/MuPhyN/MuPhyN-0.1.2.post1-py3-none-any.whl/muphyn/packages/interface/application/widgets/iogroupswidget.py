from typing import List, Dict

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QCheckBox, QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class IOGroupWidget(QGroupBox):

    removeIOGroup = pyqtSignal(object)

    def __init__(self, ioGroup: Dict, parent: QWidget = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent)

        # Is Infinite
        if "isInfinite" in ioGroup and type(ioGroup["isInfinite"]) == bool:
            self._isInfinite: bool = ioGroup["isInfinite"]
        else:
            self._isInfinite = False

        # IO Group name
        if "name" in ioGroup and type(ioGroup["name"]) == str:
            self._name: bool = ioGroup["name"]
        else:
            self._name = ""

        # Io Type
        if "type" in ioGroup and type(ioGroup["type"]) == str:
            self._type: str = ioGroup["type"]
        else:
            self._type = ""

        # IO Count
        if "count" in ioGroup and type(ioGroup["count"]) == int:
            self._defaultCount: int = ioGroup["count"]
        else:
            self._defaultCount = 0

        # Minimum Count
        if "min" in ioGroup and type(ioGroup["min"]) == int:
            self._minimumCount: int = ioGroup["min"]
        else:
            self._minimumCount = 0

        # Maximum Count
        if "max" in ioGroup and type(ioGroup["max"]) == int:
            self._maximumCount: int = ioGroup["max"]
        else:
            self._maximumCount = -1

        # Init UI
        self.initUI()

    def initUI(self):
        # Remove button
        self._ioGroupRemoveButton = QPushButton("delete")
        self._ioGroupRemoveButton.pressed.connect(self.removeButtonPressed)

        # Group name
        self._groupNameTitleLabel = QLabel("Name")
        self._groupNameLineEdit = QLineEdit(self._name)

        # Group type
        self._groupTypeTitleLabel = QLabel("Type")
        self._groupTypeLineEdit = QLineEdit(self._type)

        # Group is infinite
        self._groupIsInfiniteTitleLabel = QLabel("Is infinite ?")
        self._groupIsInfiniteCheckBox = QCheckBox()
        self._groupIsInfiniteCheckBox.setChecked(self._isInfinite)
        self._groupIsInfiniteCheckBox.stateChanged.connect(self.setIsInfinite)

        # IO default count
        self._groupDefaultCountTitleLabel = QLabel("Default count")
        self._groupDefaultCountLineEdit = QLineEdit(str(self._defaultCount))

        # Min count
        self._minCountTitleLabel = QLabel("Min Count")
        self._minCountLineEdit = QLineEdit(str(self._minimumCount))

        # Max count
        self._maxCountTitleLabel = QLabel("Max Count")
        self._maxCountLineEdit = QLineEdit(str(self._maximumCount))

        #
        mainLayout = QGridLayout()
        mainLayout.addWidget(self._ioGroupRemoveButton, 0, 2, Qt.AlignmentFlag.AlignRight)
        mainLayout.addWidget(self._groupNameTitleLabel, 1, 0)
        mainLayout.addWidget(self._groupNameLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(self._groupTypeTitleLabel, 2, 0)
        mainLayout.addWidget(self._groupTypeLineEdit, 2, 1, 1, 2)
        mainLayout.addWidget(self._groupIsInfiniteTitleLabel, 3, 0)
        mainLayout.addWidget(self._groupIsInfiniteCheckBox, 3, 1, 1, 2)
        mainLayout.addWidget(self._groupDefaultCountTitleLabel, 4, 0)
        mainLayout.addWidget(self._groupDefaultCountLineEdit, 4, 1, 1, 2)
        mainLayout.addWidget(self._minCountTitleLabel, 5, 0)
        mainLayout.addWidget(self._minCountLineEdit, 5, 1, 1, 2)
        mainLayout.addWidget(self._maxCountTitleLabel, 6, 0)
        mainLayout.addWidget(self._maxCountLineEdit, 6, 1, 1, 2)
        
        if self._isInfinite:
            self.displayMinMaxCountWidgets()
        else:
            self.hideMinMaxCountWidgets()

        mainLayout.setColumnStretch(1, 1)

        self.setLayout(mainLayout)

    def displayMinMaxCountWidgets(self):
        self._minCountTitleLabel.setVisible(True)
        self._minCountLineEdit.setVisible(True)
        self._maxCountTitleLabel.setVisible(True)
        self._maxCountLineEdit.setVisible(True)

    def hideMinMaxCountWidgets(self):
        self._minCountTitleLabel.setVisible(False)
        self._minCountLineEdit.setVisible(False)
        self._maxCountTitleLabel.setVisible(False)
        self._maxCountLineEdit.setVisible(False)

    def setIsInfinite(self, newIsInfinite: bool):
        if self._isInfinite != newIsInfinite:
            self._isInfinite = newIsInfinite

            #
            if self._isInfinite:
                self.displayMinMaxCountWidgets()
            else:
                self.hideMinMaxCountWidgets()

    def removeButtonPressed(self):
        self.removeIOGroup.emit(self)

class IOGroupsWidget(QWidget):

    def __init__(self, ioGroups: List = [], parent: QWidget = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)

        self._ioGroups: List[Dict] = ioGroups
        self._ioGroupIndex: int = len(ioGroups)

        self.initUI()

    def initUI(self):
        # Add IO group button
        self._addIOGroupButton = QPushButton()
        self._addIOGroupButton.pressed.connect(self.addIOGroup)

        # Init main layout
        self._mainLayout = QVBoxLayout()
        self._mainLayout.addWidget(self._addIOGroupButton)

        for ioGroup in self._ioGroups:
            self.addIOGroupWidget(ioGroup)

        #
        self._mainLayout.setStretch(self._mainLayout.count(), 1)
        self.setLayout(self._mainLayout)
        
    def addIOGroup(self, ioGroup: Dict = None):
        # Update IO group index
        self._ioGroupIndex += 1

        if ioGroup is None:
            ioGroup = {
                "count": 0,
                "type": "",
                "name": f"Output group {self._ioGroupIndex}"
            }

        # Add to list
        self._ioGroups.append(ioGroup)

        # Add Widget
        self.addIOGroupWidget(ioGroup)

    def addIOGroupWidget(self, ioGroup: Dict = None):
        if ioGroup is None:
            ioGroup = {
                "count": 0,
                "type": "",
                "name": f"Output group {self._mainLayout.count()}",
                "isInfinite": False
            }

        # Init IO Group Widget
        ioGroupWidget = IOGroupWidget(ioGroup)
        ioGroupWidget.removeIOGroup.connect(self.removeIOGroup)

        # 
        self._mainLayout.insertWidget(self._mainLayout.count(), ioGroupWidget)

    def removeIOGroup(self, ioGroupWidget: IOGroupWidget):
        self._mainLayout.removeWidget(ioGroupWidget)