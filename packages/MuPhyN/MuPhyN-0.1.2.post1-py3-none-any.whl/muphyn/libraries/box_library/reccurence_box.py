#-----------------------------------
# Imports
#-----------------------------------
from typing import List

from muphyn import Box, SchedulerEvent, SchedulerParams

#-----------------------------------
# Functions
#-----------------------------------

def _init_reccurence_box (box: Box, simulation_params: SchedulerParams) :

    box['values'] = []
    box['points_count'] = 0

    if len(box.inputSignals) == 0 :
        box._wait_for_all_signal_events = False
        box._wait_for_events = False
    
    box['values'].append([])

    for x in box.inputSignals :
        box['values'].append([])

def _function_reccurence_box (box: Box, event_: SchedulerEvent) -> List:
    v = 0

    # Pour chaque entrée ajouter la valeur actuelle dans la liste.
    i = 1
    for input in box.inputSignals:
        box['values'][i].insert(0, input.value)
        i += 1
    
    box['points_count'] = box['points_count'] + 1

    # Récuperation de la valeur indépenndante
    if len(box['coefficients']) > 0:
        if len(box['coefficients'][0]) > 0 :
            v = box['coefficients'][0][0]
    
    # Anciennes valeurs de sorties
    for j in range(min(len(box['coefficients'][0])-1, len(box['values'][0]))):
        v += box['coefficients'][0][j + 1] * box['values'][0][j]

    # Anciennes valeurs des entrées
    for input_index in range(min((len(box['values']) - 1), (len(box['coefficients']) - 1))) :
        values_index_count = min((len(box['coefficients'][input_index + 1])), (len(box['values'][input_index + 1])))

        for value_index in range(values_index_count) :
            v += (box['coefficients'][input_index + 1][value_index]) * (box['values'][input_index + 1][value_index]) 
    
    # Ajout de la valeur aux anciennes valeurs.
    box['values'][0].insert(0, v)
    
    return v