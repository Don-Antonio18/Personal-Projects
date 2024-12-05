''' makeQueue: void -> Queue '''
def makeQueue():
    return ('queue', [])  # tuple containing queue and list

def contents(q):
    return q[1] # returns contents of the argument

# checks if Queue is valid:
def isQueueValid(obj):
    ''' checks if arg parameters are 'queue' and type:list respectively '''
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([])

''' check if Queue is empty: '''
def isQueueEmpty1(obj):
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([]) \
    and contents(obj) == [] #checks if arg is a list
    
def isQueueEmpty2(q):
    if isQueueValid(q):  # returns True if arg is a queue
        return contents(q) == []    # returns True if queue is empty
    else:
        raise TypeError("dequeue; arg must be a queue")

''' Add elements to queue '''
def enqueue(q, elmt):
    #adding to the back
    if isQueueEmpty2(q): # 
        contents(q).insert(0,elmt)
    else:
        #raise TypeError, "enqueue: Not a Queue"
        return TypeError(q, "enqueue: Not a Queue")
    contents(q).append(elmt)  
    
'''Remove elements from queue'''
def dequeue(q):
    # removing from front:
    if not isQueueEmpty2(q):
        contents(q).pop() #use pop func to remove last elmt from queue
    else:
        raise IndexError("Queue is empty")
    
'''Idetify front of Queue: '''
def front(q):
    if isQueueValid(q) and isQueueEmpty2(q):
        return contents(q)[0] # returns first element of queue
    else:
        raise TypeError("Dequeue; arg must be a queue")
    
q = makeQueue()
details = ["Antonio", "is a ", "boy, named: "]
contents(q).append(details)
contents(q).append("Kerr")  # append adds element to end of queue
print (q)

q2 = ("queue", [1,2,3,4,5])
print (isQueueValid(q2))
print (q2)


q3 = ("queue", ["Empty"])
print (isQueueEmpty2(q3))
print (q3)


# ask tabnine to create documentation for every line

