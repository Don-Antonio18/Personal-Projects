'''
Write a recursive python function skip_power that accepts two integers n and k, as inputs
and returns the sum of all numbers starting from n down to 0 subtracting n by k each time.
Hint: If n is less than k return n otherwise return sum of n raised to the power k and use the
recursive call with a new value for the first parameter i.e. n minus k. Observe the examples
seen below as a guide.
'''
# Note: question said to return n if n < k, 
# but example used 0 as output


def skip_power(n, k):
    if n < k:
        return 0 # base case
    else:
    # returns n to the power of k, + new recursive call
    # new call uses new value for first parameter (n - k)
        return n ** k + skip_power(n-k, k)
    # when n is less than k, program stops the summing of numbers
    

    
