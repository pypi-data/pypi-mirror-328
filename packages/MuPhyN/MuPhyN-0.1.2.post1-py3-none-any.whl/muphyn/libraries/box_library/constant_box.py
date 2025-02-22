#-----------------------------------
# Imports
#-----------------------------------
from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _init_constant_box (box, simulation_params) -> None :
    
    if not 'Constant Value' in box :
        box['Constant Value'] = 1

def _function_constant_box (box: Box, event_: SchedulerEvent):
    return box['Constant Value']