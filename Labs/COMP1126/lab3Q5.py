'''
Write in python code, the function skip_valid_power which accepts two parameters: a and
b and returns a Boolean value. Using skip_power function from question 4 with parameters
a and b, return the value and perform the following validation checks:
I. If this value is between the range 1000-999999 (inclusive) and,
II. The sum of the digits (use: sumDigits) is divisible by 7 then return True and False
otherwise.
>>>skip_valid_power(10,4)
True
>>>skip_valid_power(12,6)
False 
'''
import sys
from lab3Q4 import skip_power
from lab3Q3 import sumDigits

def skip_power(n, k):
    if n < k:
        return 0
    else:
        return n ** k + skip_power(n - k, k)

sys.setrecursionlimit(20000)

def skip_valid_power(a, b):
    
        result = skip_power(a, b)
        
        if 1000 <= result <= 1000000 and sumDigits(result) % 7 == 0:
            return True
        return False


        
