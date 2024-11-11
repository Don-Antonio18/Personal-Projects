def sq(n):     return n ** 2
def incrmt(n):  return n + 1

def sum(term, start, next, stop):
    if start > stop:
        return 0
    else:
        return term(start) + \
            sum(term, next(start), next, stop)

print(sum(sq, 1, incrmt, 4))