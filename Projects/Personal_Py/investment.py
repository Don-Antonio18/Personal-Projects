# S & P 500 RETURNS AROUND 11% PER YEAR ON AVERAGE, WHICH IS 0.02739726027 PERCENT PER DAY
# Program simulates return on investment of $(input) after specified period given by user
# in future, programme should get api from investment project to detect stock history and predict future trend
#programme should also prompt user to choose which stock market to simulate return on

# function is defined with days and principal as argument
import random
def StockSim(days, principal):
    FluctRate = random.uniform((0.0274 * 2), ( 0.0274 / 2))
    TotalReturn = 0 
    
    #increments total return per day, randomly fluctuating profit
    for day in range(int(days)):
    #eg.DailyReturn = ( 100 + ( 100 * 0.1) ) = 101
        DailyReturn = principal + (principal * FluctRate)
        TotalReturn += DailyReturn
        
    years = days / 360
    YearlyPrincipal = principal * (days/365)
    YearlyReturn = principal * ((1 + FluctRate / 100) ** years - 1) * YearlyPrincipal
        
    return (f"Total ROI after {days} days of investing is ${TotalReturn:.2f} \n"
            f" Total ROI after {years:.1}years of investing is {YearlyReturn:.2f}")

days_input = float(input("How many days did you invest for?: "))
principal_input = float(input("How much did you invest per day?: "))
print (StockSim(days_input,principal_input))