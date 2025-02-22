#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_low_pass_filter (box: Box, simulation_params: SchedulerParams) -> None :
    cut_pulstation = box['cut_frequency'] * 2 * np.pi

    box['num_vect'] = [1]
    box['num_vect'].reverse()
    box['num_order'] = 1
    box['last_u_derivatives'] = [0 for _ in box['num_vect']]

    box['denom_vect'] = [1/cut_pulstation, 1]
    box['denom_vect'].reverse()
    box['denom_order'] = 1
    box['last_y_derivatives'] = [0 for _ in box['denom_vect']]

    box['order'] = 1
    box['order_coeff'] = 1

    box['last_y'] = 0
    box['last_timing'] = -1

def _function_low_pass_filter (box: Box, event_: SchedulerEvent) -> List :
    
    v = 0
    current_u_derivatives = []
    current_y_derivatives = []
    input_value = box.get_input(0).value

    if box['last_timing'] == event_.timing :
        return None
    box['last_timing'] = event_.timing

    for j, coeff_u in enumerate(box['num_vect']) : 

        if j == 0 : 
            v += coeff_u * input_value
            current_u_derivatives.append(input_value)
        
        else :
            derivative = (current_u_derivatives[j - 1] - box['last_u_derivatives'][j - 1]) / event_.step_time
            v += coeff_u * derivative
            current_u_derivatives.append(derivative)

    if box['order'] > 0 :

        for j in range(box['order']) :

            coeff_y = box['denom_vect'][j]

            if j == 0 :
                v -= coeff_y * box['last_y']
                current_y_derivatives.append(box['last_y'])

            else :
                derivative = (current_y_derivatives[j - 1] - box['last_y_derivatives'][j - 1]) / event_.step_time
                v -= coeff_y * derivative
                current_y_derivatives.append(derivative)

        v /= box['order_coeff']

        for j in range(box['order']).__reversed__() :
            v *= event_.step_time
            v += current_y_derivatives[j]

    else :
        v /= box['order_coeff']

    box['last_u_derivatives'] = current_u_derivatives
    box['last_y_derivatives'] = current_y_derivatives
    box['last_y'] = v

    """
    while (len(box['last_y_s']) > box['denom_order']) :
        del box['last_y_s'][0]
    """

    return v
