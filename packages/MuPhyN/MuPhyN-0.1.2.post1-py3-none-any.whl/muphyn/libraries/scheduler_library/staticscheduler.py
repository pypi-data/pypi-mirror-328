#-----------------------------------
# Imports
#-----------------------------------
import numpy as np
import pandas as pd
from typing import Any, Optional

from muphyn import Box, Scheduler, SchedulerEvent
from staticschedulerutils import BaseScheduler

#-----------------------------------
# Methods
#-----------------------------------

def _default_scheduler_method (scheduler: Scheduler) -> Any:
    # Init scheduler controller
    schedulerController = BaseScheduler(scheduler.stop_time, scheduler.step_time)

    # Init result dataFrame
    df: Optional[pd.DataFrame] = None

    # Add boxes to controller
    for box in scheduler.diagram.boxes:
        schedulerController.addBox(box)
        schedulerController.addConnection()

    # Add connections to controller
    # for signal in scheduler.diagram.signals:
    #     print(signal.input_name, signal.output_name)


    # # Solve system
    # startTime = perf_counter()
    # times, values = schedulerController.solve()
    # print(f"Solve took {perf_counter() - startTime:.6f}s")

    # # Reshape times
    # times: np.ndarray = times.reshape(-1, 1)

    # # Build DataFrame
    # dfRes = pd.DataFrame(np.concatenate([times, values], axis=1), columns=["times"] + [box.__class__.__name__ for box in schedulerController._boxes])
    # dfRes = dfRes.set_index("times")

    # # Rename all columns
    # dfRes.columns = [f"{schedulerClass.__name__}_{col}" for col in dfRes.columns]

    # #  
    # df = dfRes if df is None else df.merge(dfRes, how='outer', left_index = True, right_index = True)