import time
def nbr_even(list):
    e = 0
    for i in list:
        if i % 2 == 0 :
            e = e + i
            # e = i + 1
    print("The number of even numbers is: ", e)


nbr_even([3,4,76,82,77])

# ALTERNATIVE WAY OF RUNNING. DOWNSIDE IS THAT YOU MUST ENTER VARIABLES BEFOREHAND
'''
def nbr_even(list):
    list = [3,4,72,84,77]
    e = 0
    for i in list:
        if i % 2 == 0 :
            e = e + 1
    print("The number of even numbers is: ", e)

nbr_even()

'''