# ID Number: 620170333
# HackerRabnk Handle: antoniokerruni
# HackerRank Exercise: Easy Comnmute 
import math
import os
import random
import re
import sys

Map = [("A","B",4),("A","C",2),("B","C",5), ("B","D",10),("C","E",3),("E","D",4),("D","F",11)]
def getTime(A,B):
    for path in Map:
        if path[0] == A and path[1] == B:
            return path[2]
        elif path[0] == B and path[1] == A:
            return path[2]
    return -999

def travelTime(path):
    # add time between each sequence
    time_sum = getTime(path[0], path[1]) + getTime(path[1], path[2]) + getTime(path[2], path[3])
    
    # check for invalid paths
    if time_sum < 0:
        return -999
    
    else:
        # return sum of times between each sequence
        return time_sum
    