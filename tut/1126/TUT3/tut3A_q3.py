def div(x, y):
    i = 0  # This will count how many times y can be subtracted from x
    while x >= y:
        x = x - y
        i += 1
    return i

# Modulus function using a while loop
def mod(x, y):
    while x >= y:
        x = x - y
    return x

x = int(input("Enter num_1: "))
y = int(input("Enter num_2: "))

print(f"\n div({x}, {y}) =", div(x, y))
print(f"mod({x}, {y}) =", mod(x, y))