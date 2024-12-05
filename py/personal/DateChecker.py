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
''' Create  Function that returns # of days in a particular month'''
calendar = {key:value for key, value in days_in_month}

""" Using dictionary:"""
def MonthDays(month_input):
    if month_input.capitalize() in calendar: #checks if capitized vr. of input is in dict
        return calendar[month_input.capitalize()] #access days using month string as a key
    else: return f"Month '{month_input}' not found in the calendar."
month_input = input(("Enter a month to see how many days it has: "))
print(MonthDays(month_input))

""" Using For Loop: """
def MonthDays(month_input):
    if month_input.capitalize() == "February":   
        return days_in_month[1][1]
    for month, days in days_in_month:           
        # code below checks if month in list == to month_input after capitalization
        if month == month_input.capitalize():    
            return days[0]     
    return [] # base case, if list is empty


""" Zeller's Congruence is an algorithm for finding the day of the week for any date. 
Zeller's formula is as follows:
day = (((13*m+3) / 5 + d + y + (y / 4) - (y / 100) + (y / 400)) %7)
where: d = day, y = year and m = month

Note: If the month is January or February then you add 12 to the month 
and subtract 1 from theyear before calculating the day. 
Further, Zeller's Congruence is deemed to be computed correctly where the integer value 
is used for each computation of a division (or number being divided).

The result is a day number in the range 0..6 where the corresponding day can 
be extracted from the names_of_days list by using an appropriate index.
e.g. names_of_days[0] = 'Monday' and names_of_days [6] = 'Sunday'.
"""

names_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# function week_day, which displays the day name for a given date supplied in
# the form (year, moth, day).

def week_day(year, month, day):
    # Zeller's Congruence base cases
    if month == 1 or month == 2:
        month += 12
        year -= 1

    DayOfWeek = int(((int(13 * month +3 ) / 5 + day + year + int(year / 4) - int(year / 100) + int(year / 400)) %7))
    return names_of_days [DayOfWeek]

print (week_day(2006,2,4))


''' Using list comprehension, define a python function unLucky, which returns all the days in a
given year which have the date Friday 13th. The days are returned in the form (day, month, year)
e.g.>>> unLucky(2010)
[(13, 8, 2010)]
>> unLucky(2009)
[(13, 2, 2009), (13, 3, 2009), (13, 11, 2009)]



[Hint: you may use two ranges, one for day starting from 1 and going to 31 and another one for month
starting from 1 going to 12. Using these and the year which comes as an argument and use the function
week_day (Problem 2) in the if part of list comprehension to check if a given date is ‘Friday’ and
also check if the day is equal to 13.]

'''
def unLucky(year):
    # list comprehension (using multiple lines for clarity)
    return [
        (day, month, year) for day in range(1,32)               #loops through each day of month
        for month in range(1,13)                                # loops through each month of the year
        if week_day(year, month, day) == "Friday" and day == 13 #checks if date is both a friday and the 13th of a month
]
print (unLucky(2006))


''' Write a python function so_Unlucky, which lists all the years between a given start year and
end year e.g. years 0 and 2010 which have 3 unlucky days. Use function unLucky (Problem 3) to
get a list of unlucky dates for a particular year and find the length of this list. 
If the length is greater than 2 then the year is added to another list which is returned as output. 

'''
def so_unLucky():
    start = int(input("Enter starting year:" )) 
    end = int(input("Enter ending year:" ))

    # create new list using list comprehension (using multiple lines for clarity)
    ListOfunLuckies = [                        
        years for years in range(start, end + 1)  # counts years for all years in the range of start --> finish
        if len(unLucky(years)) == 3               # if length of unlucky years list == 3, there are 3 unlucky dates
]                     
    if not ListOfunLuckies: return f"No unLuckies between {start} & {end}" # base case if no unLuckies are found
    else:                  return (ListOfunLuckies)                        # return new list 

print (so_unLucky())                 
