#-----------------------------------
# Imports
#-----------------------------------

from PyQt6.QtGui import QStandardItem

#-----------------------------------
# Class
#-----------------------------------

class LibraryElement (QStandardItem) :

    # -------------
    # Constructors
    # -------------

    def __init__ (self, label_name: str) :

        QStandardItem.__init__(self)

        self.setText(label_name)
        self.setEditable(False)

    def getChildByName(self, childNodeName: str) -> QStandardItem:
        for rowIndex in range(self.rowCount()):
            child = self.child(rowIndex, 0)
            if child.text() == childNodeName:
                return child
        return None

    def hasChildNodeByName(self, childNodeName: str) -> bool:
        for rowIndex in range(self.rowCount()):
            child = self.child(rowIndex, 0)
            if child.text() == childNodeName:
                return True
        return False