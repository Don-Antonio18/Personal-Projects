'''write square root of a given perfect square without using inbuilt functions'''
import math
def sq_root(x):
    
    ans = 0
    while ans * ans < x:
        ans += 1
    return (ans)

number = int(input("Enter a number and we will calculate its square root: "))
print(f"The square root of {number} is ",sq_root(number))
print(f"The square root of {number} is ",math.sqrt(number))