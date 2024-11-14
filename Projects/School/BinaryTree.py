

#Parameters: 
#value: Contains the data for a node. This value must be number. 
#left:   Contains the details of left node child. 
#right:  Contains details of the right node child. 
from BinaryTree import Node
root = Node(3) 
root.left = Node(6) 
root.right = Node(8) 

# Getting binary tree 
print('Binary tree :', root) 

# Getting list of nodes 
print('List of nodes :', list(root)) 

# Getting inorder of nodes 
print('Inorder of nodes :', root.inorder) 

# Checking tree properties 
print('Size of tree :', root.size) 
print('Height of tree :', root.height) 

# Get all properties at once 
print('Properties of tree : \n', root.properties) 

#################################################################

def makeTree(value, left=None, right=None):
    return {'value': value, 'left': left, 'right': right}

def makeEmptyTree():
    return None

# Create a binary tree
t = makeTree(
    5,
    makeTree(
        7,
        makeEmptyTree(),
        makeTree(
            13,
            makeEmptyTree(),
            makeEmptyTree()
        )
    ),
    makeTree(
        11,
        makeEmptyTree(),
        makeEmptyTree()
    )
)

# Print the tree
def print_tree(tree):
    if tree is None:
        return
    print(tree['value'])
    print_tree(tree['left'])
    print_tree(tree['right'])

print_tree(t)
