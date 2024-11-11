
#* CAPTURING THE SUMMATION OF A SERIES of INTEGERS
def sumIntegers(start, stop):
    if start > stop: return 0 # stops recursing & loops back thru
        # returns num + next num in series 
    else: 
        return start + sumIntegers(start + 1, stop)
    
    
#* CAPTURING THE SUMMATION OF SQUARES
def sqr(n): return n ** 2

def sumSquares(start, stop):
    if start > stop: return 0 # stops recursing & loops back thru
        # returns num + next num in series 
    else: 
        return sqr(start) + sumSquares(start + 1, stop)


#* CAPTURING THE SUMMATION OF RECIPROCALS
def sqReciprocal(x): return 1/ (x * x)

def piSum(start, stop):
    if start > stop: return 0 # stops recursing & loops back thru
        # returns num + next num in series 
    else: 
        return sqReciprocal(start) + piSum(start + 2, stop)


