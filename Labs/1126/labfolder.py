def recursion(x):
    if x == 1:
        return 1
    else:
        return recursion(x -1) * x

number = int(input("\nenter a number to get its factorial: "))
print (recursion(number))