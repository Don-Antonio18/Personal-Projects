import datetime

def future_date(yy, mm, dd):
    date = datetime.datetime.now()
    current_year = date.year
    current_month = date.month
    current_day = date.day
    todays_date = int
    
    if yy > current_year:
        return True
    elif mm > current_month:
        return True
    elif dd > current_day:
        return True
    elif mm == current_month:
        if dd > current_day:
            return True
        else:
            return False
    else:
        return False
        

year = input("\nWhat year is it?: ")
year = int(year)
month = input(f"\nWhich numerical month of {year} were you born in?: " )
day = input(f"\nWhich day is it?:  ")
day = int(day)

print(future_date(year, month, day))


