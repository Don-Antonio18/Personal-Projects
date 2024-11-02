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
# converts the list into a dictionary , creating a key:value pair for 
# every element in the list
calendar = {key:value for key, value in days_in_month}

def MonthDays(month_input):
    if month_input.capitalize() in calendar: #checks if capitized vr. of input is in dict
        return calendar[month_input.capitalize()] #access days using month string as a key
    else: return f"Month '{month_input}' not found in the calendar."
print(MonthDays("December"))
