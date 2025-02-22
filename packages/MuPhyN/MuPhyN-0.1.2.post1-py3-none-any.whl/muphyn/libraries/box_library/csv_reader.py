# -----------------------------------
# Imports
# -----------------------------------
import pandas as pd
from typing import List
from PyQt6.QtCore import QSizeF

from muphyn import BoxModel, Box, SchedulerEvent, SchedulerParams
from muphyn.packages.core.base.utils.math import calc_precision

# Library imports
from utils.TransferFunction import TransferFunction

# -----------------------------------
# Functions
# -----------------------------------
def getCSVColumnNames(file: str, *, sep = ",", decimal = ".", index_col = None, 
        header = 0):
    return list(pd.read_csv(file, sep=sep, decimal=decimal, index_col=index_col, 
        header=header, nrows=0).columns)

def _on_file_selected(box_model: BoxModel) -> BoxModel:
    # Extract parameters
    modelPath = box_model.get_parameter("model_path")["value"]
    sep = box_model.get_parameter("separator")["value"]
    decimal = box_model.get_parameter("decimal")["value"]
    index_col = box_model.get_parameter("index column")["value"]
    header = box_model.get_parameter("header")["value"]

    # Init Simulation object 
    columns = getCSVColumnNames(modelPath, sep=sep, decimal=decimal, 
        index_col=index_col, header=header)
    
    # Set outputs
    for output_index, columnName in enumerate(columns):
        if output_index >= box_model.output_len:
            output = box_model.append_output("outputs")
            output.text = columnName
        else:
            box_model_outputs_group = box_model.get_outputs_group("outputs")
            output = box_model_outputs_group.outputs[output_index]
            output.text = columnName

    return box_model

def _init_csv_reader(box: Box, simulation_params: SchedulerParams) -> None:
    # Get simulation parameters
    startTime = 0.0
    stopTime = simulation_params.stop_time
    stepTime = simulation_params.step_time

    # Extract parameters
    modelPath = box.get_parameter("model_path")
    sep = box.get_parameter("separator")
    decimal = box.get_parameter("decimal")
    index_col = box.get_parameter("index column")
    header = box.get_parameter("header")

    # Load the whole DataFrame
    df = pd.read_csv(modelPath, sep=sep, decimal=decimal, index_col=index_col, header=header)

    # Limit DataFrame to the desired time range
    df = df[(df.index >= startTime) & (df.index <= stopTime)]

    # Convert float index to TimedeltaIndex
    df.index = pd.to_timedelta(df.index, unit='s')
    
    # Calculate the precision of the step time
    precision = calc_precision(stepTime)

    # Define the unit & multiplier
    unit, multiplier = ("s", 1)
    if precision > 6:
        unit, multiplier = ("ns", 1e9)
    elif precision > 3:
        unit, multiplier = ("us", 1e6)
    elif precision > 0:
        unit, multiplier = ("ms", 1e3)

    # Resample the indices
    df = df.resample(f"{stepTime * multiplier}{unit}").mean()
    df = df.interpolate()

    # Reconvert the indices to float
    df.index = df.index.total_seconds()

    # Store the dataframe
    box["DataFrame"] = df

def _function_csv_reader(box: Box, event_: SchedulerEvent):
    return box["DataFrame"].loc[event_.timing].values

def _end_csv_reader (box: Box) -> None :
    del box["DataFrame"]
