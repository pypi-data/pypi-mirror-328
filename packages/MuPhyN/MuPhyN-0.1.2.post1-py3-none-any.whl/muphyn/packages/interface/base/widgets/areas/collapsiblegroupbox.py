from typing import Dict, Tuple

from PyQt6.QtCore import QSize, QMargins
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QGroupBox, QLayout, QPushButton, QSizePolicy, QSpacerItem, QWidget

from muphyn.packages.interface.base.finders import findScreenForWidget, findWindowForWidget

class CollapseExpandButton(QPushButton):

    def __init__(self, isCollapsed: bool, parent: QWidget = None):
        super().__init__(parent)

        self._isCollapsed: bool = isCollapsed

        self.updateText()

    def isCollapsed(self):
        return self._isCollapsed
    
    def setIsCollapsed(self, newIsCollapsed: bool):
        if self._isCollapsed != newIsCollapsed:
            self._isCollapsed = newIsCollapsed
            self.updateText()
    
    def updateText(self):
        self.setText("Expand" if self._isCollapsed else "Collapse")

class CollapsibleGroupBox(QGroupBox):
    """
    This class has been adapted from C++ code

    Credits: user1134621
    Source link: https://stackoverflow.com/questions/37049588/making-collapsible-groupboxes-in-qt-what-determines-the-collapsed-size
    """

    
    def __init__(self, title: str = None, isCollapsed: bool = False, parent: QWidget = None):
        if title is None:
            super().__init__(parent)
        else:
            super().__init__(title, parent)

        # Init parameters
        self._isCollapsed = isCollapsed
        self._spacerItemSizes: Dict[QSpacerItem, Tuple[QSize, QSizePolicy]] = {}
        self._layoutMargins: Dict[QLayout, QMargins] = {}

        # Init ui
        self.initUI()


    def initUI(self):
        # Init control button
        self._collapseExpandButton: CollapseExpandButton = CollapseExpandButton(self._isCollapsed, self)
        self._collapseExpandButton.pressed.connect(self.onVisibilityChanged)

        # Connect screen changed
        self.connectScreenChanged()

        # Resize collapse button
        self.resizeCollapseButton()

    def resizeEvent(self, resizeEvent: QResizeEvent) -> None:
        self.resizeCollapseButton()
        return super().resizeEvent(resizeEvent)
    
    def resizeCollapseButton(self):
        screen = findScreenForWidget(self)

        if screen is None:
            return
        
        size = self.size()
        buttonSize = self._collapseExpandButton.sizeHint()
        self._collapseExpandButton.setGeometry(size.width() - buttonSize.width(), 0, buttonSize.width(), buttonSize.height())

    def collapseLayout(self, layout: QLayout):
        if layout not in self._layoutMargins:
            for itemIndex in range(layout.count()):
                # Get item
                item = layout.itemAt(itemIndex)

                if item.widget() is not None:
                    widget = item.widget()
                    if widget != self._collapseExpandButton:
                        widget.setVisible(False)
                elif item.spacerItem() is not None:
                    self.collapseSpacer(item.spacerItem())
                elif item.layout() is not None:
                    self.collapseLayout(item.layout())

            self._layoutMargins[layout] = layout.contentsMargins()
            layout.setContentsMargins(0, 0, 0, 0)

    def collapseSpacer(self, spacerItem: QSpacerItem):
        if spacerItem not in self._spacerItemSizes:
            self._spacerItemSizes[spacerItem] = (spacerItem.sizeHint(), spacerItem.sizePolicy())
            spacerItem.changeSize(0, 0)

    def expandLayout(self, layout: QLayout):
        if layout in self._layoutMargins:
            for itemIndex in range(layout.count()):
                item = layout.itemAt(itemIndex)

                if item.widget() is not None:
                    widget = item.widget()
                    if widget != self._collapseExpandButton:
                        widget.setVisible(True)
                elif item.spacerItem() is not None:
                    self.expandSpacer(item.spacerItem())
                elif item.layout() is not None:
                    self.expandLayout(item.layout())
        
            layout.setContentsMargins(self._layoutMargins[layout])

    def expandSpacer(self, spacerItem: QSpacerItem):
        if spacerItem in self._spacerItemSizes:
            spacerItemSize, spacerItemSizePolicy = self._spacerItemSizes[spacerItem]

            spacerItem.changeSize(spacerItemSize.width(), spacerItemSize.height(), 
                spacerItemSizePolicy.horizontalPolicy(), spacerItemSizePolicy.verticalPolicy())

    def onScreenChanged(self):
        self.resizeCollapseButton()

    def onVisibilityChanged(self):
        if self.layout() is not None:
            isCollapsed = self._isCollapsed

            if isCollapsed:
                self.expandLayout(self.layout())

                self._isCollapsed = False
                self._collapseExpandButton.setIsCollapsed(False)
            else:
                self._layoutMargins.clear()
                self._spacerItemSizes.clear()

                self.collapseLayout(self.layout())

                self._isCollapsed = True
                self._collapseExpandButton.setIsCollapsed(True)

    def connectScreenChanged(self):
        windowHandle = findWindowForWidget(self)
        if windowHandle is not None:
            windowHandle.screenChanged.connect(self.onScreenChanged)