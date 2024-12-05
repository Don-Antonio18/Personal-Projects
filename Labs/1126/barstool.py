def barstool(x):
    if num % 3 == 0:
        return ("\nBar")
    elif num % 7 == 0:
        return ("\nStool")
    elif num % 3 == 0 and num % 7 == 0:
        return "\nBarstool"
    else:
        return ("\nNo Bar No Stool")

num = int(input("Enter a number: "))
#num = int(num)
print(barstool(num))