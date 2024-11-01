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
    if month_input == "February":   return days_in_month[1][1]
    for i, days in days_in_month: 
        if i == month_input     :   return days[0] 
        else                    :   return f"The month of '{month_input}' doesn't exist."
    
#month_input = input(("Enter a month to see how many days it has: "))
print(MonthDays("Febuary"))

names_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

'''' Zeller's Congruence is an algorithm for finding the day of the week for any date. 
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

'''
# function week_day, which displays the day name for a given date supplied in
# the form (year, moth, day).

def week_day(year, month, day):
    if month == 1 or month == 2:
        month += 12
        year -= 1

    DayOfWeek = int(((int(13 * month +3 ) / 5 + day + year + int(year / 4) - int(year / 100) + int(year / 400)) %7))
    return names_of_days [DayOfWeek]

print (week_day(2010,5,9))












# For problem 4 copy solution from longest_gap 