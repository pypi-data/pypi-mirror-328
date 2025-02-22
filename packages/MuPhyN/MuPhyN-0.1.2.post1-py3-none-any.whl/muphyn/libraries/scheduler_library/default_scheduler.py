#-----------------------------------
# Imports
#-----------------------------------
from typing import Any

from muphyn import Box, Scheduler, SchedulerEvent

#-----------------------------------
# Methods
#-----------------------------------

def _execute_box (scheduler: Scheduler, event: SchedulerEvent, box: Box) -> None:
    # Execute Box and get output value
    returned = box.function(event)
    
    # Determine if output is exception or not
    if scheduler.is_scheduler_exception(returned) :
        return returned

    # Build output events
    if returned is None:
        return

    for event in returned :
        
        scheduler.append_event(event)

        if event.signal in scheduler.diagram.linked_signals :

            for signal in scheduler.diagram.linked_signals[event.signal] :
                scheduler.append_event(scheduler.construct_signal_event(signal, event.box, event.new_signal_data))

def _default_scheduler_method (scheduler: Scheduler) -> Any :
    
    b_bis = None
    event = None
    b = None

    scheduler.savedEvents = []

    try :

        while scheduler.should_simulation_continue :
            
            for b in scheduler.diagram.boxes :
                # Execute box
                new_events = _execute_box(scheduler, scheduler.construct_event(), b)

                # Test if error while executing the box
                if scheduler.is_scheduler_exception(new_events) :
                    return new_events

                # While there are events to handle
                while scheduler.are_events_left :
                    
                    # Get first signal
                    event = scheduler.get_event(0)
                    event.signal.data = event.new_signal_data

                    # Save event
                    # scheduler.savedEvents.append(event)

                    if event.signal in scheduler.diagram.box_inputs :
                    
                        for b_bis in scheduler.diagram.box_inputs[event.signal] :
                            
                            new_events = _execute_box(scheduler, scheduler.construct_event(event), b_bis)
                            if scheduler.is_scheduler_exception(new_events) :
                                return new_events
                    
                    scheduler.remove_event(event)

            scheduler.stepping_time()

    except Exception as err :
        return scheduler.construct_exception(b, b_bis, event, err)