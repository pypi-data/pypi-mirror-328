#-----------------------------------
# Imports
#-----------------------------------
from typing import List
from random import seed, random

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_noise_box (box: Box, simulation_params: SchedulerParams) -> List : 
    
    if box['apply_seed'] :
        seed(box['seed'])

    box['min'] = box['mean_value'] - (box['amplitude'] / 2)

def _function_noise_box (box: Box, event_: SchedulerEvent) -> List :
    return box['amplitude'] * random() + box['min']