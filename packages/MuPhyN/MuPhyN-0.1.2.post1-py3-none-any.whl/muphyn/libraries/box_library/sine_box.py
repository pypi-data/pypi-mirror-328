#-----------------------------------
# Imports
#-----------------------------------
from typing import List
from math import sin

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_sine_box (box: Box, simulation_params: SchedulerParams) -> None :

    if not 'amplitude' in box :
        box['amplitude'] = 1.0

    if not 'pulsation' in box :
        box['pulsation'] = 1.0
    
    if not 'phase' in box :
        box['phase'] = 0.0

def _function_sine_box (box: Box, event_: SchedulerEvent) -> List :     
    return box['amplitude'] * sin((event_.timing * box['pulsation']) + box['phase'] )