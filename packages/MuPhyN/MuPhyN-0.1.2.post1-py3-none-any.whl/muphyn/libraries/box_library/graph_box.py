#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, BoxModel, SchedulerEvent, SchedulerParams, GraphDialog

#-----------------------------------
# Functions
#-----------------------------------

def _init_graph_box (box: BoxModel, simulation_params: SchedulerParams) -> None :
    box['data_x'] = []
    box['data_y'] = {input_.input_name: [] for input_ in box.inputSignals}

    box['point_count'] = 0

    if not 'title' in box :
        box['title'] = str(box.name) + " " + str(box.index)
    
    if not 'label_x' in box :
        box['label_x'] = ' '

    if not 'label_y' in box :
        box['label_y'] = ' '

    if not 'start_time' in box :
        box['start_time'] = 1.0

    if not 'stop_time' in box : 
        box['stop_time'] = 100.0
    
    box['window'] = None

def _function_graph_box (box: Box, event_: SchedulerEvent) -> List:
    
    if box['copy_timing_from_simulation'] is True or (event_.timing > box['start_time'] and event_.timing < box['stop_time']) :
        box['data_x'].append(event_.timing)
        
        for inputSignal in box.inputSignals :
            box['data_y'][inputSignal.input_name].append(inputSignal.value)

        box['point_count'] = box['point_count'] + 1

    return None

def _end_graph_box (box: Box) -> None :
    box["graphDialog"] = GraphDialog(box)
    box["graphDialog"].show()