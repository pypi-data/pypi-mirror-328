#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_print_box (box: Box, event_: SchedulerEvent):
    print(f"at {event_.timing:.3f}: {box.input_values}")
