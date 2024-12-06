


def make_empty_tree(root):
    return ("DT",[root,[],[]])

def makeTree(root, left, right):
    return ("DT", [root, left, right])

def root(DT):
    return DT[1][0]

def left_subtree(DT):
    return DT[1][1]

def right_subtree(DT):
    return DT[1][2]

def is_empty(DT):
    return DT[1][1] == [] and DT[1][2] == []

def is_DT(DT):
    if not isinstance(DT, tuple) or len(DT) != 2:
        return False
    if DT[0] != "DT":
        return False
    if not isinstance(DT[1], list) or len(DT[1]) != 3:
        return False
    return True

# Generate the decision tree based on the image
decision_tree = makeTree("HGC",
    makeTree("HBP",
        makeTree("DBF",
            makeTree("SM",
                makeTree("LRL", [], []),
                makeTree("DB",
                    makeTree("LRL", [], []),
                    makeTree("MRL", [], [])
                )
            ),
            makeTree("EH",
                makeTree("LRL", [], []),
                makeTree("MRL", [], [])
            )
        ),
        makeTree("DBF",
            makeTree("LRL", [], []),
            makeTree("BMI",
                makeTree("MRL", [], []),
                makeTree("HRL", [], [])
            )
        )
    ),
    makeTree("DB",
        makeTree("MRL", [], []),
        makeTree("HRL", [], [])
    )
)

def diagnose(tree, hist_lst):
    # Base cases - if we've reached a risk level node
    if root(tree) in ["LRL", "MRL", "HRL"]:
        return root(tree)
    
    # Get the index and value for the current condition
    condition_map = {
        "HGC": 0, "DB": 1, "HBP": 2, "DBF": 3,
        "EH": 4, "SM": 5, "BMI": 6
    }
    
    current_condition = root(tree)
    condition_index = condition_map[current_condition]
    condition_value = hist_lst[condition_index]
    
    # Traverse left for "False", right for "True"
    if condition_value == "False":
        return diagnose(left_subtree(tree), hist_lst)
    else:  # condition_value == "True"
        return diagnose(right_subtree(tree), hist_lst)