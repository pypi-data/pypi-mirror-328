#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, BoxModel, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

import math

def _function_logarithm_box (box: Box, event_: SchedulerEvent) -> List:
    input_ = box.input_values[0]

    if input_ > 0:
        return math.log(input_, box["base"])
    else:
        raise(ValueError(f"Value must be strictly positive: {input_}"))