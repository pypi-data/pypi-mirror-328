#-----------------------------------
# Imports
#-----------------------------------
import numpy as np

from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_divide_box (box: Box, event_: SchedulerEvent):
    input_values = box.input_values
    if len(input_values) == 2:
        if input_values[1] != 0.0:
            return input_values[0] / input_values[1]
        else:
            raise(ValueError(f"Denominator value is Zero"))
    else:
        raise(ValueError(f"Divide box must have only two input values: {len(input_values)}"))
    return np.prod(box.input_values)