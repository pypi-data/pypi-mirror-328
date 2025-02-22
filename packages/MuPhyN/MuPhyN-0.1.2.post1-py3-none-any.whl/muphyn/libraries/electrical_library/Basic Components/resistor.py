#-----------------------------------
# Imports
#-----------------------------------

from typing import List

#-----------------------------------
# Functions
#-----------------------------------

def _function_addition_box (box, event_) -> List:
    v = 0
    
    for input in box.inputSignals:
        v += input.value

    events : List = []
    
    for output in box.outputs :
        events.append(box.construct_signal_event(output, v))

    return events