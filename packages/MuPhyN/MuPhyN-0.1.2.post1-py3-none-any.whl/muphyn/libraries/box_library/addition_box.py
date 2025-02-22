#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_addition_box (box: Box, event_: SchedulerEvent):
    return np.sum(box.input_values)