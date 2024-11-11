#   ID Number: 620170333
#   Hackerrank Handle: antoniokerruni
#   Hackerank Exercise: Simple Functions: Auto-Scheduler

#   Code submission from Hackerrank:


def busySchedule(sh, sm, eh, em, m):
    start_time = (sh * 60) + sm
    end_time = (eh * 60) + em
    
    if end_time < start_time:
        # there are 1440 minutes in a day
        # subtracting start_time from 1440 gives minutes left till midnight
        total_time = (1440 -  start_time) + end_time
    else:
        total_time = end_time - start_time

    if total_time >= m :
        remaining_time = total_time - m
        return remaining_time
    else:
        return -1
    
