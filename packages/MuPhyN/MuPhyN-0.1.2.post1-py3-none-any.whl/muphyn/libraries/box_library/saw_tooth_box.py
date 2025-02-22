#-----------------------------------
# Imports
#-----------------------------------
from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_saw_tooth_box (box: Box, simulation_params: SchedulerParams) -> None :

    if not 'amplitude' in box :
        box['amplitude'] = 1.0

    if not 'slope' in box :
        box['slope'] = 1.0
    
    if not 'mean_value' in box :
        box['mean_value'] = 0.0

    box['period'] = box['amplitude'] / box['slope']
    if box['period'] < 0 :
        box['period'] = - box['period']

    box['current_period'] = 0.0
    box['start_value'] = box['mean_value'] - box['amplitude'] / 2

def _function_saw_tooth_box (box: Box, event_: SchedulerEvent):
    
    if event_.timing == 0 :
        box['current_period'] = 0.0
    else :
        box['current_period'] = box['current_period'] + event_.step_time

    if box['current_period'] > box['period'] :
        box['current_period'] = box['current_period'] - box['period']

    v = box['start_value'] + box['current_period'] * box['slope']
    
    return v