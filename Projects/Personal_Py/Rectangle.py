# rows  = int(input("how many rows?: "))
# columns  = int(input("how many columns?: "))
# symbol = input(("what symbol to draw rectangle?: "))

# for i in range(rows):
#     for j in range(columns):
#         print (symbol, end="")
#     print ()

length = int(input("how long is it: "))
width = int(input("how wise is it: "))
symbol = input(("what symbol to draw rectangle?: "))
for i in range(width):
    for j in range(length):
        print(symbol, end="")   # end ="" prevents print from ending w/ new line
    print() #prints a new line once you exit the inner for loop 