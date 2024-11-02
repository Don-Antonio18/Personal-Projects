days_in_month = [ 
    ('January',[31]),
    ('February',[28,29]),
    ('March',[31]),
    ('April',[30]),
    ('May',[31]),
    ('June',[30]),
    ('July',[31]),
    ('August',[31]),
    ('September',[30]),
    ('October',[31]),
    ('November',[30]),
    ('December',[31])
]
''' Function that returns # of days in a particular month'''
def MonthDays(month_input):
    if month_input.capitalize() == "February":   
        return days_in_month[1][1]
    for month, days in days_in_month:           
        # code below checks if month in list == to month_input after capitalization
        if month == month_input.capitalize():    
            return days[0]     
    #return f"The month of '{month_input}' doesn't exist."
    return [] # base case, if list is empty
    
#month_input = input(("Enter a month to see how many days it has: "))
print(MonthDays("a"))

names_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# function week_day, which displays the day name for a given date supplied in
# the form (year, moth, day).

def week_day(year, month, day):
    # Zeller's Congruence base cases
    if month == 1 or month == 2:
        month += 12
        year -= 1

    DayOfWeek = int(((int(13 * month +3 ) / 5 + day + year + int(year / 4)  - int(year / 100) + int(year / 400)) %7))
    return names_of_days [DayOfWeek]    

print (week_day(2006,2,4))


def unLucky(year):
    # list comprehension (using multiple lines for clarity)
    return [
        (day, month, year) for day in range(1,32)   #loops through each day of month
        for month in range(1,13)    # loops through each month of the year
        if week_day(year, month, day) == "Friday" and day == 13 #checks if date is both a friday and the 13th of a month
]
print (unLucky(2006))

def so_unLucky():
    start = int(input("Enter starting year:" )) 
    end = int(input("Enter ending year:" ))

    # create new list using list comprehension (using multiple lines for clarity)
    ListOfunLuckies = [                        
        years for years in range(start, end + 1)  # counts years for all years in the range of start --> finish
        if len(unLucky(years)) == 3 # if length of unlucky years list == 3, there are 3 unlucky dates
]                     
    if not ListOfunLuckies: 
        return f"No unLuckies between {start} & {end}" # base case if no unLuckies are found
    else:                  
        return (ListOfunLuckies) # return new list 

print (so_unLucky())                 

