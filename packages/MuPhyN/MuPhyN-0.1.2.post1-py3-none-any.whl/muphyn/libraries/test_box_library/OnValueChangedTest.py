#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
from typing import List


from muphyn import Box, BoxModel, SchedulerEvent


"""
Notes:
 - If the initialization of the node is made in the _init_function then we won't access to the inputs first value 
    → (must implement a way to create firsts values)
 - If the outputs are read before the step is made we get one  step lag ;
 - If the inputs are set before the step then we get one step lag
"""
def _update_period(boxModel: BoxModel) -> None:
    if boxModel["frequency"] == 0.0:
        boxModel["period"] = np.inf
    else:
        boxModel["period"] = 1/boxModel["frequency"]

def _update_frequency(boxModel: BoxModel) -> None:
    if boxModel["period"] == 0.0:
        boxModel["frequency"] = np.inf
    else:
        boxModel["frequency"] = 1/boxModel["period"]

#-----------------------------------
# Functions
#-----------------------------------
def _step_simumation (box: Box, event_: SchedulerEvent) -> List :
    pass

def _finish_simulation (box: Box) -> List :
    for name, value in box.params.items():
        print(name, value)
    return None