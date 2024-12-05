from tree import *

#   PROBLEM 2
def stack():
    return ('stack', [])  #returns stack tag and empty list

def contents(stack):
    return stack[1] # returns 1st elmnt in stack

def top(stack):
    if not is_stack(stack):
        raise ValueError("Argument is not a valid stack.")
    elif stack_empty(stack):
        raise ValueError("Cannot view the top of an empty stack.")
    else:
        return contents(stack)[-1]  # returns top of stack
    
def pop(stack):
    if not is_stack(stack):
        raise ValueError("Argument is not a valid stack.")
    if stack_empty(stack):
        raise ValueError("Can't pop an empty stack.")
    return contents(stack).pop()
    
def push(stack, elmt):
    if not is_stack(stack):
        raise ValueError("Argument is not a valid stack.")
    else:
        contents(stack).append(elmt)
    
def is_stack(obj):
    ''' checks if arg parameters are 'queue' and type --> list '''
    return type(obj) == tuple and len(obj) == 2 \
    and obj[0] == "stack" and type(obj[1]) == list
    
def stack_empty(stack):
    if is_stack(stack):             # returns True if arg is a stack
        return contents(stack) == []    # returns True if stack is empty
    else:
        raise TypeError("dequeue; arg must be a stack")
    
#   PROBLEM 3

def isOperator(symbol):
    """Returns True if the argument is an operator (+, -, *, /) and False otherwise."""
    operators = ['+', '-', '*', '/']
    return symbol in operators

def isOperator(symbol):
    """Returns True if the argument is an operator (+, -, *, /) and False otherwise."""
    operators = ['+', '-', '*', '/']
    return symbol in operators

def applyOperator(operator, operand1, operand2):
    """
    Applies the operator to operand1 and operand2.
    operand1 is the second popped value
    operand2 is the first popped value
    """
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        # Handle division by zero
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2
    else:
        raise ValueError(f"Unknown operator: {operator}")

def eval_Postfix(tree):
    # Convert tree to postfix list
    postfix_list = post_order(tree)
    
    # Create stack for evaluation
    eval_stack = stack()
    
    # Process each element in the postfix list
    for element in postfix_list:
        if not isOperator(element):
            # If element is an operand, push it to stack
            push(eval_stack, element)
        else:
            # If element is an operator, pop two operands and apply operator
            if stack_empty(eval_stack):
                raise ValueError("Invalid expression: not enough operands")
            
            operand2 = pop(eval_stack)  # First popped value
            
            if stack_empty(eval_stack):
                raise ValueError("Invalid expression: not enough operands")
                
            operand1 = pop(eval_stack)  # Second popped value
            
            # Calculate result and push back to stack
            result = applyOperator(element, operand1, operand2)
            push(eval_stack, result)
    
    # After processing all elements, stack should have exactly one value
    if stack_empty(eval_stack):
        raise ValueError("Invalid expression: empty result")
    
    result = top(eval_stack)
    pop(eval_stack)  # Remove the result
    
    if not stack_empty(eval_stack):
        raise ValueError("Invalid expression: too many operands")
        
    return result

print(eval_Postfix(tree_ex)) 