#Tutorial 2A QUESTION 1
# a function of two arguments that returns 1 if the first argument is negative, AND the second 
# argument otherwise. (aka  second argument is positive)
# Write a function in python called SMALLEST by modifying question 3b from tutorial 1b to take in 3
# numbers and return the smallest number.'''

def smallest(x, y, c):
        if x < y and x <= c:
                return(f"The smallest number is: {x}")
        elif y < x and y < c:
                return(f"The smallest number is: {y}")
        elif c < x and c < y:
            return(f"The smallest number is: {c}")
        else:
            return(f"The numbers entered, {x}, {y}, and {c} are equal. ")

        
print("This program returns the smallest of 3 numbers\n")
num1 = int(input("Enter a number \n"))          # prompts user for first number
num2 = int(input("Enter a second number \n"))   # prompts user for second number
num3 = int(input("Enter a third number \n"))
print((smallest(num1,num2,num3)))