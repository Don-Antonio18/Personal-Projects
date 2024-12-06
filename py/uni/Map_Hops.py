
def my_map(f, lst):
    if list == []:  return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def sq(x): return x * x
lst =  [3, 5, 7, 9, 11, 13]

print (list(map(lambda x: 2*x, map(sq, lst))))
print (list(map(lambda x: x , map(sq, lst))))

