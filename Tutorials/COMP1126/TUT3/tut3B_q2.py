''' 
Write a recursive function in python that takes a number as argument and 
returns the SUMof all
even numbers between 1 and num. 

'''

def sumEven(num):
    if num <= 1:
        return 0
    if num % 2 == 0:
        return num + sumEven(num-1)
    else:
        return sumEven(num-1)

number  = int(input("\n Enter a number: "))
print (f"\nThe sum of even numbers between 1 & {number} = ",  (sumEven(number)) )