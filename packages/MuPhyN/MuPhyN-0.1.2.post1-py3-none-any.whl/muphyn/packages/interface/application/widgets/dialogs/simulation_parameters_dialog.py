#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from PyQt6.QtCore import QCoreApplication, pyqtSlot
from PyQt6.QtWidgets import QComboBox, QVBoxLayout, QPushButton, QGridLayout

from muphyn.packages.core.application import SchedulersLibrariesManager, SchedulerData, SchedulerParams
from muphyn.packages.interface.base import PlainButton, PropertyLabel, DoubleSpinBox

from ...models.editablemodels.schedulermodel import SchedulerModel
from ...models.editablemodels.simulationmodel import SimulationModel
from .abstract_dialog import AbstractDialog

#-----------------------------------
# Class
#-----------------------------------

class SimulationParametersDialog (AbstractDialog) :
    """Est la classe de dialogue qui permet de modifier les paramètres de la simulation."""
    
    # -------------
    # Constructors
    # -------------

    def __init__ (self, dialog_holder : Any, simulation_model : SimulationModel) :

        AbstractDialog.__init__(self, dialog_holder, 'simulation_parameters_dialog', QCoreApplication.translate(u'dlg_simulation_parameter', 'Simulation parameters', None))

        # Init dialog ui
        self.setFixedSize(370, 160)
        self.init_ui()
        self.tranlsate_ui()

        # Set simulation model information
        self.simulation_model = simulation_model


    # -------------
    # Properties
    # -------------

    @property 
    def simulation_model (self) -> SimulationModel :
        """Permet de récuperer le modèle de simulation."""
        return self._simulation_model

    @simulation_model.setter
    def simulation_model (self, simulation_model_ : SimulationModel) -> None :
        """Permet de modifier le modèle de simulation."""

        self._simulation_model = simulation_model_

        # If a simulation model has not been set
        if self._simulation_model is None : 
            # Disable all elements
            self._btn_accept.setEnabled(False)
            self._spn_simulation_tick.setEnabled(False)
            self._spn_simulation_time.setEnabled(False)
            self._cmb_scheduler.setEnabled(False)

            # Set default values
            self._spn_simulation_tick.setValue(0)
            self._spn_simulation_time.setValue(0)
            if self._cmb_scheduler.count() > 0 :
                self._cmb_scheduler.setCurrentIndex(0)

        # If a simulation model has been set
        else : 
            # Enable all items
            self._spn_simulation_tick.setEnabled(True)
            self._spn_simulation_time.setEnabled(True)
            self._cmb_scheduler.setEnabled(True)
            
            # If a scheduler model has not been set
            if self._simulation_model.scheduler_model is None :
                # Set default values
                self._spn_simulation_tick.setValue(10)
                self._spn_simulation_time.setValue(0.01)

            # If a scheduler model has been set
            else: 
                if self._simulation_model.scheduler_model.params is None : 
                    # Set default values
                    self._cmb_scheduler.setCurrentIndex(0)
                    self._spn_simulation_tick.setValue(10)
                    self._spn_simulation_time.setValue(0.01)
                    
                else:
                    # Set UI items with scheduler model values
                    self._cmb_scheduler.setCurrentIndex(self.getCurrentValueIndex(self._simulation_model.scheduler_model))
                    self._spn_simulation_tick.setValue(self._simulation_model.scheduler_model.params.step_time)
                    self._spn_simulation_time.setValue(self._simulation_model.scheduler_model.params.stop_time)
        
        self.check_changed()

    # -------------
    # Methods
    # -------------

    @pyqtSlot()
    def button_accept_clicked (self) -> None :
        """Est la méthode appelée quand l'utilisateur clique sur le bouton accepter du dialogue."""
        
        scheduler_data : SchedulerData = self._cmb_scheduler.currentData() 
        scheduler_params = SchedulerParams(self._spn_simulation_time.value(), self._spn_simulation_tick.value())
        self._value = SchedulerModel(scheduler_data.scheduler_library, scheduler_data.scheduler_name, scheduler_params)
        self.close()

    @pyqtSlot()
    def button_cancel_clicked (self) -> None : 
        """Est la méthode appelée quand l'utilisateur clique sur le bouton annuler du dialogue."""
        self.close()

    @pyqtSlot()
    def check_changed (self) -> None : 
        """Est la méthode appelée quand l'utilisateur modifie un élément graphique. La méthode débloque alors le bouton accepter si il y a quelque chose de modifié."""

        if self.simulation_model is None or not(self._cmb_scheduler.count() > 0) :
            self._btn_accept.setEnabled(False)
            return

        if self.simulation_model.scheduler_model is None : 

            if not(self._cmb_scheduler.currentIndex() == -1) :
                self._btn_accept.setEnabled(True)
            
            else :
                self._btn_accept.setEnabled(False)

            return

        if self.simulation_model.scheduler_model.params is None : 
            self._btn_accept.setEnabled(True)
            return 

        # If Simulation Duration time is zero or Step time is zero → invalid value
        if self._spn_simulation_tick.value() == 0 or self._spn_simulation_time.value() == 0 :
            self._btn_accept.setEnabled(False)
            return

        # If Step time is greater than simulation time → invalid value
        if self._spn_simulation_time.value()  < self._spn_simulation_tick.value() : 
            self._btn_accept.setEnabled(False)
            return

        # If Scheduler is different from set parameters → enable button
        if self.simulation_model.scheduler_model.completeName != self._cmb_scheduler.currentText():
            self._btn_accept.setEnabled(True)
            return

        # If Step Time is different from set parameters → enable button
        if self.simulation_model.scheduler_model.params.step_time != self._spn_simulation_tick.value() :
            self._btn_accept.setEnabled(True)
            return

        # If Stop Time is different from set parameters → enable button
        if self.simulation_model.scheduler_model.params.stop_time != self._spn_simulation_time.value() :
            self._btn_accept.setEnabled(True)
            return

        # Disable accept button
        self._btn_accept.setEnabled(False)

    def getCurrentValueIndex(self, schedulerModel: SchedulerModel) -> int:
        for index in range(self._cmb_scheduler.count()):
            if self._cmb_scheduler.itemData(index).completeName == schedulerModel.completeName:
                return index
        return -1


    def init_ui (self) -> None :
        """Est la méthode appelée pour initialiser les éléments de l'interface graphique."""

        if self.objectName() is None : 
            self.setObjectName('dlg_simulation_parameter')

        mainLayout = QVBoxLayout()

        # Options Layout
        optionsLayout = QGridLayout()

        # Buttons Layout
        buttonsLayout = QGridLayout()
        buttonsLayout.setColumnMinimumWidth(1, 90)
        buttonsLayout.setColumnMinimumWidth(2, 90)
        buttonsLayout.setHorizontalSpacing(5)

        # Scheduler
        self._lbl_scheduler : PropertyLabel = PropertyLabel()
        self._cmb_scheduler : QComboBox = QComboBox()
        for scheduler_data in SchedulersLibrariesManager().schedulers :
            self._cmb_scheduler.addItem(scheduler_data.__str__(), scheduler_data)
        self._cmb_scheduler.currentIndexChanged.connect(self.check_changed)

        # Time Value
        self._lbl_simulation_time : PropertyLabel = PropertyLabel()
        self._spn_simulation_time : DoubleSpinBox = DoubleSpinBox()
        self._spn_simulation_time.setMinimum(0)
        self._spn_simulation_time.valueChanged.connect(self.check_changed)

        # Step Time Value
        self._lbl_simulation_tick : PropertyLabel = PropertyLabel()
        self._spn_simulation_tick : DoubleSpinBox = DoubleSpinBox()
        self._spn_simulation_tick.setMinimum(0)
        self._spn_simulation_tick.valueChanged.connect(self.check_changed)

        # Accept button
        self._btn_accept : QPushButton = PlainButton()
        self._btn_accept.clicked.connect(self.button_accept_clicked)

        # Cancel Button
        self._btn_cancel : QPushButton = QPushButton()
        self._btn_cancel.clicked.connect(self.button_cancel_clicked)
        
        # Add option widgets to layout
        optionsLayout.addWidget(self._lbl_scheduler, 0, 0)
        optionsLayout.addWidget(self._cmb_scheduler, 0, 1)
        optionsLayout.addWidget(self._lbl_simulation_time, 1, 0)
        optionsLayout.addWidget(self._spn_simulation_time, 1, 1)
        optionsLayout.addWidget(self._lbl_simulation_tick, 2, 0)
        optionsLayout.addWidget(self._spn_simulation_tick, 2, 1)
        optionsLayout.setColumnStretch(1, 1)

        # Add buttons to layout
        buttonsLayout.addWidget(self._btn_accept, 0, 1)
        buttonsLayout.addWidget(self._btn_cancel, 0, 2)
        buttonsLayout.setColumnStretch(0, 1)

        # Add Options Layout to Main Layout
        mainLayout.addLayout(optionsLayout, 1)

        # Add Buttons Layout to Main Layout
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

    def tranlsate_ui (self) -> None : 
        """Est la méthode pour traduire les éléments de l'interface graphique."""

        self._lbl_scheduler.setText(QCoreApplication.translate(self.objectName(), u'Scheduler : ', None))
        self._lbl_simulation_time.setText(QCoreApplication.translate(self.objectName(), u'Duration time [s] :', None))
        self._lbl_simulation_tick.setText(QCoreApplication.translate(self.objectName(), u'Step time [s] :', None))
        self._btn_accept.setText(QCoreApplication.translate(self.objectName(), u'Accept', None))
        self._btn_cancel.setText(QCoreApplication.translate(self.objectName(), u'Cancel', None))