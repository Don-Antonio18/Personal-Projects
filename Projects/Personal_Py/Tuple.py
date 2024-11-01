# tuple = collection which is ORDERED and UNCHANGEABLE
# tuples are denoted by tuple_name ()
# tuple.count(value) returns count of condition in tuple
# tuple.index(value) returns location of condition in tuple
#   YOU CAN LOOP THROUGH TUPLES:
# for i in tuple:
#   print (i, end="")

#declaration of tuple:
student = ("Antonio", "Kerr", "Feb 4 2006", 6)
        
# for loop to find location of value in Tuple:
TrynaFind = input("what are u looking for?: ")
count = 0
for i in student:
    if i == TrynaFind:
        print (f"{TrynaFind} found at index {count}")
        count += 1
        break
    else:
        count += 1
else:
    print(f"{TrynaFind} not found in tuple.")


#for loop to PRINT all values in tuple

for i in student:
    print (i, end=" ")   

''' If the number of variables is less than the number of values,  
you can add an * to the variable name and the values will be assigned to the variable as a list:

Example: Assign the rest of the values as a list called "red": '''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

''' This will Output:
'apple', 'banana', ['cherry', 'strawberry', 'raspberry']'''

