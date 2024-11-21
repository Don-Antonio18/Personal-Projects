def my_map(f, lst):
    if list == []:  return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def sq(x): return x * x
lst =  [3, 5, 7, 9, 11, 13]

# print (list(map(lambda x: 2*x, map(sq, lst))))
# print (list(map(lambda x: x , map(sq, lst))))





'''
filter takes a predicate and a list as arguments, and returns
a new list containing only those elements of the given list
for which the predicate is true
'''

lst = [3,17,11,9,7,2,19,17]

def filterForPrimes():
    #* converts filtered object into a list so it can be returned
    return list(filter(lambda x: x > 10, [3,17,11,9,7,2,19,17]))

print (filterForPrimes())

#! ^Using LIST COMPREHENSION to do the same thing ^:
# print ([x for x in lst if x > 10])
# print ([2*x for x in lst if x > 10])
# print ([x ** 2 for x in lst if x > 10])

def prime(x):
    for i in range(2, int(x**0.5)):
        
        if x % i == 0 and i != x: return False
        if x == 2: return True
        
    return True
        
#print (prime(29))
        
        
def my_filter(predicate, lst):
    if lst == 0: return []
    elif predicate(lst[0]): 
        return [lst[0]] + my_filter(predicate, lst[1:])
    else:
        return my_filter(predicate, lst[1:])