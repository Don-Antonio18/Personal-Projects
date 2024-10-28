def power(base, exp):
    #basecase
    if exp == 0:
        return 1
    
    #function calls itself
    else:
        return base * power(base, exp -1 )
    
basenum = int(input("\nEnter power: "))
expnum = int(input("\nEnter exponent: "))
print (power(basenum, expnum))