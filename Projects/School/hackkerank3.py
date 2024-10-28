#   ID Number: 620170333
#   Hackerrank Handle: antoniokerruni
#   Hackerank Exercise: Simple Functions: Auto-Scheduler

#   Code submission from Hackerrank:


def busySchedule(starting_hours, starting_minutes, ending_hours, ending_minutes, minutes):
    start_time = (starting_hours * 60) + starting_minutes
    end_time = (ending_hours * 60) + ending_minutes
    
    if end_time < start_time:
        # there are 1440 minutes in a day
        # subtracting start_time from 1440 gives minutes left till midnight
        total_time = (1440 -  start_time) + end_time
    else:
        total_time = end_time - start_time

    if total_time >= minutes :
        remainting_time = total_time - minutes
        return remainting_time
    else:
        return -1
    
