'''Complete the function power in python that raises an integer num to its nth power and returns that
value. If num is less than or equal to 0 then the function should return 0. (Don’t use the inbuilt
python exponentiation operator).
e.g.
power(3) = 27
3^3 = 3*3^2
3^2 = 3*3^1
3^1 = 3*3^0
3^0 = 1
def power2(num):
def helper(num,pow):
…
…
else:
return helper(pow,pow)
'''

def power(num):
    def helper(num, pow):
        if pow == 0:
            return 1
        else:
            return num * helper(num, pow-1)
        
    if num <= 0:
        return 0
    else:
        return helper(num,num)
print (power(3))

            

