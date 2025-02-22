
from PyQt6.QtWidgets import QLabel, QTabWidget

from ..holders.actions_holder import ActionsHolder
from ..models.editablemodels.abstractcodemodel import AbstractCodeModel

from .abstracteditor import AbstractEditor

class CodeEditor (AbstractEditor) :
    
    def __init__(self, tab_holder : QTabWidget, code_model : AbstractCodeModel, actions_holder : ActionsHolder) :
        AbstractEditor.__init__(self, tab_holder, code_model, actions_holder)
        
        self.lbl : QLabel = QLabel(self)
        self.lbl.setText('code editor')