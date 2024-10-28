def isPrime(n):
    # 1 is not a prime number
    if n <= 1:
        return False
    else:
        # code sets range for n to be between 2 and n-1
        for i in range (2, n ):
            # code checks if n is divisible by number 
            # between above 1 and n - 1 
            if n % i == 0:
                # prime numbers are only divisible by 1 and itself
                # therefore if n can be divided by numbers apart from 1 and itself,
                # it is NOT a prime number
                return False
        #hence, if no divisors are found,
        # n is a prime number
        return True
number = int(input( '''\n Enter a number. True for prime numbers and False for Non-Prime numbers: '''))
print(isPrime(number))
