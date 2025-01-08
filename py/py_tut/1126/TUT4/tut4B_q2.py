'''
Question 2
Write functions that perform addition and subtraction recursively. You have been given two
functions pred and succ, pred given a number returns the previous number and succ given a
number returns the next number.
>> pred(5)
4
>> succ(5)
6
Logic for addition is that given two numbers as arguments keep on getting the successor (succ) of
the first and the predecessor (pred)of the second, until the second argument is 0 then the first argument
is the answer.
>>>addition(5,3)
8
Logic for subtraction is that given two numbers as arguments keep on getting the predecessor (pred)
of the first and the predecessor (pred)of the second, until the second argument is 0 then the first argument
is the answer.
>>>subtraction(5,3)
2
'''




def succ(a):
    if a == 0:
        return 0
    else:
        return a + 1

def pred (b):
    if b == 0:
        return 0
    else:
        return b -  1
    
def add(a,b):
    if b == a:
        return a
    if b == 0:
        return a
    else:
        return add(succ(a), pred(b))
    
def subtract(a,b):
    if b == a:
        return a
    if b == 0:
        return a
    else:
        return subtract(pred(a), pred(b))
    
print(add(20,10))
print (subtract(100,50))
