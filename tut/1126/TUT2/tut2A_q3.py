
'''Write a function in python called salesTotal that accepts as its inputs the price of an item, and the
number of units of the item purchased. The function should compute and return the total charge for the
item applying any discount according to the following rules:
 - No discount is given if 5, or less, units are bought.
 - 10% discount if more than 5 units up to 10 units are bought.
 - 12½% discount if more than 10 units are bought'''
import time
def salesTotal(price,units):
    if units <= 5:
        discount = 1
    elif units >= 5 and units < 10:
        discount = 0.9
    elif units >= 10:
        discount = 0.875
    return(f"The charge is: {price * discount * units}") #must calculate price of item * units of item * discount of total
            
x = int(input("Enter the price of the item:  "))
time.sleep(1)
y = int(input(("Enter the amount of units bought: ")))
print((salesTotal(x,y)))

'''
def salesTotal(price,numUnits):
    total = 0
    if 5 < numUnits < 11:
        discount = 0.9
    elif numUnits > 10:
        discount = 0.875
    total = price * numUnits * discount
    return f"The total is: {total}"
    
x = int(input("Enter the price of the item:  "))
y = int(input(("Enter the amount of units bought: ")))
print((salesTotal(x,y)))'''

