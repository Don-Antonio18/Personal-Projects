


def sq(x): return x * x
lst =  [3, 5, 7, 9, 11, 13]
lst2 = map(sq, lst)

print map(lambda x: 2*x, map(sq, lst))
