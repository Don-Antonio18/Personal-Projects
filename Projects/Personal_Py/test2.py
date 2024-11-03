#!/bin/python3

import math
import os
import random
import re
import sys

days_in_month = [ 
    ('January', [31]),
    ('February', [28, 29]),
    ('March', [31]),
    ('April', [30]),
    ('May', [31]),
    ('June', [30]),
    ('July', [31]),
    ('August', [31]),
    ('September', [30]),
    ('October', [31]),
    ('November', [30]),
    ('December', [31])
]

names_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def MonthDays(month_name):
    if month_name.capitalize() == "February":   
        return days_in_month[1][1]
    for month, days in days_in_month:           
        if month == month_name.capitalize():    
            return days[0]     
    return []  # base case, if month is not found

def week_day(year, month, day):
    # Zeller's Congruence base cases
    if month == 1 or month == 2:
        month += 12
        year -= 1

    DayOfWeek = int((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7
    return names_of_days[DayOfWeek]    

def unLucky(year):
    # list comprehension to find Friday the 13th in each month
    return [
        (day, month, year) for day in range(1, 32)   # loop through each day of the month
        for month in range(1, 13)                    # loop through each month
        if week_day(year, month, day) == "Friday" and day == 13
    ]

def so_unLucky(start, end):
    # Create a list of years with exactly 3 unlucky (Friday the 13th) dates
    ListOfunLuckies = [                        
        year for year in range(start, end + 1)  # iterate over all years from start to end
        if len(unLucky(year)) == 3  # check if there are exactly 3 Friday the 13ths in the year
    ]
    
    # Return an empty list if no unlucky years are found, otherwise return the list of years
    return ListOfunLuckies  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    years = list(map(int, input().rstrip().split()))

    answer = so_unLucky(years[0], years[1])

    # Format answer as a list of integers in string form
    fptr.write('[' + ', '.join(map(str, answer)) + ']')
    fptr.write('\n')

    fptr.close()