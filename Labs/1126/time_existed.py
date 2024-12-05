from datetime import date
import datetime

def time_existed():

    todays_date = int
    name = input("\nWHat is your name?: ")
    birthyear = input("\nWhat year were you born in? : ")
    birthyear = int(birthyear)
    birthmonth = input(f"\nWhich numerical month of {birthyear} were you born in?: ")
    birthmonth = int(birthmonth)
    birthday = input(f"\nWhich day were you born on? ")
    birthday = int(birthday)
    
    bornday = datetime.date(birthyear, birthmonth, birthday)
    current_date = date.today() 
    days_alive = (current_date - bornday).days
    print (f"\n{name} has lived for {days_alive} days")

time_existed()
    








