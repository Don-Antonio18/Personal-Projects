


operator = input("Enter an operator ( +, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
    print(f"The sum of {num1} and {num2} is: round{(num1 + num2):.3f}\n")
elif operator == "-":
    print(f"The difference of {num1} and {num2} is: {(num1 - num2):.3f}\n")
elif operator == "*":
    print(f"The product of {num1} and {num2} is: {(num1 * num2):.3f}\n")
elif operator == "/":
    if num2 == 0:
        print("Error! Division by zero is not allowed.\n")
    else:
        print(f"The quotient of {num1} and {num2} is: {(num1 / num2):.3f}\n")
else:
    print("Error! Invalid operator. Please use +, -, *, / only.\n")
