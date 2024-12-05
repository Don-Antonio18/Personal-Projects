
import math
import os
import random
import re
import sys


def solve_processor_scheduling(cycle_limit, num_processes, process_cycles):
    
    process_queue = [(cycles, i+1) for i, cycles in enumerate(process_cycles)]
    
    current_time = 0
    
    while process_queue:
        # Get the next process from the front of the queue
        cycles_remaining, process_index = process_queue.pop(0)
        
        # Calculate how much work we can do this turn, either we complete the process or hit the cycle limit
        work_done = min(cycle_limit, cycles_remaining)
        
        # Add the time spent working
        current_time += work_done
        
        # Calculate remaining work after this turn
        cycles_after_work = cycles_remaining - work_done
        
        if cycles_after_work > 0:
            # Process not complete --> add it to back of queue with its remaining cycles
            process_queue.append((cycles_after_work, process_index))
        else:
            # Process is complete --> return the current time
            return current_time
    
    
    return -1

# if __name__ == '__main__':
#     # Read input for cycle limit (l) and number of processes (n)
#     ln = input().rstrip().split()
    
#     l = int(ln[0])
    
#     n = int(ln[1])
    
#     # Read the list of required cycles for each process
#     processes = list(map(int, input().rstrip().split()))
    
#     # Calculate and output result
#     result = solve_processor_scheduling(l, n, processes)
#     print(result)



