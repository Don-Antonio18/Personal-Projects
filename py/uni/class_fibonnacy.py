def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1 ) + fib(n-2)

position = int(input("\nWhich number of the fibonnaci sequence do you want?: "))
print (f"\nThe {position}th number of the fibonnaci sequence is", fib(position))
