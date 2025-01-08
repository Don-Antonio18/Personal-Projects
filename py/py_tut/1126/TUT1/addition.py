def add(x,y):                                                #x and y are placeholders for values
    sum = x + y
    return sum                                                 # prompts the program to return the sum value of the 2 variables
print()
print("Okay bud. Gimme two numbers and i'll add em for ya.")
print()
try:                                                           #using try because user might enter smth that is not a number
    user_input1 = int(input("Gimme the first number:  "))       # prompts user for first number
    user_input2 = int(input("Gimme the second number: "))       #prompts user for second number
    print(f"Aiite so..the sum of the two numbers, {user_input1} and {user_input2},  is ", add(user_input1, user_input2))
except ValueError: # except is used in conjuction with try, kinda like if -> then     
    print("Please enter valid numbers.")