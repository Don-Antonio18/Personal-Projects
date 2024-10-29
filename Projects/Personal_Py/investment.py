import random
# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# THIS PROGRAM CALCULATES ROI for n days based on inputted INVESTMENT  amount PER DAY
# in future programme should api from investment project to detect stock history and predict future trend

#user enters how many days they invested for 
def ROI(days_invested,amt_invested):
    counter = 1
    rate = random(range(1.02739726027, 0.02739726027 - 1))
    while counter <= days_invested:
        # calculate the ROI for the day
        # yearly investment of $100 = (100 * ( 1 + 0.02739726027)) - 100 ) = 2.739726027 after 1st day
        daily_roi = (amt_invested * (1 + amt_invested)) - amt_invested
        yearly_investment = amt_invested * (days_invested / 365)
        total = amt_invested ( pow(1 + rate / 100), yearly_investment)
        print(f"Total after {years_invested}years = {total:.2f}")

        

        counter += 1

days = int(input("How many days did you invest for?: "))
amt = float(input("How much $ did you invest per day?: "))
print (ROI(days,amt))


