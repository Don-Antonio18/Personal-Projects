def f1(x):
    if x == 0:
        return True
    else:
        return f2(x - 1)
    
def f2(x):
    if x == 0:
        return False
    else:
        return f1(x - 1)
    
print (f1(5))