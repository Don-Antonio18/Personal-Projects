# Write a program that calculates the 
# amount of money a person would earn 
# over a period of time if their
# salary is $1 the first day, $2 the second day,
# $4 the third day and continues to double each day. 
# The program
# should take in the number of days. Display salary for each day 
# and the total pay at the end of the period.
# Display total pay in dollars. [Hint: Use a while loop

import time
def earnings(work_days):
    counter = 1; salary = 1
    #code limits the days counted towards earnings by the amount of work days
    while counter <= work_days:
        time.sleep(0.01)
        print (f"Salary earned on day {counter} = ${salary}")
        salary *= 2
        counter +=1 
    return f"\nSalary earned after working {work_days} days is: ${salary}"
days = int(input("How many days in ur life did you work for?: "))
print(earnings(days))

# def compound_salary(days):
#     i = 1
#     while i != days:
#         pay = i * i
#         print 
#         salary += pay
#         i += i
#         print (salary)



