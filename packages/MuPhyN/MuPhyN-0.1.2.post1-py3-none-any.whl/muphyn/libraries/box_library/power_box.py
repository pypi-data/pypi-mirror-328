#-----------------------------------
# Imports
#-----------------------------------
import numpy as np

from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_power_box (box: Box, event_: SchedulerEvent):
    return np.power(box.get_input(0).value, box["power"])