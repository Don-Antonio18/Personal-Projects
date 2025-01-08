# def isPrime(num):
#     #numbers less than 2 are not primt
#     if num < 2:
#         return False
#     # code uses range of lowest prime, 2 to the square root of input
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# code imports function from previous code
from lab2q3 import isPrime

def prime_time(m, n):
    if  n <= m:
        return 
    # code checks range and uses n + 1 to include n
    # range should be between m and n
    for i in range (1, n + 1):
        if isPrime(i):
            dif = i - m
            #code checks to see if difference between prime num and m 
            # is a prime num itself
            # AND if it is greater than or equal to m
            if dif >= 2 and isPrime(dif):
                print(i, end=", ")

number1 = int(input("\n Enter m number: "))
number2 = int(input("\n Enter n number: "))
print (prime_time(number1, number2))