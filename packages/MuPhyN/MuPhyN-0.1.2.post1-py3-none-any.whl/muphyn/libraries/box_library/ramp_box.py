#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_ramp_box (box: Box, simulation_params: SchedulerParams) -> None :

    if not 'start_time' in box :
        box['start_time'] = 0.0

    if not 'initial_value' in box :
        box['initial_value'] = 0.0

    if not 'slope' in box :
        box['slope'] = 1.0

def _function_ramp_box (box: Box, event_: SchedulerEvent) -> List : 
    if event_.timing < box['start_time']:
        v = box['initial_value']
    else:
        v = box['initial_value'] + ((event_.timing - box['start_time']) * box['slope'])

    return v