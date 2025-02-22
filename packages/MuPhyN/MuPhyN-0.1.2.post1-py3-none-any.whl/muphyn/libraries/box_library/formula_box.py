#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from numbers import Number
import numexpr as ne

from muphyn import GlobalEnvVariablesManager, SchedulerParams, Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------
def _init_formula_box(box: Box, simulation_params: SchedulerParams):
    # Handle variables in formula
    formula: str = box["Formula"]

    # Replace all values
    for envVarName, envVar in GlobalEnvVariablesManager().global_vars.items():
        if isinstance(envVar, Number):
            formula = formula.replace(box["Formula"], envVarName, str(envVar))

    # Set box formula
    box["Formula"] = formula

def _function_formula_box (box: Box, event_: SchedulerEvent) -> List :
    # Add all input value to local env
    local_dict = {}
    for inputSignal in box.inputSignals:
        local_dict[inputSignal.input_name] = inputSignal.value

    # Get Formula
    formula = box["Formula"]

    # Calculate formula resolution
    v = float(ne.evaluate(formula, local_dict=local_dict))

    return v