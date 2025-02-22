import os
from typing import Union

from PyQt6.QtCore import pyqtSignal, QDir, QUrl, Qt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView

class WebEnginePage(QWebEnginePage):

    linkClicked = pyqtSignal(QUrl)

    def __init__(self, profile: QWebEngineProfile, parent = None):
        super().__init__(profile, parent)

    def acceptNavigationRequest(self, url: QUrl, type_: QWebEnginePage.NavigationType, isMainFrame: bool) -> bool:
        if type_ == QWebEnginePage.NavigationType.NavigationTypeLinkClicked:
            self.linkClicked.emit(url)
        return super().acceptNavigationRequest(url, type_, isMainFrame)
    
    def fromQWebEnginePage(webEnginePage: QWebEnginePage):
        return WebEnginePage(webEnginePage.profile(), webEnginePage.parent())

class WebEngineView(QWebEngineView):

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setContentsMargins(2, 2, 2, 2)

        # Init web engine page
        page = WebEnginePage.fromQWebEnginePage(self.page())
        self.setPage(page)
        page.linkClicked.connect(self.onLinkClicked)

    def loadUrlContent(self, url: Union[str, QUrl]):
        # Get url string
        urlString = WebEngineView.getUrlString(url)
        
        # Get base url
        baseUrl = QUrl.fromLocalFile(os.path.dirname(urlString) + "/")

        # Get markdown content
        markdownContent = WebEngineView.getFileContent(url)

        # Display HTML
        self.setContentData(markdownContent, baseUrl)

    def setContentData(self, content: str, baseUrl: QUrl):
        return self.setHtmlContent(content, baseUrl)
    
    def setHtmlContent(self, html: str, baseUrl: QUrl):
        self.page().setHtml(html, baseUrl)

    def onLinkClicked(self, url: QUrl):
        # Handle file link
        urlString = WebEngineView.getUrlString(url)
        if urlString.startswith("file:///"):
            url.setUrl(urlString.removeprefix("file:///"))
            self.loadUrlContent(url)

    @staticmethod
    def calculateRelativePath(targetPath: str, sourceDir: str):
        return f"./{QDir(sourceDir[1:]).relativeFilePath(targetPath)}"

    @staticmethod
    def getUrlString(url: Union[str, QUrl]):
        if isinstance(url, QUrl):
            return url.toString()
        elif isinstance(url, str):
            return url
        else:
            raise(TypeError(f"Unsupported url type: {type(url)}"))

    @staticmethod
    def getFileContent(url: Union[str, QUrl]):
        # Get url string
        urlString = WebEngineView.getUrlString(url)
        
        # Load HTML file
        if os.path.exists(urlString):

            with open(urlString, "r") as file:
                # Read HTML File
                fileContent = file.read()

            return fileContent