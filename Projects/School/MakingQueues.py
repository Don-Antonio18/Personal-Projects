# makeQueue: void -> Quewue
def makeQueue():
    return ('queue', ["antonio", 2])

q1 = makeQueue()
print (q1)

def contents(q):
    return q[1] # returns contents of the arg

# checks if Queue is valid:
def isQueueValid(obj):
    # checks if arg parameters are 'queue' and type:list respectively
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([])
    
q2 = ("queue", [1,2,3,4,5])
print (isQueueValid(q2))

# check if Queue is empty:
def isQueueEmpty(obj):
    # checks if arg parameters are 'queue' and type:list respectively
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([]) \
    and contents(obj) == [] #checks if arg is a list

q3 = ("queue", [])
print (isQueueEmpty(q3))