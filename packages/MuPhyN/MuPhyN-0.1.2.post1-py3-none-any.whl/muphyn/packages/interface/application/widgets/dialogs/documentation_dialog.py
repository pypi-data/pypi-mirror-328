import os
from enum import IntEnum, Enum
from typing import Any, List

from PyQt6.QtCore import QSortFilterProxyModel, QItemSelection, QRegularExpression, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QSplitter, QVBoxLayout, QLineEdit, QWidget, \
    QAbstractItemView, QTreeView

from muphyn.packages.core.application import BoxesLibrariesManager, CodeBoxData, SchedulersLibrariesManager, SchedulerData
from muphyn.packages.interface.base import WebView
from muphyn.utils.paths import ROOT_DIR

from ...boxlibrary.library_element import LibraryElement
from .abstract_dialog import AbstractDialog

def buildMarkdownFromBoxData(boxData: CodeBoxData):
    # Get box Name
    boxName = boxData.box_name
    
    # Get box description
    description = boxData.description.replace('\\n', "\\n\\n")

    # Get Parameters
    parameters = boxData.params
    nParameters = len(parameters)
    parametersTable = '\n'.join([f"|{parameterName}|`{parameter['type']}`|{parameter['value']}|{parameter['description']}|" for parameterName, parameter in parameters.items()])
    
    # Inputs
    inputs = boxData.inputs
    inputsTable = [f"|{inputGroupName}|`{str(inputData['type'])}`|`{'Unlimited' if inputData['isInfinite'] else 'Fixed'}`|{'/' if 'count' not in inputData else inputData['count']}|{'/' if 'minimumCount' not in inputData else inputData['minimumCount']}|{'/' if 'maximumCount' not in inputData or inputData['maximumCount'] == 2147483647 else inputData['maximumCount']}|" for inputGroupName, inputData in inputs.items()]

    # Outputs
    outputs = boxData.outputs
    outputsTable = [f"|{outputGroupName}|`{str(outputData['type'])}`|`{'Unlimited' if outputData['isInfinite'] else 'Fixed'}`|{'/' if 'count' not in outputData else outputData['count']}|{'/' if 'minimumCount' not in outputData else outputData['minimumCount']}|{'/' if 'maximumCount' not in outputData or outputData['maximumCount'] == 2147483647 else outputData['maximumCount']}|" for outputGroupName, outputData in outputs.items()]
    
    ioTable = '\n'.join(inputsTable + outputsTable)

    return f"""
# {boxName} box

## 1. Description
{description}

## 2. Parameters
{boxName} box have {"no" if nParameters == 0 else nParameters } {'parameters' if nParameters > 1 else "parameter"}{':' if nParameters > 0 else "."}

{"" if nParameters == 0 else "| Name | Type | Default value | Description |"}
{"" if nParameters == 0 else "|---|---|---| --- |"}
{parametersTable}

## 3. IO
|       |Data Type  | Type | Default   | Minimum   | Maximum   |
| ---   |---        |---    |---        | ---       | ---       |
{ioTable}
    """

class DocumentationLibraryElement(LibraryElement):

    class Role(IntEnum):
        Title = 0
        Path = 1
        Order = 2
        Type = 3
        BoxData = 4

    class Type(Enum):
        Box = "Box"
        Document = "Document"
        Scheduler = "Scheduler"
    
    def __init__(self, title: str, path: str, type_: Type = Type.Document, boxData: CodeBoxData = None):
        super().__init__(title)

        self.setData(title, DocumentationLibraryElement.Role.Title)
        self.setData(path, DocumentationLibraryElement.Role.Path)
        self.setData(type_, DocumentationLibraryElement.Role.Type)
        self.setData(boxData, DocumentationLibraryElement.Role.BoxData)

    def hasChildNodeByName(self, childNodeName: str) -> bool:
        for rowIndex in range(self.rowCount()):
            child = self.child(rowIndex, 0)
            if child.data(DocumentationLibraryElement.Role.Title) == childNodeName:
                return True
        return False

    @staticmethod
    def fromPath(path: str, type: Type = Type.Document) -> QStandardItem:
        # Get basename
        title = os.path.splitext(os.path.basename(path))[0]

        return DocumentationLibraryElement(title, path, type)

class DocumentationDialog(AbstractDialog):

    def __init__(self, dialog_holder: Any, libraryItemPath: str = None):
        super().__init__(dialog_holder, "documentation", "Documentation", flags = Qt.WindowType.Window)

        # Init UI
        self.initUi()

        # Open path if a path is given
        if libraryItemPath is not None:
            self.openDocByPath(libraryItemPath)

    def initUi(self):
        # Size
        self.setMinimumSize(480, 360)
        self.resize(1280, 720)

        # Documentation List Tree View
        self.documentationTopicsTreeView = QTreeView()
        self.documentationTopicsTreeView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.documentationTopicsTreeView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.documentationTopicsTreeView.selectionChanged = self.onSelectedDocumentChanged
        self.documentationTopicsTreeView.setHeaderHidden(True)
        self.documentationTopicsTreeView.setAnimated(True)
        self.initTreeViewModel()

        # Documentation Topics list
        documentationTopicsResearchBar = QLineEdit()
        documentationTopicsResearchBar.textEdited.connect(self.filterDocumentationList)

        # Documentation List Layout
        documentationTopicsLayout = QVBoxLayout()
        documentationTopicsLayout.addWidget(documentationTopicsResearchBar)
        documentationTopicsLayout.addWidget(self.documentationTopicsTreeView, 1)
        documentationTopicsLayout.setContentsMargins(0, 0, 0, 0)

        # Documentation List Widget
        documentationTopicsWidget = QWidget()
        documentationTopicsWidget.setLayout(documentationTopicsLayout)
        documentationTopicsWidget.setMinimumWidth(300)

        # Document View
        self.documentView = WebView(WebView.Type.Markdown)
        self.documentView.setMinimumWidth(300)
        
        # Split view
        splitter = QSplitter()
        splitter.addWidget(documentationTopicsWidget)
        splitter.addWidget(self.documentView)
        splitter.setStretchFactor(1, 1)
        splitter.setCollapsible(0, True)
        splitter.setCollapsible(1, False)

        # Main Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(splitter, 1)

        self.setLayout(mainLayout)

    def filterDocumentationList(self, searchedString: str):
        # Build Regular Expression
        regExpression = QRegularExpression(searchedString, QRegularExpression.PatternOption.CaseInsensitiveOption)
        
        # Apply Regex Filtering
        self.proxyModel.setFilterRegularExpression(regExpression)

        if searchedString != "":
            self.documentationTopicsTreeView.expandAll()
        else:
            self.documentationTopicsTreeView.collapseAll()

            for selected_index in self.documentationTopicsTreeView.selectedIndexes():
                self.documentationTopicsTreeView.expandRecursively(selected_index)
                expanded_item_parent = selected_index.parent()

                while expanded_item_parent.row() != -1:
                    self.documentationTopicsTreeView.expand(expanded_item_parent)
                    expanded_item_parent = expanded_item_parent.parent()

    def getBoxesLibrariesElement(self) -> LibraryElement:
        # Box Libraries
        boxDatas: List[CodeBoxData] = [boxData for boxData in BoxesLibrariesManager().boxes]

        boxesRootElement = LibraryElement("Boxes")

        for boxData in boxDatas:
            # Reset current element
            currentElement = boxesRootElement

            # Get box tree
            print(boxData)
            boxTree = boxData.box_complete_name.split('.')

            # Remove "Boxes" from tree
            if boxTree[0] == "Boxes":
                boxTree.pop(0)

            while len(boxTree) > 0:
                # Pop box tree point from list
                boxPoint = boxTree.pop(0)

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

            if len(boxTree) == 0:
                if hasattr(boxData, "path"):
                    markdownPath = f"{boxData.path}.md"

                    currentElement.appendRow(
                            DocumentationLibraryElement(boxData.box_name, markdownPath, DocumentationLibraryElement.Type.Box, boxData)
                    )

        return boxesRootElement
    
    def getMuphynDocumentation(self) -> LibraryElement:
        # Init Library Element
        baseLibraryElement = LibraryElement("MuPhyN")

        # Get list of Markdown files
        docDirectory = os.path.join(ROOT_DIR, "docs")

        [\
            baseLibraryElement.appendRow(DocumentationLibraryElement.fromPath(os.path.join(docDirectory, file))) \
                for file in os.listdir(docDirectory) if file.endswith(".md")
        ]
    
        return baseLibraryElement
    
    def getSchedulersLibrariesElement(self) -> LibraryElement:
        # Init Scheduler root element
        schedulerRootElement = LibraryElement("Schedulers")

        schedulerDatas: List[SchedulerData] = list(SchedulersLibrariesManager().schedulers)

        for schedulerData in schedulerDatas:
            # Reset current element
            currentElement = schedulerRootElement
            
            # Get scheduler tree
            schedulerTree = schedulerData.scheduler_library.split('.')

            # Remove "Schedulers" from tree
            if schedulerTree[0] == "Schedulers":
                schedulerTree.pop(0)

            while len(schedulerTree) > 0:
                # Pop scheduler tree point from list
                schedulerPoint = schedulerTree.pop(0)

                # Check if node name already exists
                if currentElement.hasChildNodeByName(schedulerPoint):
                    # Get this node point
                    currentElement = currentElement.getChildByName(schedulerPoint)
                else:
                    # Create this node point
                    newElement = LibraryElement(schedulerPoint)

                    # Append new element
                    currentElement.appendRow(newElement)

                    # Go to the new Element
                    currentElement = newElement

            if len(schedulerTree) == 0:
                if hasattr(SchedulerData, "path"):
                    markdownPath = f"{SchedulerData.path}.md"

                    currentElement.appendRow(
                            DocumentationLibraryElement(schedulerData.scheduler_name, markdownPath, DocumentationLibraryElement.Type.Scheduler)
                    )

        return schedulerRootElement
    
    def getElementByPath(self, libraryItemPath: str):
        # Get splitted path
        itemPathTree: List[str] = libraryItemPath.split('.')

        # 
        rootItems = [self.proxyModel.index(rowIndex, 0).data() for rowIndex in range(self.proxyModel.rowCount())]

        if itemPathTree[0] in rootItems:
            # Init depth
            depth = 1

            # Get current depth path name
            currentDepthPath = itemPathTree[depth]

            # Current item
            currentItemIndex = self.proxyModel.index(rootItems.index(itemPathTree[0]), 0)

            # 
            while depth < len(itemPathTree):
                items = [self.proxyModel.index(rowIndex, 0, currentItemIndex).data() for rowIndex in range(self.proxyModel.rowCount(currentItemIndex))]
                if currentDepthPath in items:
                    depth += 1
                    currentItemIndex = self.proxyModel.index(items.index(currentDepthPath), 0, currentItemIndex)
                    if depth == len(itemPathTree):
                        return currentItemIndex
                    else:
                        currentDepthPath = itemPathTree[depth]
                else:
                    return None
        return None


    def initTreeViewModel(self):
        # Init Model
        tree_model: QStandardItemModel = QStandardItemModel()

        # Append Muphyn Documentation
        tree_model.appendRow(self.getMuphynDocumentation())

        # Append Box Libraries Documentation
        tree_model.appendRow(self.getBoxesLibrariesElement())

        # Append Scheduler Libraries Documentation
        tree_model.appendRow(self.getSchedulersLibrariesElement())

        # Init Filter Model
        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setSourceModel(tree_model)
        self.proxyModel.setRecursiveFilteringEnabled(True)

        self.documentationTopicsTreeView.setModel(self.proxyModel)

    def onSelectedDocumentChanged(self, selected: QItemSelection, deselected: QItemSelection):
        if selected.count() == 1:
            # Get Item Data
            itemModelIndex = selected.first().indexes()[0]
            itemData = self.proxyModel.itemData(itemModelIndex)

            if DocumentationLibraryElement.Role.Path in itemData:

                # Extract Url from ItemData
                urlString: str = itemData[DocumentationLibraryElement.Role.Path].replace("\\", "/")

                if os.path.exists(urlString):
                    # Load page from markdown file
                    self.documentView.loadUrlContent(urlString)
                else:
                    # Get item type
                    itemDataType = itemData[DocumentationLibraryElement.Role.Type]
                    
                    # Get document title
                    title: str = itemData[DocumentationLibraryElement.Role.Title].replace("\\", "/")
                    if itemDataType == DocumentationLibraryElement.Type.Box:
                        # Get box data
                        boxData = itemData[DocumentationLibraryElement.Role.BoxData]

                        # Build Generic Box Data Markdown
                        markdownContent = buildMarkdownFromBoxData(boxData)

                        self.documentView.setContent(markdownContent)
                    else:
                        self.documentView.setContent(f"No Markdown file found for **{title}** {itemDataType.value}")

    def openDocByPath(self, libraryItemPath: str):
        # Get model index
        index = self.getElementByPath(libraryItemPath)

        # Expand tree view
        if index is not None:
            # Set current index
            self.documentationTopicsTreeView.setCurrentIndex(index)

            # Expand tree view
            self.documentationTopicsTreeView.expandRecursively(index)
            expanded_item_parent = index.parent()
            while expanded_item_parent.row() != -1:
                self.documentationTopicsTreeView.expand(expanded_item_parent)
                expanded_item_parent = expanded_item_parent.parent()