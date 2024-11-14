import time
import random

# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# THIS PROGRAM CALCULATES ROI ON A $100 INVESTMENT PER DAY
# AVERAGE AMOUNT OF DAYS WORKED OVER A LIFETIME IS 90,000 HOURS, OR 3715 DAYS

def standard_and_poors(work_days, investment_amount):
    avg_increase = 0.02739726027  # Average daily percentage increase
    total_investment = investment_amount * work_days
    total_stock_value = investment_amount  # Start with the first day's investment
    
    counter = 1
    return_on_investment = 0

    while counter <= work_days:  # Loop through the number of work days
        time.sleep(0.009)
        
        # Calculate fluctuation for the day (random percentage applied to current stock value)
        fluctuation = random.uniform(avg_increase * 0.5, avg_increase * 1.5)

        # Adjust stock value based on fluctuation
        daily_roi = total_stock_value * fluctuation  # Multiply by fluctuation rate
        total_stock_value += daily_roi  # Accumulate the stock value
        
        # Print out the ROI for the day
        print(f"\n ROI on day {counter} after investing ${investment_amount:.2f} is ${daily_roi:.6f}")

        # Print out the stock value for the day
        print(f"\n Stock Value after investing for {counter} days is ${total_stock_value:.2f}")

        # Calculate profit earned
        # profit_earned = total_stock_value - total_investment
        # print(f"\n Profit earned so far: ${profit_earned:.2f}")

        counter += 1  # Increment the day counter

    # Program prints total amount earned after investing for x amount of days
    roi = total_stock_value - investment_amount
    return f"\n Final ROI after investing ${total_investment:.2f} over {work_days} days is ${roi:.2f}\n"

# Program prompts the user to enter how long they've been investing for    
# Uncomment the following lines to take input from the user
days = int(input("\nHow many days did you invest for? ")) 
amt = int(input("\nHow much did you invest per day? "))

# Uncomment this to execute the function with user inputs
print(standard_and_poors(days, amt))

'''
For numbers bigger than 100, ROI values become inaccurate 

'''