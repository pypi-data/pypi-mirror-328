from typing import List

from PyQt6.QtCore import QMimeData, QRegularExpression, QSortFilterProxyModel, Qt
from PyQt6.QtWidgets import QTreeView, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QMouseEvent, QDrag

from muphyn.packages.core.application import AbstractBoxData
from ..models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from .library_element import LibraryElement
from .box_library_element import BoxLibraryElement, BoxLibraryElementRole

class LibraryTreeView(QTreeView):

    MULTIPLE_BOX_IMPORT_OFFSET_X = 0
    MULTIPLE_BOX_IMPORT_OFFSET_Y = AbstractBoxModel.MinimunBoxHeight + 20

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        # General Parameters
        self.setHeaderHidden(True)
        self.setAnimated(True)

        # Enable Drag
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        # Set Selection Mode
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

    def build_model(self, boxesData: List[AbstractBoxData]):
        # Init Model
        treeModel: QStandardItemModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        rootModelDict = {}

        # Build Model
        for boxData in boxesData:
            # Split Box Library & Sub Libraries if there is a Sub Library
            libraryHierarchy = boxData.box_library.split(".")
            
            # Create Component Item
            componentItem = BoxLibraryElement(boxData)
            componentItem.setData(boxData, BoxLibraryElementRole.BOX_DATA)

            # Find Path in tree model
            if len(libraryHierarchy) > 0:
                rootPoint = libraryHierarchy.pop(0)

                if rootPoint in rootModelDict:
                    currentElement = rootModelDict[rootPoint]
                else:
                    # Create new element
                    currentElement = LibraryElement(rootPoint)

                    # Append new element to tree model
                    rootNode.appendRow(currentElement)

                    # Append element to model dict
                    rootModelDict[rootPoint] = currentElement
            
                while len(libraryHierarchy) > 0:
                    # Pop scheduler tree point from list
                    boxPoint = libraryHierarchy.pop(0)

                    # Check if node name already exists
                    if currentElement.hasChildNodeByName(boxPoint):
                        # Get this node point
                        currentElement = currentElement.getChildByName(boxPoint)
                    else:
                        # Create this node point
                        newElement = LibraryElement(boxPoint)

                        # Append new element
                        currentElement.appendRow(newElement)

                        # Go to the new Element
                        currentElement = newElement

                # Append component to tree
                currentElement.appendRow(componentItem)
        
        self._sourceModel = treeModel

        # Init Filter Model
        self._proxyModel =  QSortFilterProxyModel()
        self._proxyModel.setSourceModel(self._sourceModel)
        self._proxyModel.setRecursiveFilteringEnabled(True)
        self._proxyModel.sort(0)

        self.setModel(self._proxyModel)

    def filter_library_list(self, searched_string: str):
        # Build Regular Expression
        regExpression = QRegularExpression(searched_string, QRegularExpression.PatternOption.CaseInsensitiveOption)

        # Apply Regex Filtering
        self._proxyModel.setFilterRegularExpression(regExpression)
        if searched_string != "":
            self.expandAll()
        else:
            self.collapseAll()
            for selected_index in self.selectedIndexes():
                self.expandRecursively(selected_index)
                expanded_item_parent = selected_index.parent()
                while expanded_item_parent.row() != -1:
                    self.expand(expanded_item_parent)
                    expanded_item_parent = expanded_item_parent.parent()

    def mouseMoveEvent (self, event : QMouseEvent) -> None:
        if event.buttons() == Qt.MouseButton.LeftButton:
            selectedIndex = self.selectedIndexes()
            lenSelectedBoxes = len(selectedIndex)
            if self.selectionModel() is not None and lenSelectedBoxes > 1:
                # Init Mimedata
                mimeData : QMimeData = QMimeData()
                mimeData.setData("action", bytearray("new boxes".encode()))
                mimeData.setData("len", bytearray(f"{lenSelectedBoxes}".encode()))

                # Add Mimedata of each box
                for box_index, selected_index in enumerate(selectedIndex):
                    # Get Selected Item
                    itemData = self.model().itemData(selected_index)

                    # If Box Data has been saved
                    if BoxLibraryElementRole.BOX_DATA in itemData:
                        box_data: AbstractBoxData = itemData[BoxLibraryElementRole.BOX_DATA]

                        offset_x = LibraryTreeView.MULTIPLE_BOX_IMPORT_OFFSET_X * box_index
                        offset_y = LibraryTreeView.MULTIPLE_BOX_IMPORT_OFFSET_Y * box_index

                        mimeData.setData(f"box_data.{box_index}", bytearray(str(id(box_data)).encode()))
                        mimeData.setData(f"offset.{box_index}", bytearray(str(f"{offset_x};{offset_y}").encode()))

                # Create Drag Event
                drag : QDrag = QDrag(self)
                drag.setMimeData(mimeData)

                # Execute Drag
                da : Qt.DropAction = drag.exec(Qt.DropAction.CopyAction)

            elif lenSelectedBoxes == 1:
                # Get selected Index
                selected_index = selectedIndex[0]

                # 
                itemData = self.model().itemData(selected_index)
                if BoxLibraryElementRole.BOX_DATA in itemData:
                    box_data: AbstractBoxData = itemData[BoxLibraryElementRole.BOX_DATA]
                    
                    mimeData : QMimeData = QMimeData()
                    mimeData.setData("action", bytearray("new box".encode()))
                    mimeData.setData("box_data", bytearray(str(id(box_data)).encode()))

                    # Create Drag Event
                    drag : QDrag = QDrag(self)
                    drag.setMimeData(mimeData)

                    # Set Drag Pixmap
                    pixmap = box_data.pixmap
                    if pixmap is not None:
                        drag.setPixmap(pixmap)

                    # Execute Drag
                    da : Qt.DropAction = drag.exec(Qt.DropAction.CopyAction)