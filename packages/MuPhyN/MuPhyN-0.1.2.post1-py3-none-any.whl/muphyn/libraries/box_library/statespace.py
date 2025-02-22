# -----------------------------------
# Imports
# -----------------------------------
import scipy.signal as signal
from scipy.signal import StateSpace
from control import StateSpace, step_response, TimeResponseData

from muphyn import Box, SchedulerEvent, SchedulerParams, decodeArray

# Library imports

# -----------------------------------
# Functions
# -----------------------------------

def _init_state_space(box: Box, simulation_params: SchedulerParams) -> None:
    # Extract values
    A = decodeArray(box["A"])
    B = decodeArray(box["B"])
    C = decodeArray(box["C"])
    D = decodeArray(box["D"])

    # Init state space object
    box["stateSpace"] = StateSpace(A, B, C, D)

    # 
    box["lastState"] = decodeArray(box["Initial state"])
    box["lastTime"] = 0


def _function_state_space(box: Box, event_: SchedulerEvent):
    # Get last state
    lastState = box["lastState"]
    lastTime = box["lastTime"]
    times = (lastTime, event_.timing)

    # Step solve
    response = step_response(box["stateSpace"], times, lastState, return_x=True)

    # Get output
    y = response.y.squeeze()[1]
    
    # Update initial conditions
    box["lastTime"] = event_.timing
    box["lastState"] = response.x.squeeze().T[1]

    return y

def _end_state_space (box: Box) -> None :
    pass
