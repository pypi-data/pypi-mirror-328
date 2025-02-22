from typing import Union


from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtWidgets import QGridLayout, QWidget

from muphyn.packages.core.base import Enum
from ...base.buttons import ArrowButton
from .markdownview import MarkdownView
from .webengineview import WebEngineView

class WebView(QWidget):

    loadFinished = pyqtSignal()

    class Type(Enum):
        Default = 0
        Markdown = 1

    def __init__(self, type_: Type, parent: QWidget = None) -> None:
        super().__init__(parent, Qt.WindowType.Widget)

        # Web engine view
        if not isinstance(type_, WebView.Type) or type_ not in WebView.Type.keys():
            raise(TypeError(f"Unsupported web engine view type: {type_}"))

        self._type = type_

        # Init UI
        self.initUI()

    def initUI(self):
        # Init widget layout
        widgetLayout = QGridLayout()

        # Init web engine view
        if self._type == WebView.Type.Markdown:
            self._webEngineView = MarkdownView()
        else:
            self._webEngineView = WebEngineView()
        self._webEngineView.loadStarted.connect(self.onLoadStarted)
        self._webEngineView.loadFinished.connect(self.onLoadFinished)

        # Init back button
        self._backButton = ArrowButton(ArrowButton.Direction.Left)
        self._backButton.clicked.connect(self.onBackButtonClicked)
        
        # Init forward button
        self._forwardButton = ArrowButton(ArrowButton.Direction.Right)
        self._forwardButton.clicked.connect(self.onForwardButtonClicked)
        
        self.updateButtonsState()

        # Add items to layout
        widgetLayout.addWidget(self._webEngineView, 0, 0, 2, 3)
        widgetLayout.addWidget(self._backButton, 0, 0)
        widgetLayout.addWidget(self._forwardButton, 0, 1)
        widgetLayout.setRowMinimumHeight(0, 20)
        widgetLayout.setRowStretch(1, 1)
        widgetLayout.setColumnStretch(2, 1)

        # Set main layout
        self.setLayout(widgetLayout)

    def goBack(self):
        if self.canGoBack():
            self._webEngineView.back()
            self.updateButtonsState()

    def goForward(self):
        if self.canGoForward():
            self._webEngineView.forward()
            self.updateButtonsState()
        
    def canGoBack(self) -> bool:
        return self._webEngineView.history().canGoBack()

    def canGoForward(self) -> bool:
        return self._webEngineView.history().canGoForward()
    
    def loadUrlContent(self, url: Union[str, QUrl]):
        self._webEngineView.loadUrlContent(url)

    def setContent(self, content: str):
        self._webEngineView.setContentData(content)

    def updateButtonsState(self):
        self._backButton.setEnabled(self.canGoBack())
        self._forwardButton.setEnabled(self.canGoForward())


    def onBackButtonClicked(self):
        self.goBack()

    def onForwardButtonClicked(self):
        self.goForward()

    def onLoadStarted(self):
        # Disable buttons
        self._backButton.setEnabled(False)
        self._forwardButton.setEnabled(False)

    def onLoadFinished(self, ok: bool):
        self.updateButtonsState()