#-----------------------------------
# Imports
#-----------------------------------
from muphyn.packages.core.base.managers import ManagerMetaClass


class GlobalEnvVariablesManager(metaclass=ManagerMetaClass) :
    """Est la classe qui permet de construire les boxes.""" 

    # -------------
    # Constructors
    # -------------
    def __init__ (self, global_vars: dict) :
        self.global_vars: dict = global_vars