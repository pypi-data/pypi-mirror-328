from PyQt6.QtWidgets import QMessageBox, QPushButton

from muphyn.utils.appconstants import ApplicationWindowTitle
from ..base.buttons import PlainButton

class YesNoMessageBox(QMessageBox):

    def __init__(self, question: str, title: str=ApplicationWindowTitle, parent = None):
        super().__init__(parent)

        # Set Question Text
        self.setText(question)

        # Set Title
        self.setWindowTitle(title)

        # Add buttons
        self.addButton(PlainButton(text="Oui"), QMessageBox.ButtonRole.AcceptRole)
        self.addButton(QPushButton(text="Non"), QMessageBox.ButtonRole.RejectRole)
