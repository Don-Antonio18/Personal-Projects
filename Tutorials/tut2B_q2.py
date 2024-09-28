# TUTORIAL 3 QUESTION 2

# function accepts two inputs
# import time
# def power_list(num,number_of_powers):
#     power = 0
#     result = 0 
#     while power < number_of_powers:
#         result = num ** power 
#         return (f"{num} raised to {power} = {result}")
#         time.sleep(0.1)
#         power += 1

# power_list(10,10)

def power_list(num, num_of_powers):
    def looper(i):
        if i == num_of_powers:
            return None
        print (f"{num} raised to {i} = {num ** i}")
        looper(i + 1)
    return looper(0)

power_list(2,10)
