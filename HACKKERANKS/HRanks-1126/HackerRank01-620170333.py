#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def absAverage(a, b, c):
    # Write your code here
    avg = (abs(a) + abs(b) + abs(c))/ 3
    return avg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    c = int(first_multiple_input[2])

    avg = absAverage(a, b, c)

    fptr.write(str(avg) + '\n')

    fptr.close()
