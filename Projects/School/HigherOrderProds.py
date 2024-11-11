def sum(term, start, next, stop):
    if start > stop:
        return 0
    else:
        return term(start) + \
            sum(term, next(start), next, stop)
            
def sq(n):     return n ** 2
def incrmt(n):  return n + 1

print(sum(sq, 1, incrmt, 4))

#? Using lambda functon, replace sq and incrmt functions
            # sq funct        # incrmt func
print(sum(lambda n: n **2, 1, lambda n: n + 1, 4  ) )
