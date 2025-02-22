#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_square_box_2 (box: Box, simulation_params: SchedulerParams) -> None :
    
    box['current_period'] = 0

    if not 'high_value' in box :
        box['high_value'] = 1.0

    if not 'low_value' in box :
        box['low_value'] = 0.0

    if not 'high_time' in box :
        box['high_time'] = 0.5

    if not 'low_time' in box :
        box['low_time'] = 0.5

    if not 'rise_time' in box: 
        box['rise_time'] = 0.01

    if not 'fall_time' in box: 
        box['fall_time'] = 0.01

    if box['fall_time'] == 0 :
        box['fall_slope'] = 1
    else :
        box['fall_slope'] = (box['low_value'] - box['high_value']) / box['fall_time']

    if box['rise_time'] == 0:
        box['rise_slope'] = 1
    else :
        box['rise_slope'] = (box['high_value'] - box['low_value'])  / box['rise_time']


    box['high_time'] = box['high_time'] - box['fall_time']
    box['fall_time'] = box['high_time'] + box['fall_time'] 
    box['low_time'] = box['low_time'] + box['fall_time'] - box['rise_time']
    box['rise_time'] = box['low_time'] + box['rise_time']


def _function_square_box_2 (box: Box, event_: SchedulerEvent) -> List : 

    if box['current_period'] < box['high_time'] :

        v = box['high_value']

    elif box['current_period'] < box['fall_time']:

        v = box['high_value'] + (box['fall_slope'] * (box['fall_time'] - box['current_period']))

    elif box['current_period'] < box['low_time']:
        
        v = box['low_value']

    elif box['current_period'] < box['rise_time']:

        v = box['low_value'] + (box['rise_slope'] * (box['rise_time'] - box['current_period']))
    
    else :

        v = box['high_value']
    
    box['current_period'] = box['current_period'] + event_.step_time

    while box['current_period'] >= box['rise_time'] :
        box['current_period'] = box['current_period'] - box['rise_time']

    return v