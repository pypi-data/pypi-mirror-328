#-----------------------------------
# Imports
#-----------------------------------

# General Imports
import os
import yaml

from PyQt6.QtWidgets import QFileDialog

# Project Imports
from muphyn.packages.core.base import LogManager
from muphyn.utils.appconstants import ApplicationWindowTitle

from ..editors.abstracteditor import AbstractEditor
from ..models.editablemodels.abstractboxmodel import AbstractEditableModel
from ..models.editablemodels.boxcodemodel import BoxCodeModel
from ..models.editablemodels.boxcompositemodel import BoxCompositeModel
from ..models.editablemodels.schedulermodel import SchedulerModel
from ..models.editablemodels.simulationmodel import SimulationModel

from .abstractexporter import AbstractExporter
from .abstractimporter import AbstractImporter
from .filters import saveFileFilter, defaultInitialFileFilter, getExtensionFromFilter
from .loadnloader import load as loadFile
from .simulationfiles.simulationexporter import SimulationExporter
from .simulationfiles.simulationimporter import SimulationsImporter

#-----------------------------------
# Functions
#-----------------------------------

def load (path : str) -> AbstractEditableModel :
    """Permet de charger le modèle se trouvant au chemin passé en paramètre."""
    
    # Init importer object
    importer : AbstractImporter = None

    # Load data
    dataDict = loadFile(path)

    if "simulation" in dataDict:
        importer = SimulationsImporter()
        data = dataDict['simulation']

    if importer is None : 
        return None
    
    name = os.path.splitext(os.path.basename(path))[0]

    return importer.open(data, path, name)

def save (model : AbstractEditableModel, path : str) -> bool :
    """Permet de sauvegarder le modèle au chemin passé en paramètre."""
    
    exporter : AbstractExporter = None

    if isinstance(model, SimulationModel):
        exporter = SimulationExporter()

    elif isinstance(model, BoxCompositeModel) :
        LogManager().debug('Save box composite !')
        raise Exception('no exporter found for box composite model')

    elif isinstance(model, SchedulerModel) :
        LogManager().debug('Save scheduler !')
        raise Exception('no exporter found for scheduler model')

    elif isinstance(model, BoxCodeModel) :
        LogManager().debug('Save box code !')
        raise Exception('no exporter found for box code model')

    return exporter.save(model, path)

def saveas (model : AbstractEditableModel) -> str :
    """Est la méthode appelée lorsque l'utilisateur veut sauvegarder le fichier en cours sous un nouveau nom."""

    # Get current project path
    defaultDir = os.getcwd() if model.path is None or len(model.path) == 0 else os.path.join(model.path, model.name)

    # 
    path, filter_ = QFileDialog.getSaveFileName(
        caption = f'{ApplicationWindowTitle} - Save as file',
        directory = defaultDir,
        filter = saveFileFilter,
        initialFilter = defaultInitialFileFilter
    )

    if path is None or len(path) == 0 :
        return None
    
    # Rebuild the path
    path = os.path.splitext(path)[0] + getExtensionFromFilter(filter_).value

    # Save model
    return path if save(model, path) else None

def export (editor : AbstractEditor, argument : str) :
    """Permet d'exporter l'éditeur sous une forme voulue."""