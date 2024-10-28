
def add_sub (a,b):
    if (a < b):
        return (f"Since the 1st num, {num}, was less than the 2nd num, {num2}, their sum is:", a + b)
    else:
        return (f"Since the 1st num, {num}, was greater than the 2nd num, {num2},  their subtraction is:  ", a - b)
    
num = int(input("Enter the first num "))
num2 = int(input("Enter the second num "))
print (add_sub(num,num2))