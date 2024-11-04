''' makeQueue: void -> Queue '''
def makeQueue():
    return ('queue', [])  # tuple containing queue and list
# q1 = makeQueue()
# print (q1)

def contents(q):
    return q[1] # returns contents of the argument

# checks if Queue is valid:
def isQueueValid(obj):
    ''' checks if arg parameters are 'queue' and type:list respectively '''
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([])
    
# q2 = ("queue", [1,2,3,4,5])
# print (isQueueValid(q2))3

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
# q3 = ("queue", [])
# print (isQueueEmpty(q3))

''' Add elements to queue '''
def enqueue(q, elmnt):
    contents(q).append(elmnt)  
    
'''Remove elements from queue'''
def dequeue(q):
    contents(q).pop(0) #use pop func to remove last elmt from queue
    
'''Idetify front of Queue: '''
def front(q):
    if isQueueValid(q) and isQueueEmpty2(q):
        return contents(q)[0] # returns first element of queue
    else:
        raise TypeError("Dequeue; arg must be a queue")
    
q = makeQueue()
contents(q).append("Antonio") 
contents(q).append("Kerr")  # append adds element to end of queue
print (q)
