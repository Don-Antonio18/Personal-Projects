def div(x, y):
    if x < y:
        return 0
    else:
        return 1 + div( x - y, y)
def mod(x, y):
    if x < y:
        return x
    else:
        return mod(x-y, y)

