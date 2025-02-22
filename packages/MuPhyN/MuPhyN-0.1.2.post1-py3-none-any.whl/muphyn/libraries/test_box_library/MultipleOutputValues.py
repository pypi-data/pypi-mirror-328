#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
from typing import List


from muphyn import Box, BoxModel, SchedulerEvent


#-----------------------------------
# Functions
#-----------------------------------
def _step_simulation (box: Box, event_: SchedulerEvent) -> List :
    numberOfOutputs = len(box.outputSignals)
    return {"Default_0": 1, "Default_1": box["value"]}