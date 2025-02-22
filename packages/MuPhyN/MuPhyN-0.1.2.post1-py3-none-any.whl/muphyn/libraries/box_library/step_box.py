#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_step_box (box: Box, simulation_params: SchedulerParams) -> None :

    if not 'step_time' in box :
        box['step_time'] = 1.0

    if not 'start_value' in box :
        box['start_value'] = 0.0

    if not 'stop_value' in box :
        box['stop_value'] = 1.0

def _function_step_box (box: Box, event_: SchedulerEvent) -> List : 
    if event_.timing < box['step_time']:
        v = box['start_value']
    else:
        v = box['stop_value']

    return v