
def my_map(f, lst):
    if list == []:  return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def sq(x): return x * x
lst =  [3, 5, 7, 9, 11, 13]
lst2 = my_map(sq, lst)

print (my_map(lambda x: 2*x, map(sq, lst)))
