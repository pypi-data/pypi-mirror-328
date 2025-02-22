#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent


"""
Notes:
 - If the initialization of the node is made in the _init_function then we won't access to the inputs first value 
    → (must implement a way to create firsts values)
 - If the outputs are read before the step is made we get one  step lag ;
 - If the inputs are set before the step then we get one step lag
"""

#-----------------------------------
# Functions
#-----------------------------------

def _step_simumation (box: Box, event_: SchedulerEvent) -> List :
    return 0


def _finish_simulation (box: Box) -> List :

    for inputSignal in box.inputSignals:
        print(inputSignal)