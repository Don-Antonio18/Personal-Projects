'''
This function takes list as argument and 
returns the # of elements in the list
'''


def myLen(lst):
    if lst == []:
        return 0
    else:
        return 1 + myLen(lst[1:])

    
list = [1,2,3]
print (myLen(list))

'''


'''