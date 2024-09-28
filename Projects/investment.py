import time
import random
# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# THIS PROGRAM CALCULATES ROI ON A $100 INVESTMENT PER DAY
# AVERAGE AMOUNT OF DAYS WORKED OVER A LIFETIME IS 90,000 HOURS, OR 3715 DAYS
def standard_and_poors(work_days, investment_amount):
    counter = 1
    avg_increase = .02739726027 
    total_investment = investment_amount * work_days
    
    return_on_investment = 0
    while counter <= work_days: #''code limits the days counted towards earnings by the amount of days invested'''
        time.sleep(0.01)
        # Calculate fluctuation for the day
        #fluctuation = random.uniform( avg_increase / 2, avg_increase * 2)
        fluctuation = random.uniform( avg_increase * 50, avg_increase * 150)

        #Adjust ROI based on fluctuation (apply percentage change to the current value)
        daily_roi = investment_amount * fluctuation # Multiply by the fluctuation rate

        return_on_investment +=  daily_roi

        # Print out the ROI for the day
        print(f"\n ROI on day {counter} after investing {investment_amount} is ${daily_roi:.6f}")

        # Print out the ROI for the day
        print(f"\n ROI on day {counter} after investing {investment_amount} is ${daily_roi:.2f}")

        profit_earned = return_on_investment - total_investment
        counter += 1 
        print(f"\n Stock Value after investing for {counter -1} days is ${investment_amount + daily_roi:.2f}")
    #program prints total amount earned after investing x amount of days'''
    return f"\n ROI after investing ${investment_amount * work_days} after {counter - 1} days is ${daily_roi:.2f}\n"

#program prompts the user to enter how long they've been investing for    
days = int(input("\nHow many days did you invest for? ")) 
amt = int(input("\nHow much did you invest per day? "))

#program passes the user parameter into the argument used by the function "work_days"   
print (standard_and_poors(days, amt))

