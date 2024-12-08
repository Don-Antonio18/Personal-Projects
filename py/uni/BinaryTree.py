#creates empty tree and returns empty branches
def makeemptytree(root):
    return ("DT",[root,[],[]])

#* crea
def maketree(root, left, right):
    return ("DT", [root, left, right])

#* level order binary tree
level_order_tree = maketree (
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
print(level_order_tree)

#will try to create pre-order tree.
#pre-order tree:
preordertree = maketree(
    1,                               # Root
    maketree(
        2,                          # Left subtree of 1
        maketree(
            4,                      # Left subtree of 2
            maketree(
                8,                  # Left subtree of 4
                makeemptytree(None),
                makeemptytree(None)
            ),
            maketree(               # Right subtree of 4
                9,
                makeemptytree(None),
                makeemptytree(None)
            )
        ),
        maketree(                   # Right subtree of 2
            5,
            maketree(               # Left subtree of 5
                10,
                makeemptytree(None),
                makeemptytree(None)
            ),
            maketree(               # Right subtree of 5
                11,
                makeemptytree(None),
                makeemptytree(None)
            )
        )
    ),
    maketree(                       # Right subtree of 1
        3,
        maketree(                   # Left subtree of 3
            6,
            maketree(               # Left subtree of 6
                12,
                makeemptytree(None),
                makeemptytree(None)
            ),
            maketree(               # Right subtree of 6
                13,
                makeemptytree(None),
                makeemptytree(None)
            )
        ),
        maketree(                   # Right subtree of 3
            7,
            maketree(               # Left subtree of 7
                14,
                makeemptytree(None),
                makeemptytree(None)
            ),
            maketree(               # Right subtree of 7
                15,
                makeemptytree(None),
                makeemptytree(None)
            )
        )
    )
)
    
    
    
