#   TUTORIAL 3 QUESTION 1

# import time
# def five_powers(num):
#     power = 0
#     result = 0 
#     while power <= 4:
#         print (f"{num} raised to {power} = {num ** power}")
#         power += 1
#         time.sleep(0.1)

# five_powers(3)

#   NOTES ON RECURSION

# import time
# def five_powers(num):
#     power = 0
#     result = 0 
#     while power <= 4:
#         print (f"{num} raised to {power} = {num ** power}")
#         power += 1
#         time.sleep(0.1)

# five_powers(3)


def five_power(x):
    def looper(i): 
        #RECURSIONS USE THE OPPOSITE CONDITIONAL AS WHILE LOOP OF SAME FUNCTION
        if i > 4:
            return None
        print (x ** i)
        looper(i + 1)

    looper(0)
five_power(3)

