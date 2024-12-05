def isPrime(num):
    #numbers less than 2 are not primt
    if num < 2:
        return False
    # code uses range of lowest prime, 2 to the square root of input
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def trickWithPrime(num1, num2):
    if num1 <= 3 or num2 <=3:
        return "\nNumbers should be greater than 3! "
        # code sets conditionals for inputs BETWEEN both numbers
        #code uses num2 + 1 to include num2 itself
    for i in range(num1, num2 +1):
        #checks to see if number between num1 and num2 is prime
        if isPrime(i):
            #code squares said prime number
            prime_sqr = i ** 2
            # code adds 29 to said prime number
            prime_sqr += 29
            # code calcs remainder when num is divided by 8
            remainder = prime_sqr % 8
            print(f"{i}: {remainder * '\U0001F601'}")
number1 = int(input("\n Enter 1st number: "))
number2 = int(input("\n Enter 2nd number: "))
print (trickWithPrime(number1, number2))

