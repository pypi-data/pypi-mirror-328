#-----------------------------------
# Imports
#-----------------------------------
from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_derivator_box (box: Box, simulation_params: SchedulerParams) -> None :
    box['last_input'] = 0
    box['last_time'] = None

def _function_derivator_box (box: Box, event_: SchedulerEvent):

    # Test if already executed
    if box['last_time'] == event_.timing:
        return None
    
    # Update last time
    box['last_time'] = event_.timing
    
    # Get current value
    currentInputValue = box.get_input(0).value

    # Calculate output value
    v = box["initialValue"] if event_.timing == 0 else (currentInputValue - box['last_input']) / event_.step_time

    return v