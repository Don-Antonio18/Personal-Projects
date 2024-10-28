def count_fails(lst,passing_grade):
    fails = 0 
    for i in lst:
        # program returns count of numbers less than the passmark
        if i < passing_grade:
            fails += 1
    return (f" There were {fails} fails in the class")

#code initialises a list of grades to be entered
grades = []

#code gets grade input from teacher
while True:
    #code prompts teacher to input string of grades 
    grade_input = input("\nEnter a grade (or type 'done' to finish entering grades): ")
    
    #code provides exit case of the string "done"
    if grade_input.lower() == 'done':
        break 

    # block contains code that might raise an error
    try: 
        grade = int(grade_input)  # Converts input to a number
        grades.append(grade) # adds a new element to the end of the list without creating new list

    #if try block error occurs, this code block runs
    except ValueError: #ValueError  = input is NOT a valid NUMBER
        print("\nInvalid input, please enter a number or 'done'.")

#code allows user to enter passmark for exam
passmark = int(input("\nwhat is the passmark for this exam?: "))

#code calls function and passes array of grades to argument
print (count_fails(grades, passmark))



# first_grade = int(input("\nwhat is the first grade?"))
# second_grade = int(input("\n What is the second grade? "))
# my_list = [first_grade, second_grade]
# #my_list = [25, 45, 55, 75, 85, 100]