import random
# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# THIS PROGRAM CALCULATES ROI ON A $100 INVESTMENT PER DAY
# AVERAGE AMOUNT OF DAYS WORKED OVER A LIFETIME IS 90,000 HOURS, OR 3715 DAYS

#user enters how many days they invested for 
def ROI(days_worked,amt_invested)
    days_worked 
    def standard_and_poors


'''
def standard_and_poors(work_days, investment_amount):
    counter = 1
    avg_increase = 0.02739726027
    total_investment = investment_amount * counter

    return_on_investment = 0
    while counter <= work_days:
        # Calculate fluctuation for the day
        fluctuation = random.uniform(avg_increase * 50, avg_increase * 150)

        # Adjust ROI based on fluctuation (apply percentage change to the current value)
        daily_roi = investment_amount * fluctuation - investment_amount

        return_on_investment += daily_roi

        # Print out the ROI for the day
        print(f"\nROI on day {counter} after investing ${investment_amount:.2f} is ${daily_roi:.2f}")

        profit_earned = return_on_investment
        counter += 1
        print(f"\nStock Value after investing for {counter - 1} days is ${total_investment + daily_roi:.2f}")

    # Program prints total amount earned after investing x amount of days
    return return_on_investment

# Program prompts the user to enter how long they've been investing for
days = int(input("\nHow many days did you invest for? "))
amt = int(input("\nHow much did you invest per day? "))

# Program passes the user parameter into the argument used by the function "work_days"
'''
print(f"\nROI after investing ${amt * days:.2f} after {days} days is ${standard_and_poors(days, amt):.2f}\n")
