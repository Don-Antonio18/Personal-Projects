import time
import random

# S&P 500 average return per day (~0.0274%)
def standard_and_poors(work_days, investment_amount):
    avg_increase = 0.0002739726027  # Daily return as a percentage
    total_investment = investment_amount * work_days
    return_on_investment = investment_amount  # Start with the initial investment
    
    for day in range(1, work_days + 1):
        time.sleep(0.01)
        
        # Generate a random daily fluctuation in a more reasonable range
        fluctuation = random.uniform(avg_increase * 0.5, avg_increase * 1.5)
        
        # Apply the fluctuation to the current total investment value
        daily_roi = return_on_investment * fluctuation
        return_on_investment += daily_roi

        # Print the ROI for the current day
        print(f"\nDay {day}: Daily ROI is ${daily_roi:.6f}")
        print(f"Total value after {day} days: ${return_on_investment:.2f}")

    # Calculate total profit
    profit_earned = return_on_investment - total_investment
    return f"\nTotal ROI after {work_days} days of investing ${investment_amount} per day: ${return_on_investment:.2f}\nProfit: ${profit_earned:.2f}\n"

# Get user input
days = int(input("\nHow many days did you invest for? "))
amt = int(input("\nHow much did you invest per day? "))

# Run the calculation
print(standard_and_poors(days, amt))