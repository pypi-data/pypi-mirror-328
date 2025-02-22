from PyQt6.QtWidgets import QLabel, QTabWidget

from ..holders.actions_holder import ActionsHolder
from ..models.editablemodels.abstracteditablemodel import AbstractEditableModel

from .abstracteditor import AbstractEditor
from .boxdataeditor import BoxDataEditor
from .codeeditor import CodeEditor
from .diagrameditor import DiagramEditor

def factory_editors (tab_holder : QTabWidget, editable_model : AbstractEditableModel) -> AbstractEditor :
    
    if hasattr(editable_model, 'editor_type') :

        if editable_model.editor_type == 'code-editor' :
            return CodeEditor(tab_holder, editable_model, ActionsHolder())
        
        elif editable_model.editor_type == 'box-data-editor' :
            return BoxDataEditor(tab_holder, editable_model, ActionsHolder())
        
        elif editable_model.editor_type == 'diagram-editor' :
            return DiagramEditor(tab_holder, editable_model, ActionsHolder())

    lbl : QLabel = QLabel(tab_holder)
    lbl.setText('No editor')
    return lbl