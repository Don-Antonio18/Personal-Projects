def test5(x,y):
    if x > 99:
        if y % 2 == 0:
            return x/y
        else:
            return x/(y+1)
    else:
        return x
    
print (test5(1000,3))