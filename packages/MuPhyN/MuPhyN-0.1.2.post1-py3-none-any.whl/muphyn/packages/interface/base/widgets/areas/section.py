"""
This code is based on the code of the following link:
    https://github.com/MichaelVoelkel/qt-collapsible-section
"""

from PyQt6.QtWidgets import QWidget, QToolButton, QFrame, QScrollArea, QGridLayout, QSizePolicy, QLayout
from PyQt6.QtCore import QParallelAnimationGroup, Qt, QPropertyAnimation, QAbstractAnimation

class Section(QWidget):

    def __init__(self, title: str, animationDuration: int=250, parent: QWidget = None):

        super().__init__(parent)
        self.toggleButton = QToolButton(self)
        headerLine = QFrame(self)
        self.toggleAnimation = QParallelAnimationGroup(self)
        self.contentArea = QScrollArea(self)
        mainLayout = QGridLayout(self)
        self.animationDuration = animationDuration

        self.toggleButton.setStyleSheet("QToolButton {border: none}")
        self.toggleButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggleButton.setArrowType(Qt.ArrowType.RightArrow)
        self.toggleButton.setText(title)
        self.toggleButton.setCheckable(True)
        self.toggleButton.setChecked(False)

        headerLine.setFrameShape(QFrame.Shape.HLine)
        headerLine.setFrameShadow(QFrame.Shadow.Sunken)
        headerLine.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.contentArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # start out collapsed
        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)
        self.isExpanded = False

        # let the entire widget grow and shrink with its content
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggleAnimation.addAnimation(QPropertyAnimation(self.contentArea, b"maximumHeight"))

        mainLayout.setVerticalSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        row = 0
        mainLayout.addWidget(self.toggleButton, row, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        row += 1
        mainLayout.addWidget(headerLine, row, 2, 1, 1)
        mainLayout.addWidget(self.contentArea, row, 0, 1, 3)
        self.setLayout(mainLayout)

        self.toggleButton.toggled.connect(self.toggle)

    def toggle(self, expanded: bool):
        self.toggleButton.setArrowType(Qt.ArrowType.DownArrow if expanded else Qt.ArrowType.RightArrow)
        self.toggleAnimation.setDirection(QAbstractAnimation.Direction.Forward if expanded else QAbstractAnimation.Direction.Backward)
        self.toggleAnimation.start()
        
        self.isExpanded = expanded

    def setContentLayout(self, contentLayout: QLayout):
        if self.contentArea.layout() is not None:
            self.contentArea.layout().deleteLater()
        self.contentArea.setLayout(contentLayout)
        self.collapsedHeight = self.sizeHint().height() - self.contentArea.maximumHeight()
        
        self.updateHeights()
    
    def setTitle(self, title: str):
        self.toggleButton.setText(title)
    
    def updateHeights(self):
        contentHeight: int = self.contentArea.layout().sizeHint().height()

        # for (int i = 0 i < self.toggleAnimation->animationCount() - 1 ++i):
        for animationIndex in range(self.toggleAnimation.animationCount()-1):
            sectionAnimation: QPropertyAnimation = self.toggleAnimation.animationAt(animationIndex)
            sectionAnimation.setDuration(self.animationDuration)
            sectionAnimation.setStartValue(self.collapsedHeight)
            sectionAnimation.setEndValue(self.collapsedHeight + contentHeight)

        # Do last animation
        contentAnimation: QPropertyAnimation = self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1)
        contentAnimation.setDuration(self.animationDuration)
        contentAnimation.setStartValue(0)
        contentAnimation.setEndValue(contentHeight)
        
        self.toggleAnimation.setDirection(QAbstractAnimation.Direction.Forward if self.isExpanded else QAbstractAnimation.Direction.Backward)
        self.toggleAnimation.start()