#number should recurse until number hits 0

def sum(n):
    # base case
    if n < 1: 
        return 0
    else:
        # prints sum of all numbers less than n, including n
        return n + sum(n - 1)

#print (sum(4))


def factoral(n):
    # base case: factorial of 0 is 1
    if n < 1:
        return 1
    else:
        # multiplies each number below n by the next decrementing number
        return n * factoral(n-1)

#print (factoral(4))


def fibonacci(num):
    # base case:
    return ( 
            1 if num == 1 
            else 0 if num == 0 
            else fibonacci(num-1) + fibonacci (num-2) 
            )
print (fibonacci(9))

        
""" Write a recursive function reverse_string(s) 
that takes a string s as input and returns the reversed string."""

def reverse_string(s):
    # base cases:
    return (
        "invalid string" if not isinstance(s, str)
        else s if len(s) < 1
        else s if len(s) == 1
        # return last index of string then add substring using negative step, excluding the last char
        else s[-1] + reverse_string(s[:-1])
    )
print (reverse_string("Antonio"))


"""Write a recursive function sum_list(lst) that takes a list of numbers as input and 
returns the sum of all the numbers in the list."""

def sum_list(lst):
    return (
        "not a list" if not isinstance(lst, list)
        else lst[0] if len(lst) == 1
        else 0 if lst == []
        # returns first index in list, then appends second index onwards
        else lst[0] + sum_list(lst[1:])
    )
nums = [5,3]
print (sum_list(nums))