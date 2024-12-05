'''
The mathematical factorial function is defined as being the product of all the numbers up to
and including the argument, and the factorial of 1 is 1. Thinking about this, we see that another
way to express this is that the factorial of N is equal to N times the factorial of (N-1).
Thus,
1! = 1
2! = 2 x 1! = 2 x 1 = 2
3! = 3 x 2! = 3 x 2 x 1! = 3 x 2 x 1 =6
N! = N x (N-1)!= N x (N-1) x (N-2)! = N X (N-1) x (N-2)..1

Write a recursive function factorial in python which calculates the factorial of a number
given as input.
'''
def factorial(n):
    def bop(t, a):
        if t == a:
            return a
        return bop(t-1, a * t)
    return bop(n, 1)

number = int(input("\n Enter a number to get its factorial "))
print (f" {number}! = ", factorial(number))

#OR

def fact(n):
    t = n
    a = 1
    while t > 0:
        a *= t
        t -= 1
    return a

number = int(input("\n Enter a number to get its factorial "))
print (f" {number}! = ", fact(number))

#OR

def fac(n):
    if n == 1:   # since 1! = 1, you can use this conditional
        return 1
    else:
        return fac (n - 1) * n  # for each iteration it multiplies n by a lesser number till 1

number = int(input("\n Enter a number to get its factorial "))
print (f" {number}! = ", fac(number))

'''
Output:

fac (5)
5 * fac (4)
5 * 4 * fac (3)
5 * 4 * 3 * fac (2)
5 * 4 * 3 * 2 * fac (1)
5 8 4 * 3 * 2 * 1
    
it is computed as 5 x (4 x (3 x (2 x 1 )))
                = 5 x (4 x (3 x 2))
                = 5 x (4 x 6)
                = 5 x 24
                = 120


                


'''