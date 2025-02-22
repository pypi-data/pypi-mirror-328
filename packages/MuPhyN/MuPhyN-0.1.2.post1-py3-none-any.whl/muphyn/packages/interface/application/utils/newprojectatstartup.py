#-----------------------------------
# Imports
#-----------------------------------
 
import os
import pathlib
from datetime import date

from PyQt6.QtCore import QCoreApplication

from muphyn.packages.core.application import SchedulersLibrariesManager, SchedulerParams

from ..models.editablemodels.simulationmodel import SimulationModel 
from ..models.editablemodels.schedulermodel import SchedulerModel 
from ..userdata import UserData

#-----------------------------------
# Functions
#-----------------------------------

newProjectPath = pathlib.Path(__file__).parent.parent.parent.absolute().__str__() + os.sep.__str__()

def newProjectOnStartup (user_data : UserData) -> SimulationModel :
    """Permet de créer un nouveau projet vide au démarrage du projet."""

    name = QCoreApplication.translate("_new_project_on_startup", "New Project", None)
    path = newProjectPath
    
    creator = user_data.user_name
    _date = date.today() 
    version = 1.0

    step_time = 0.1
    stop_time = 10
    
    scheduler = None
    for sch in SchedulersLibrariesManager().schedulers :
        scheduler = sch
        break

    scheduler_params = SchedulerParams(stop_time, step_time)
    if not(scheduler is None) :
        scheduler_model : SchedulerModel = SchedulerModel(scheduler.scheduler_library, scheduler.scheduler_name, scheduler_params)
    else : 
        scheduler_model : SchedulerModel = SchedulerModel('', '', scheduler_params)
    
    return SimulationModel(name, path, creator, _date, version, scheduler_model)