#creates empty tree and returns empty nodes
def makeemptytree(root):
    return ("DT",[root,[],[]])

#* crea
def maketree(root, left, right):
    return ("DT", [root, left, right])

#* parent node
t = maketree (
    # el, left, right
    1, 
        #left node
        maketree(
            2,
            #left node subtree 1
            makeemptytree(),
            # left node subtree 2
            makeemptytree(),  
        ),
        #right node
        maketree(
            3,
            #right node subtree 1
            makeemptytree(),
            #right node subtree 2
            makeemptytree(),
        )
    
#end of tree
)
