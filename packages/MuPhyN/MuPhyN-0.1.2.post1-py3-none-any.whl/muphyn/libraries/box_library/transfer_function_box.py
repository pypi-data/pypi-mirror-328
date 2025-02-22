# -----------------------------------
# Imports
# -----------------------------------
from typing import List
from scipy.integrate import solve_ivp

from PyQt6.QtCore import QSizeF

from muphyn import Box, BoxModel, SchedulerEvent, SchedulerParams, mathTex_to_QImage

# -----------------------------------
# Functions
# -----------------------------------
def _updateDisplayedValue(boxModel: BoxModel):
    num = get_coeff_vector(boxModel.get_parameter('numerator')["value"])
    numStr = ""
    for index in range(len(num)):
        degree = len(num) - index - 1
        coef = num [index]
        numStr += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            numStr += f" s^{degree}"
        elif degree == 1:
            numStr += " s"

    denom = get_coeff_vector(boxModel.get_parameter('denominator')["value"])
    denomStr = ""
    for index in range(len(denom)):
        degree = len(denom) - index - 1
        coef = denom [index]
        denomStr += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            denomStr += f" s^{degree}"
        elif degree == 1:
            denomStr += " s"

    nUnderscore = max(len(numStr), len(denomStr))
    underscoreText = '_' * nUnderscore

    boxText = f"{numStr}\n{underscoreText}\n{denomStr}"
    width = boxModel._font_metrics_used.horizontalAdvance(underscoreText)
    boxModel.setValue(boxText)
    boxModel.setSize(QSizeF(width, boxModel.size.height()))

def _update_icon(box_model: BoxModel):
    num = get_coeff_vector(box_model.get_parameter('numerator')["value"])
    num_str = ""
    for index in range(len(num)):
        degree = len(num) - index - 1
        coef = num [index]
        num_str += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            num_str += f" s^{degree}"
        elif degree == 1:
            num_str += " s"

    denom = get_coeff_vector(box_model.get_parameter('denominator')["value"])
    denom_str = ""
    for index in range(len(denom)):
        degree = len(denom) - index - 1
        coef = denom [index]
        denom_str += f"{' + ' if index != 0 else ''}{coef}" if coef >= 0 else f"-{-coef}"
        if degree > 1:
            denom_str += f" s^{degree}"
        elif degree == 1:
            denom_str += " s"

    math_eq = "$\\frac{" + num_str + "}{" + denom_str + "}$"

    # Get Math Expression Image
    image = mathTex_to_QImage(math_eq)

    # Update Box Model Icon
    box_model.setIcon(image)

    # Calculate new box size
    newBoxSize: QSizeF = QSizeF(80 * image.size().width() / image.size().height(), 80) - QSizeF(100, 0)
    box_model.setSize(newBoxSize)

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

def _function_transfer_function(box: Box, event_: SchedulerEvent):        

    if box['last_timing'] == event_.timing:    # if we are still on the current step, leave
        return None
    
    step = event_.step_time

    t0 = event_.timing

    t = [t0, t0 + step]                 # time vector is only current and next step
    sol = solve_ivp(f, t, box['last_y'], args=(box,), method='RK45', rtol=box['rtol'], atol=box['atol'])
    
    out = list(sol.y[:,-1])               # use the last values as the output of the step

    box['last_y'] = out

    box['last_timing'] = event_.timing

    return out[0]
