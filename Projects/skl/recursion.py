def sumTo(n):
    if n == 1:
        return 1
    else:
        return sumTo(n-1) + n 
    
print (sumTo(3))