from lab3Q2 import div 
from lab3Q2 import mod
'''
Given a number n as an
argument the function lastDigit returns the last digit of that number and allButLast
returns the number with its last digit taken off. Write a recursive function sumDigits which
uses these two functions and sums all digits in a given number. 
'''
def lastDigit(n): 
    return mod(n, 10) # returns last digit of number
        # same as saying n % 10

def allButLast(n):
    return div(n,10) # removes last digit from number
        # same as saying n // 10

def sumDigits(n):
    if n < 10:  # base case, since only 1 digit will remain
        return n
    else:
    # gives sum of : the last digit + the rest of the number through allButLast
        return lastDigit(n) + sumDigits(allButLast(n))
    
