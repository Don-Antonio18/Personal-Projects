def makeQueue():
    return ('queue', [])  # tuple containing queue and list

def contents(q):
    return q[1] # returns contents of the argument

def isQueueValid(obj):
    ''' checks if arg parameters are 'queue' and type:list respectively '''
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "queue" and type(obj[1]) == type([])

def isQueueEmpty2(q):
    if isQueueValid(q):  # returns True if arg is a queue
        return contents(q) == []    # returns True if queue is empty
    else:
        raise TypeError("dequeue; arg must be a queue")

queue = []
#* while NOT isqueueempty
while not (isQueueEmpty2(queue)):
    print (queue)