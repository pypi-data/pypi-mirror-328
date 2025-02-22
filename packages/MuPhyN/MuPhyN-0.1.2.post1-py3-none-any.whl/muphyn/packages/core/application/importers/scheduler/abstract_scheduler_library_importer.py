#-----------------------------------
# Imports
#-----------------------------------

from typing import Dict

from ...scheduler.scheduler_library_data import SchedulerData

#-----------------------------------
# Class
#-----------------------------------

class AbstractSchedulerLibraryImporter : 
    """Est la classe commune des classes capable d'importer des planificateur."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self) :
        ...

    # -------------
    # Methods
    # -------------

    def import_scheduler_data (self, path : str, file_name : str, absolute_yaml_file : str, schedulers : Dict[str, SchedulerData]) -> Dict[str, SchedulerData] :
        ...