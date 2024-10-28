
def computedSquare(n):
    n = int(n)
    a = 1
    # 1 is the lowest square number, and so n must be 1 and up
    if n <= 0:
        return False
    #program checks range of a
    while a < n:
        #if a is greater than n, a^2 + b^2 cannot = n
        while a ** 2 <= n:
            b = 1

            #if b is greater than n, a^2 + b^2 cannot = n
            while b < n:
                #code checks if both squares add up to n
                if a ** 2 + b ** 2 ==  n:
                    return True
                b += 1 #code increments b
            a += 1 # code increments a
        # stops code if a is greater than n
        return False
num = int(input("\nEnter a number: "))
print (computedSquare(num))
                    
                    
            
    
