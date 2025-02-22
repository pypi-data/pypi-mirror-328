#-----------------------------------
# Imports
#-----------------------------------
import numpy as np

from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_multiplier_box (box: Box, event_: SchedulerEvent):
    return np.prod(box.input_values)