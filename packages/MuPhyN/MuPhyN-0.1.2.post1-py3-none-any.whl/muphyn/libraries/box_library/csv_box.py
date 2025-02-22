#-----------------------------------
# Imports
#-----------------------------------
import pandas as pd
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_csv_box (box: Box, simulation_params: SchedulerParams):
    # Init Box values list
    box['values'] = []

    # Build column names
    box['titles'] = ["Time"] + [inputSignal.input_name for inputSignal in box.inputSignals]

def _function_csv_box (box: Box, event_: SchedulerEvent):
    if box['copy_timing_from_simulation'] is True or (event_.timing > box['start_time'] and event_.timing < box['stop_time']) :
        lst = [event_.timing] + [inputSignal.value for inputSignal in box.inputSignals]
        box['values'].append(lst)

    return None

def _end_csv_box (box: Box) -> None :
    df = pd.DataFrame(box["values"], columns=box["titles"])
    df.to_csv(box['file_name'], sep=box["delimiter"], decimal=box["decimal"], index=False)

