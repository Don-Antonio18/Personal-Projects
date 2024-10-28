def strange(n):
    if n <= 1:
        return 0
    else:
        return (1 + strange(n/3))

print (strange(8))