

# 1A Memory structure for std:
#Given the following list
std = [6200001, ["Doe","David","John"], [["COMP1126",[20,10,23,54]],["COMP1127",[3,6,11,60]]]]
def memory_struct():
    '''
    std has length of 4 items:
    std[0] = 6200001

    std[1] = ["Doe","David","John"]
        std[1][0] = "Doe"
        std[1][1] = "David"
        std[1][2] = "John"

    std[2] = [["COMP1126",[20,10,23,54]]
        std[2][0][0] = "COMP1126"
        std[2][0][1] = [20,10,23,54]
        
        std[2][1][0] = "COMP1127"
        std[2][1][1] = [3,6,11,60]
    '''

# 1B Give statements in python which will return id, last name and first name of std. '''
def student_info(idnum):
    
    if idnum in std:
        return (f" ID: {idnum}, Last Name: {std[1][0]}, First Name: {std[1][2]} ")
    return "Invalid ID Number."
        
#id = int(input("Enter Student ID: "))
#print (student_info(id))

'''
# 1C: Write a function get_grades which given the student list above and a course code
returns the corresponding grades summed up.
>>>get_grades(std, "COMP1127")
80
'''
def get_grades(coursecode):
    
    while len(coursecode) != 8:
        coursecode = input("Code too short; enter again. ")
    if coursecode[-1] == "6":
        grade_sum = sum(std[2][0][1][0:5])
        all_caps = all_caps = coursecode[0:4].upper()
        return f"Course:{all_caps}{coursecode[5:9]} , Grade:{grade_sum}"
    elif coursecode[-1] == "7" : #and len(coursecode) == 7
        grade_sum = sum(std[2][1][1][0:5])
        all_caps = coursecode[0:4].upper()
        return f"Course: {all_caps}{coursecode[5:9]},Grade: {grade_sum}"
    else:
        return "Invalid Course Code."
    
code = input("Enter Course Code: ")  
print (get_grades(code))


