

                                                #QUESTION 3A 
#A function of one argument that returns double the value of the argument.

'''def double(arg):    #arg is a placeholder
    arg *= 2        #short way of doubling tbhe function
    return arg

user_input = int(input("what number do you want to double?  "))  
print()  
print(f"The number {user_input} when doubled turns into ", (double(user_input)))'''



                                                #QUESTION 3B
#A function of two arguments that returns the smaller of them.
'''def smaller(x,y):
    if x < y:
        return x
    return y
x = int(input("Enter x ")) 
y = int(input("Enter y ")) 
# function ^ returns x if it's smaller than y, else it returns y  '''


                                                    
                                                    #QUESTION 3C
# a function of two arguments that returns 1 if the first argument is negative, AND the second 
# argument otherwise. (aka  second argument is positive)'''

def tracker(x, y):
    return 1 if x < 0 and y >= 10 else 0 

print()
print("This program returns 1 if num1 is negative and both num2  and num3 are positive.")
print("Otherwise, it returns 0")
print()
num1 = int(input("Enter a number "))          # prompts user for first number
num2 = int(input("Enter a second number "))   # prompts user for second number
num3 = int(input("Enter a third number "))   # prompts user for third number
print()
print("The return value is", tracker(num1, num2, num3) ) 
