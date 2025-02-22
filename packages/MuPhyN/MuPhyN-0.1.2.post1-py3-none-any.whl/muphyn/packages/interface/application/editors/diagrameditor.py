#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import ctypes, yaml, time
from typing import Iterable, List

# PyQt6 Imports
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, pyqtSignal, QPointF, QThread
from PyQt6.QtGui import QPainter, QClipboard
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsSceneDragDropEvent, QGraphicsView, QTabWidget, QApplication, QGridLayout

# Project Imports
import muphyn.packages.interface.application.files.simulationfiles.simulationexporter as simulationexporter
from muphyn.packages.core.application import AbstractBoxData, Scheduler
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.base import findMainWindow
from muphyn.packages.parser.parser import Parser
from ..actions.graphicalactions.diagram_add_graphical_element_action import DiagramAddGraphicalElementAction
from ..actions.graphicalactions.diagram_paste_graphical_element_action import DiagramPasteGraphicalElementAction
from ..actions.graphicalactions.diagram_remove_graphical_element_action import DiagramRemoveGraphicalElementAction
from ..actions.graphicalactions.diagram_rotate_graphical_element_action import DiagramRotateGraphicalElementAction
from ..holders.actions_holder import ActionsHolder
from ..editors.abstracteditor import AbstractEditor
from ..models.editablemodels.abstractdiagrammodel import AbstractDiagramModel
from ..models.graphicalmodels.boxmodel.abstractboxmodel import AbstractBoxModel
from ..models.graphicalmodels.abstractgraphicalelement import AbstractGraphicalElement
from ..models.graphicalmodels.boxmodel.boxmodel import BoxModel
from ..models.graphicalmodels.resizers.abstractresizer import AbstractResizer
from ..models.linksmodel.abstractlinkmodel import AbstractLinkModel
from ..models.signalsmodel.inputconnectionmodel import InputConnectionModel
from ..models.signalsmodel.outputconnectionmodel import OutputConnectionModel
from ..widgets.simulationcontroltoolbar import SimulationControlToolbar
from ..widgets.menus.rightclickmenu import rightClickContextMenu, RightClickContextMenu

#-----------------------------------
# Classes
#-----------------------------------

class SceneEditor (QGraphicsScene) :
    """Est la scéne graphique dans laquelle les éléments sont dessinés."""    

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, diagram_editor : QGraphicsView, actions_holder : ActionsHolder, diagram_model : AbstractDiagramModel) :

        QGraphicsScene.__init__(self, diagram_editor)
        self._diagram_editor = diagram_editor
        self._actions_holder = actions_holder
        self._diagram_model = diagram_model
        self.setParent(diagram_editor)

    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur d'action."""
        return self._actions_holder

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model

    # -------------
    # Methods
    # -------------

    def dropEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        if event.mimeData().hasUrls() :
            parent = self.parent()
            next_parent = parent.parent()

            while not(next_parent is None) :
                parent = next_parent
                next_parent = parent.parent()

            for url in event.mimeData().urls() :
                mainWindow = findMainWindow()
                if mainWindow is not None:
                    mainWindow.open_file(url.toLocalFile())
                # self._diagram_editor.open_file(url.toLocalFile())

        else :
            # Multiple boxes dropped
            if event.possibleActions() == Qt.DropAction.CopyAction and event.mimeData().data("action") == "new boxes":
                lenDroppedBoxes = int(event.mimeData().data("len"))

                for boxIndex in range(lenDroppedBoxes):
                    # Get Box mime data
                    boxData: AbstractBoxData = ctypes.cast(int(event.mimeData().data(f"box_data.{boxIndex}")), ctypes.py_object).value
                    offsetX, offsetY = [float(offset) for offset in event.mimeData().data(f"offset.{boxIndex}").split(b";")]

                    # Calculate Box Position
                    newBoxPosition = event.scenePos() + QPointF(offsetX, offsetY)

                    # Add box
                    action = DiagramAddGraphicalElementAction(self._diagram_editor._diagram_model, [{"box_data": boxData, "pos": newBoxPosition}])
                    action.do()
                    self.actions_holder.append(action)
        
                # Accept event
                event.accept()

            # Single box dropped
            elif event.possibleActions() == Qt.DropAction.CopyAction and event.mimeData().data("action") == "new box":
                # Get box data
                box_data : AbstractBoxData = ctypes.cast(int(event.mimeData().data("box_data")), ctypes.py_object).value

                # Add box
                action = DiagramAddGraphicalElementAction(self._diagram_editor._diagram_model, [{"box_data": box_data, "pos": event.scenePos()}])
                action.do()
                self.actions_holder.append(action)
        
                # Accept event
                event.accept()

            else :
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if hasattr(graphical_element, 'inputs') :
                        for input in graphical_element.inputs :
                            if input.isUnderMouse() :
                                input.dropEvent(event)
                                if event.isAccepted() :
                                    return

        super().dropEvent(event)

    def dragEnterEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        
        if event.mimeData().hasUrls() :
            event.accept()
        
        else :

            if event.possibleActions() == Qt.DropAction.CopyAction and event.mimeData().data('action') == 'new box' :
                    event.accept()
            
            if not(event.isAccepted()) : 
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if hasattr(graphical_element, 'inputs') :
                        for input in graphical_element.inputs :
                            if input.isUnderMouse() :
                                input.dragEnterEvent(event)
                                if event.isAccepted() :
                                    return
            
        super().dragEnterEvent(event)
            
    
    def dragMoveEvent (self, event : QGraphicsSceneDragDropEvent) -> None :
        
        if event.mimeData().hasUrls() :
            event.accept()

        else :
            if event.possibleActions() == Qt.DropAction.CopyAction and event.mimeData().data('action') == 'new box' :
                event.accept()
            else :
                for graphical_element in self.parent()._diagram_model.graphical_elements :
                    if isinstance(graphical_element, AbstractBoxModel) :
                        if hasattr(graphical_element, 'inputs') :
                            for input in graphical_element.inputs :
                                if input.isUnderMouse() :
                                    input.dragMoveEvent(event)
                                    if event.isAccepted() :
                                        return

        super().dragEnterEvent(event)

    def selected_elements (self) -> Iterable :
        """Permet de récuperer les éléments sélectionnés dans l'interface."""

        for item in self.selectedItems() :
            if isinstance(item, AbstractGraphicalElement) :
                if isinstance(item, AbstractResizer) :
                    continue

                yield item


class GraphicsView (QGraphicsView) :
    """Est la vue graphique dans laquelle la scène graphique est placée.""" 

    # -------------
    # Signals
    # -------------
    
    elements_selected_changed = pyqtSignal(object)

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self, actions_holder : ActionsHolder, diagram_model : AbstractDiagramModel, graphical_editor : AbstractEditor = None) : 

        QGraphicsView.__init__(self, graphical_editor)

        self._diagram_model : AbstractDiagramModel = diagram_model 
        self._graphical_editor = graphical_editor
        self._actions_holder = actions_holder

        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)

        self._diagram_model.scene = SceneEditor(self, actions_holder, diagram_model)
        self._diagram_model.scene.selectionChanged.connect(self.scene_elements_selected_changed)
        
        self.setScene(self._diagram_model.scene)

        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self._sliding_mouse_event_started =  False

        self.setRenderHint(QPainter.RenderHint.Antialiasing, on=True)
        self.setRenderHint(QPainter.RenderHint.TextAntialiasing, on=True)

    # -------------
    # Properties
    # -------------

    @property
    def actions_holder (self) -> ActionsHolder :
        """Permet de récuperer le conteneur d'action."""
        return self._actions_holder

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model

    # -------------
    # Methods
    # -------------
    def add_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet d'ajouter un élément graphique à l'interface."""

        if graphical_element is None :
            return

        self._diagram_model.add_element(graphical_element)

    def rem_graphical_element (self, graphical_element : AbstractGraphicalElement) -> None :
        """Permet de supprimer un élément graphique de l'interface."""

        self._diagram_model.remove_element(graphical_element)
        graphical_element.deleteLater()

    
    def mousePressEvent (self, event : QtGui.QMouseEvent):
        """Est l'événement appelée lorsque l'utilisateur appuie sur un bouton de sa souris."""


        if event.button() == Qt.MouseButton.MiddleButton :
            self.__prevMousePos = event.pos()
            self._sliding_mouse_event_started = True
            event.accept()

        elif event.button() == Qt.MouseButton.RightButton:
            while QApplication.overrideCursor() is not None:
                QApplication.restoreOverrideCursor()
            graphical_element_under_mouse = None
            for graphical_element in self.parent()._diagram_model.graphical_elements :
                if graphical_element.isUnderMouse():
                    graphical_element_under_mouse = graphical_element
                    break

            # If Right Click on Box
            contextMenu = rightClickContextMenu(graphical_element_under_mouse, self)
            selectedActionType: RightClickContextMenu.Type = contextMenu.openContextMenu(event.globalPosition())

            # Remove Selected Items
            if selectedActionType == RightClickContextMenu.Type.RemoveSelectedItems:
                selectedElements = list(self.selected_elements())
                if len(selectedElements) > 0:
                    action = DiagramRemoveGraphicalElementAction(self._diagram_model, selectedElements)
                    action.do()
                    self.actions_holder.append(action)

            # Delete Item under mouse
            elif selectedActionType == RightClickContextMenu.Type.DeleteItem:
                action = DiagramRemoveGraphicalElementAction(self._diagram_model, [graphical_element_under_mouse])
                action.do()
                self.actions_holder.append(action)

            # Rotate Item Left
            elif selectedActionType == RightClickContextMenu.Type.RotateLeftItem:
                new_rotation = (graphical_element_under_mouse.rotation() - 90) % 360
                action = DiagramRotateGraphicalElementAction(graphical_element_under_mouse, graphical_element_under_mouse.rotation(), new_rotation)
                action.do()
                self.actions_holder.append(action)

            # Rotate Item Right
            elif selectedActionType == RightClickContextMenu.Type.RotateRightItem:
                new_rotation = (graphical_element_under_mouse.rotation() + 90) % 360
                action = DiagramRotateGraphicalElementAction(graphical_element_under_mouse, graphical_element_under_mouse.rotation(), new_rotation)
                action.do()
                self.actions_holder.append(action)

            # Open Simulation Panel
            elif selectedActionType == RightClickContextMenu.Type.OpenBoxDocumentation:
                mainWindow = findMainWindow()
                mainWindow._help_documentation_method(graphical_element_under_mouse.completeLibrary)

            # No action selected
            else:
                pass
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent (self, event : QtGui.QMouseEvent) :
        """Est l'événement appelée lorsque l'utilisateur bouge sa souris dans l'élément graphique."""
        
        if event.buttons() == Qt.MouseButton.MiddleButton :
            
            if not(self._sliding_mouse_event_started) :
                self.__prevMousePos = event.pos()
                self._sliding_mouse_event_started = True
            
            else :
                offset = self.__prevMousePos - event.pos()
                self.__prevMousePos = event.pos()

                self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
                self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())

            event.accept()

        else:
            return super().mouseMoveEvent(event)


    def mouseReleaseEvent (self, event: QtGui.QMouseEvent) -> None :
        """Est l'événement appelée lorsque l'utilisateur relache un bouton de sa souris."""

        if event.button() == Qt.MouseButton.MiddleButton :
            self._sliding_mouse_event_started = False
            event.accept()

        else :
            return super().mouseReleaseEvent(event)

    def wheelEvent (self, event: QtGui.QWheelEvent) -> None :
        """Est l'événement appelée lorsque l'utilisateur bouge sa souris dans l'élément graphique."""

        if event.modifiers() == Qt.KeyboardModifier.ControlModifier :

            self.zoom(event.angleDelta().y() / 120)
            event.accept()

        else :
            super().wheelEvent(event) 

    def zoom (self, value : int) -> None :
        
        if value == 0 :
            value = 1

        elif value > 0 :
            value *= 1.125

        elif value < 0 :
            value *= -0.825
        
        self.scale(value, value)

    def scene_elements_selected_changed (self) -> None :
        """Est la méthode appelée lorsque l'utilisateur modifie la sélection d'éléments à l'écran."""
        self.elements_selected_changed.emit(self.selected_elements)
    
    def selected_elements (self) -> Iterable :
        """Permet de récuperer les éléments sélectionnés dans l'interface."""
        
        for item in self._diagram_model.scene.selected_elements() :
            yield item

class DiagramEditor (AbstractEditor) :
    """Est l'élément graphique capable d'éditer des simulation ou des boxes composites.""" 


    # -------------
    # Constructors
    # -------------

    def __init__ (self, tab_holder : QTabWidget, diagram_model : AbstractDiagramModel, actions_holder : ActionsHolder) :

        AbstractEditor.__init__(self, tab_holder, diagram_model, actions_holder)

        # Add diagram Model to tab
        self._diagram_model = diagram_model
        self._diagram_model.elementDoubleClicked.connect(self.elementDoubleClicked)
        
        # Init Ui
        self.initUI()

    # -------------
    # Properties
    # -------------

    @property
    def diagram_model (self) -> AbstractDiagramModel :
        """Permet de récuperer le modèle content diagramme en cours d'édition."""
        return self._diagram_model 
    
    # -------------
    # Methods
    # -------------

    def initUI(self):
        # Enable Mouse Tracking
        self.setMouseTracking(True)

        # Create Graphics View
        self._graphics_view : GraphicsView = GraphicsView(self._actions_holder, self._diagram_model)

        # Connect Selection changed event
        self._graphics_view.elements_selected_changed.connect(self.graphics_view_elements_selected_changed)

        # Init simulation runner controls
        self._controlToolBar = SimulationControlToolbar()
        self._controlToolBar.playButtonClicked.connect(self.startSimulation)
        self._controlToolBar.stopButtonClicked.connect(self.stopSimulation)

        # Grid Layout
        gridLayout = QGridLayout()
        gridLayout.addWidget(self._graphics_view, 0, 0, 2, 3)
        gridLayout.addWidget(self._controlToolBar, 0, 1)

        # Grid Layout set constraints
        gridLayout.setRowStretch(1, 1)
        gridLayout.setRowMinimumHeight(0, 40)
        gridLayout.setColumnStretch(0, 1)
        gridLayout.setColumnStretch(2, 1)
        gridLayout.setColumnMinimumWidth(1, 300)

        # Add Layout to item
        self.setLayout(gridLayout)

    def startSimulation(self):
        # Grab focus to force all other items to leave focus
        self._controlToolBar.setFocus()
        
        # Check is tab has valid editable model
        if self.editable_model is None:
            return
        
        # Print Start Simulation
        LogManager().info(f"{'='*10} Start Simulation for {self.editable_model.name} {'='*10}", is_global_message=True)
        
        # Get Global Starting Time
        self.globalStartTime = time.perf_counter()

        # Init Parser
        parser = Parser()

        # Parse
        self._scheduler : Scheduler = parser.parse(self.editable_model)
        
        if self._scheduler is None : 
            LogManager().error('No self._scheduler returned for the simulation !!')

        else :
            # Init the simulation
            self._thread = QThread(self)
            self._scheduler.moveToThread(self._thread)

            # Connect signals
            self._thread.started.connect(self._scheduler.doWork) # Start simulation
            self._thread.finished.connect(self.endSimulation) # Finish simulation
            self._scheduler.finished.connect(self._thread.quit) # End Scheduler
            QApplication.instance().aboutToQuit.connect(self._thread.exit) # Quit application
            self._scheduler.progressed.connect(self._controlToolBar.updateProgression) # Update progress bar

            # Run the simulation
            self._thread.start()

    def stopSimulation(self):
        if hasattr(self, "_thread") and self._thread is not None:
            self._scheduler.requestEnd()

    def endSimulation(self):
        startingEndPhaseTime = time.perf_counter()

        # Execute ending stuff
        schedulerException = self._scheduler.endSimuation()
        if schedulerException is not None :
            LogManager().error(f"The simulation encoutered an error after {time.perf_counter() - startingEndPhaseTime:.6f}s of simulation.")
            schedulerException.print()

        LogManager().info(f"Simulation Ending Time: {time.perf_counter() - startingEndPhaseTime:.6f}s", is_global_message=True)

        # Delete scheduler & thread
        self._thread.deleteLater()

        # Terminate progress bar
        self._controlToolBar.progressionFinished()

        # Print total time
        LogManager().info(f"Simulation Global Time: {time.perf_counter() - self.globalStartTime:.6f}s", is_global_message=True)

        # Print End of Simulation
        LogManager().info(f"{'='*10} End Simulation {'='*10}", is_global_message=True)

    def copy (self) -> None :
        
        serializer = {}
        serializer['MuPhyN'] = {}
        serializer['MuPhyN']['boxes'] = []
        serializer['MuPhyN']['signals'] = []

        box_copied = []
        for box_model in self.selected_elements() :
            if isinstance(box_model, BoxModel) :

                if not(box_model in box_copied) : 
                    box_copied.append(box_model)
                
        link_copied : List[AbstractLinkModel] = []
        for link_model in self.selected_elements() :
            if isinstance(link_model, AbstractLinkModel) :

                if link_model.input.parent() in box_copied and link_model.output.parent() in box_copied :
                
                    if link_model in link_copied :
                        continue

                    link_dict = simulationexporter.export_signal(len(link_copied), link_model)
                    serializer['MuPhyN']['signals'].append(link_dict)
                    link_copied.append(link_model)

        for box_model in box_copied :
            # Convert box to dict
            box_dict = box_model.to_dict()

            # Add box dict to serializer
            serializer['MuPhyN']['boxes'].append(box_dict)
        
        cb: QClipboard = QApplication.clipboard()
        cb.clear(mode = QClipboard.Mode.Clipboard)
        cb.setText(yaml.dump(serializer).__str__())

    def cut (self) -> None :
        
        self.copy()
        self.delete_selection()

    def paste (self) -> None :

        cb = QApplication.clipboard()
        cb_text = cb.text().strip()

        if cb_text.__len__() == 0 :
            return

        action = DiagramPasteGraphicalElementAction(self, self.diagram_model, cb_text)
        action.do()
        self.actions_holder.append(action)

    def graphics_view_elements_selected_changed (self, elements) -> None :
        """Est la méthode appelée lorsque l'utilisateur change la sélection."""
        self.elements_selected_changed.emit(elements)
    
    def selected_elements (self) -> Iterable :
        for item in self._graphics_view.selected_elements() :
            yield item

    def unslect_elements (self) -> None :
        for el in self.selected_elements() :
            el.setSelected(False) 

    def elements (self) -> Iterable[AbstractGraphicalElement] :
        for chld in self._graphics_view._diagram_model._graphical_elements :
            if isinstance(chld, AbstractGraphicalElement) :

                if isinstance(chld, InputConnectionModel) or isinstance(chld, OutputConnectionModel) :
                    continue

                yield chld 

    def zoom (self, value : int) -> None :
        self._graphics_view.zoom(value)

    def elementDoubleClicked(self, box: AbstractBoxModel):
        if hasattr(self, "_scheduler") and self._scheduler is not None and hasattr(self._scheduler, "savedEvents"):
            pass

    def add_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.add_graphical_element(graphical_element)
        
    def rem_item (self, graphical_element : AbstractGraphicalElement) -> None :
        self._graphics_view.rem_graphical_element(graphical_element)

    def delete_selection (self) -> None :
        action = DiagramRemoveGraphicalElementAction(self._graphics_view._diagram_model, self.selected_elements())
        action.do()
        self.actions_holder.append(action)

    def clear (self) -> None :
        to_delete = []
        for el in self.elements() :
            if isinstance(el, AbstractLinkModel) :
                continue
            to_delete.append(el)

        for el in to_delete :
            self.rem_item(el)