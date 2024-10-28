import random
# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# THIS PROGRAM CALCULATES ROI for n days based on inputted INVESTMENT  amount PER DAY
# in future programme should api from investment project to detect stock history and predict future trend

#user enters how many days they invested for 
def ROI(days_invested,amt_invested):
    counter = 1
    while counter <= days_invested:
        # calculate the ROI for the day
        # daily investment of $100 = (100 * ( 1 + 0.02739726027)) - 100 ) = 2.739726027 after 1st day
        daily_roi = amt_invested * (1 + amt_invested) - amt_invested

        # print the ROI for the day
        print(f"\nROI on day {days} after investing ${amt_invested:.2f} is ${daily_roi:,.2f}")

        profit_earned = daily_roi * days
        print(f"\nStock Value after investing for {days} days is ${amt_invested * (1 + daily_roi) ** days:.2f}")

        # fix calculation for compound return on investment
        

        counter += 1

days = int(input("How many days did you invest for?: "))
amt = float(input("How much $ did you invest per day?: "))
print (ROI(days,amt))


