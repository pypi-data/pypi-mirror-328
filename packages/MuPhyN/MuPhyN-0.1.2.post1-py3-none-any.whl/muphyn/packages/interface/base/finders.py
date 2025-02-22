import typing

from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

def findMainWindow() -> typing.Union[QMainWindow, None]:
    # Global function to find the (open) QMainWindow in application
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None

def findWindowForWidget(widget: QWidget):

    while widget is not None:
        # Get window object
        windowHandle: QWindow = widget.window().windowHandle()

        # If we get window widget → return instance
        if windowHandle is not None:
            return windowHandle
        # else get widget parent
        else:
            widget = widget.parent()

    return None

def findScreenForWidget(widget: QWidget):
    while widget is not None:
        # Get window object
        windowHandle: QWindow = widget.window().windowHandle()

        if windowHandle is not None:
            # Get screen object
            screen = windowHandle.screen()
            if screen is not None:
                return screen
        else:
            widget = widget.parent()
    return None