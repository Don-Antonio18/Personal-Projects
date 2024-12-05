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

calendar = {key:value for key, value in days_in_month}

''' Function that returns # of days in a particular month'''
def MonthDays(month_name):
    if month_name.capitalize() in calendar: #checks if capitized vr. of input is in dict
        return calendar[month_name.capitalize()] #access days using month string as a key
    else: return []



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




def unLucky(year):
    # list comprehension (using multiple lines for clarity)
    return [
        (day, month, year) for day in range(1,32)   #loops through each day of month
        for month in range(1,13)    # loops through each month of the year
        if week_day(year, month, 13) == "Friday"  #checks if 13th day of each month is a Friday
        #if week_day(year, month, day) == "Friday" and day == 13 #checks if date is both a friday and the 13th of a month
]


def so_unLucky(start,end):
    # create new list using list comprehension (using multiple lines for clarity)
    ListOfunLuckies = [                        
        years for years in range(start, end + 1)  # counts years for all years in the range of start --> finish
        if len(unLucky(years)) > 2 # if length of unlucky years list == 3, there are 3 unlucky dates
    ]                     
    return ListOfunLuckies

2