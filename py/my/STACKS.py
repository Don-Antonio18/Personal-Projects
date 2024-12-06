""" uses last in first out method"""
""" Stacks are implemented using constructors, mutators, and selectors. 
1. Constructors:
- `create_stack()`: Initializes the stack. 
This function creates an empty list to store the stack elements.

2. Mutators (or Modifiers): These functions modify the state of the stack.
- `push(stack, data)`: Adds an element to the top of the stack. 
If the stack is full, it raises an OverflowError.
- `pop(stack)`: Removes and returns the top element from the stack. 
If the stack is empty, it raises an UnderflowError.

3. Selectors (or Accessors): 
- `peek(stack)`: Returns the top element of the stack without removing it. 
If the stack is empty, it returns None.
- `is_empty(stack)`: Returns True if the stack is empty, False otherwise.
- `size(stack)`: Returns the number of elements in the stack. """

def makeStack():
    return ('stack', [])  #returns stack tag and empty list

def contents(s):
    return s[1] # returns 1st elmnt in stack

def top(stack):
    if not isStackValid(stack):
        raise ValueError("Argument is not a valid stack.")
    elif isStackEmpty(stack):
        raise ValueError("Cannot view the top of an empty stack.")
    else:
        return contents(stack)[-1]  # returns top of stack
    

# stack Predicate / Checker
def isStackValid(obj):
    ''' checks if arg parameters are 'queue' and type --> list '''
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "stack" and type(obj[1]) == list
    
    
def isStackEmpty(obj):
    if isStackValid(obj):             # returns True if arg is a stack

        return contents(obj) == []    # returns True if stack is empty
    else:
        raise TypeError("dequeue; arg must be a stack")
    
def pop(s):
    #removing from top of stack
    #contents(s).pop()
    contents(s).pop(0)

def push(stack, item):
    """
    Pushes an item onto the stack.
    """
    if not isStackValid(stack):
        raise ValueError("Argument is not a valid stack.")
    else:
        contents(stack).append(item)
    
def enqueue(s, el):
    #adding to the back
    if isStackValid(s):
        contents(s).insert(0,el)
    else:
        #raise TypeError, "enqueue: Not a Stack"
        return TypeError(s, "enqueue: Not a Stack")
    contents(s).append(el)  
    
def dequeue(s):
    # removing from top
    if not isStackValid(s):
        contents(s).pop() 
    else:
        raise IndexError("Queue is empty")

    

    




