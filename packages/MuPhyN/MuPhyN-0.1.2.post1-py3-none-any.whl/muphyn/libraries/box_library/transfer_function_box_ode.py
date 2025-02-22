# -----------------------------------
# Imports
# -----------------------------------

from typing import List
from scipy.integrate import odeint

from muphyn import Box, SchedulerEvent, SchedulerParams

# -----------------------------------
# Functions
# -----------------------------------

def get_coeff_vector(coeff_vector_string: str) -> List[float]:

    if coeff_vector_string is None:
        return [0]

    vector = []
    for sub in coeff_vector_string.split(' '):

        sub = sub.strip()
        if len(sub) == 0:
            continue

        try:
            vector.append(float(sub))
        except ValueError:
            ...

    return vector


def _init_transfer_function(box: Box, simulation_params: SchedulerParams) -> None:
    
    box['num_vect'] = get_coeff_vector(box['numerator'])
    box['num_vect'].reverse()
    box['num_order'] = len(box['num_vect']) - 1

    box['denom_vect'] = get_coeff_vector(box['denominator'])
    box['denom_vect'].reverse()
    box['denom_order'] = len(box['denom_vect']) - 1

    box['last_y'] = [box['initial_value']] + [0] * (box['denom_order'] -1) 
    
    box['last_timing'] = -1

def f(t: float, y: float, box: Box): 
    out = 0
    for j, coeff_y  in enumerate(box['denom_vect'][:-1]):
        out -= coeff_y * y[j]
    
    for j, coeff_y in enumerate(box['num_vect']):
        if j == 0:
            out += coeff_y * box.get_input(0).value
        else:
            out += coeff_y * y[j]
    
    out_vector = [y[box['denom_order'] - 1 - x] for x in range(box['denom_order'])]
    out_vector[-1] = out/box['denom_vect'][-1]

    return out_vector

def _function_transfer_function(box: Box, event_: SchedulerEvent) -> List :             

    if box['last_timing'] == event_.timing:    # if we are still on the current step, leave
        return None

    if box['last_timing'] == -1:
        box['last_timing'] = event_.timing

        # Set output value
        v = box['initial_value']
    else:
        step = event_.step_time

        t0 = event_.timing

        t = [t0, t0 + step]                 # time vector is only current and next step

        sol = odeint(f, t, box['last_y'], args=(box,))   # run odeint until next step
        
        out = list(sol[-1,:])               # use the last values as the output of the step

        box['last_y'] = out

        # Set output value
        v = out[0]

    box['last_timing'] = event_.timing

    return v
