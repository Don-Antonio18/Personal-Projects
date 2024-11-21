'''write square root of a given perfect square without using inbuilt functions'''
import math
                #! x to the power of 0.5 gives square root 
def sq_root(x): return (f"The square root of {x} is {x ** 0.5}")

number = int(input("Enter a number and we will calculate its square root: "))
print (sq_root(number))

#* function that returns square of a number:
def sqr(n): return n ** 2