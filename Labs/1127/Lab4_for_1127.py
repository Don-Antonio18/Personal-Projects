
''' Details of the student record st1, the dictionaries and functions'''
def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

#A student record for Jane Doe
st1 = student('620000101',
        "Jane","Doe",
        ["COMP1126",80, "COMP1127",60, 
        "COMP1210",50,"COMP1161",60,
        "COCR2003",85,"COMP2140",80])

#A function that performs an operation on each element in a list
def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])


'''Write a function computeLetterGrade() which takes a number grade and returns the
corresponding letter grade'''
def computeLetterGrade(Grade):
    #implementing grade function with match case:
    if Grade > 89:
            return ("A+")
    elif Grade >= 80:
            return ("A")
    elif Grade >= 75:
            return ("A-")
    elif Grade >= 70:
            return ("B+")
    elif Grade >= 65:
            return ("B")
    elif Grade >= 60:
            return ("B-")
    elif Grade >= 55:
            return ("C+")
    elif Grade >= 50:
            return ("C")
    elif Grade >= 45:
            return ("F1")
    elif Grade >= 40:
            return ("F2")
    elif Grade >= 0:
            return ("F3")
    else:
        raise ValueError("Invalid grade")



def calcLetterGrade(student):
    # returns a list of tuples of course CODES & GRADES
    Course_List = get_courses(student)
    
    # underscore (_) indicates that 1st part of tuple isnt needed
    Number_Grades = [grades for (_, grades) in Course_List]
    
    # applies computeLetterGrade func to each index in grade lst
    Letter_Grades = list(my_map(computeLetterGrade,Number_Grades))
    
    # New list with list of courses + list of letter grades
    NewCourseList = list(myzip([Course_Tuple[0] for Course_Tuple in Course_List], Letter_Grades))
    return NewCourseList
    




#A dictionary of course codes as keys and their corresponding credit values
credit_list={   'COMP1126':3,
                'COMP1127':3,
                'COMP1161':3,
                'COMP1210':3,
                'COMP1220':3,
                'COMP2140':3,
                'COMP2111':3,
                'COCR2003':1    }

#A dictionary with letter grades as keys and their quality points
qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,\
"C":2.0,"F1":1.7,"F2":1.3,"F3": 0.0}


def convertToWtqp(course_tuple):
    #extracting course code from tuple:
    course_code = get_ccode(course_tuple)
    
    #extracting letter grade from tuple:
    letter_grade = get_grade(course_tuple)

    # uses course code as key in credit list dict
    if course_code in credit_list:
        credit_weight = credit_list[course_code]
    else:
        raise ValueError(f"Course code {course_code} not found.")

    # uses letter grade as key in letter grade dict
    if letter_grade in qp_list:
        quality_point = qp_list[letter_grade]
    else:
        raise ValueError(f"Letter grade {letter_grade} not found. ")

    # Return the tuple (Credit Weigh, Quality Point)
    return (credit_weight, quality_point)

# print(convertToWtqp(("COMP1127", "B-")))
    
def calcGPA(student):
    """Calculates the GPA for the given student record."""
    # Extract list of tuples of course codes and number grades
    course_list = get_courses(student)
    
    # Create a list of tuples of course codes and letter grades
    letter_grade_list = calcLetterGrade(student)
    
    # Create a list of corresponding weight and quality points for each course code and letter grade
    weight_and_qp_list = my_map(convertToWtqp, letter_grade_list)
    
    # Calculate total grade points and credit weights
    total_grade_points = sum(weight * quality_point for weight, quality_point in weight_and_qp_list)
    total_credit_weights = sum(weight for weight, _ in weight_and_qp_list) 
    
    if total_credit_weights == 0:
        raise ValueError("Total # of credit weights can't be zero.")
    
    gpa = round(total_grade_points / total_credit_weights, 2)
    return gpa

#A function that prints a student’s details including GPA. It needs function calcGPA
def print_students_gpa(student):
    """Prints the student's details and GPA."""
    print("Student Id:", get_id(student))
    print("Student name:", get_fname(get_name(student)), get_lname(get_name(student)))
    print("GPA: %.2f" % calcGPA(student))


