import time
import random

def standard_and_poors(work_days, investment_amount):
    counter = 1
    avg_increase = 0.0002739726027  # 0.02739726027 percent daily return
    total_investment = investment_amount * work_days
    return_on_investment = 0

    while counter <= work_days:
        time.sleep(0.01)

        # Calculate fluctuation for the day
        fluctuation = random.uniform(avg_increase * 50, avg_increase * 150)  # Fluctuation within a reasonable range

        # Calculate the daily ROI based on the initial investment and fluctuation
        daily_roi = investment_amount * fluctuation

        # Add the daily ROI to the total ROI
        return_on_investment += daily_roi

        # Print out the ROI for the day
        print(f"\nROI on day {counter} after investing {investment_amount} is ${daily_roi:.6f}")

        counter += 1 

    profit_earned = return_on_investment
    print(f"\nTotal earnings after {work_days} days: ${return_on_investment:.2f}")
    print(f"Initial investment: ${total_investment:.2f}")
    print(f"Profit earned: ${profit_earned:.2f}")
    
    return f"\nROI after investing ${investment_amount} per day for {counter - 1} days is ${profit_earned:.2f}\n"

# Program prompts the user to enter how long they've been investing for    
days = int(input("\nHow many days did you invest for? ")) 
amt = int(input("\nHow much did you invest per day? "))

# Pass the user parameter into the function
print(standard_and_poors(days, amt))