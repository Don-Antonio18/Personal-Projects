#creates empty tree and returns empty branches
def makeemptytree(root):
    return ("DT",[root,[],[]])

#* crea
def maketree(root, left, right):
    return ("DT", [root, left, right])

#* parent node
t = maketree (
    # el, left, right
    1, 
    #left branch
    maketree(
        2,
        #left node subtree 1
        makeemptytree(None),
        # left node subtree 2
        makeemptytree(None),  
    ),
    #right branch
    maketree(
        3,
        #right node subtree 1
        makeemptytree(None),
        #right node subtree 2
        makeemptytree(None),
    )
    
#end of tree
)
