#-----------------------------------
# Imports
#-----------------------------------

from typing import List
import math

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_square_box_1 (box: Box, simulation_params: SchedulerParams) -> None :
    
    box['current_period'] = 0
    box['period_max'] = (math.pi * 2) / box['pulsation']
    box['switch_period'] = box['period_max'] * box['duty_cycle']
    box['high_value'] = box['mean_value'] + (box['amplitude'] / 2)
    box['low_value'] = box['mean_value'] - (box['amplitude'] / 2)


def _function_square_box_1 (box: Box, event_: SchedulerEvent) -> List : 

    if event_.timing == 0 :
        box['current_period'] = 0
    else :
        box['current_period'] = box['current_period'] + event_.step_time

    while box['current_period'] >= box['period_max'] :
        box['current_period'] = box['current_period'] - box['period_max']
        
    if box['current_period'] < box['switch_period'] :
        v = box['low_value']

    elif box['current_period'] >= box['switch_period'] :
        v = box['high_value']

    return v