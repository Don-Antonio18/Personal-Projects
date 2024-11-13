
#? Define list_copy that takes a list & produces a list containing
#? All the elements of the first list

def list_copy():
    old_list = list(input("enter a list: "))
    new_list = []
    for i in old_list:
        new_list.append(i)
    return f" New list is {new_list}"

print(list_copy())


