
#! Question 1 
'''Draw the hierarchy chart and then plan the logic for a program that calculates a
person s body mass index (BMI). BMI is a statistical measure that compares a
person s weight and height.

The program uses three modules.
● The first prompts a user for and accepts the user's height in inches.
● The second module accepts the users weight in pounds and converts the user's height
to meters and weight to kilograms.
● Then, it calculates BMI as weight in kilograms divided by height in meters squared, and
displays the results.
There are:
● 2.54 centimeters in an inch
● 100 centimeters in a meter
● 453.59 grams in a pound
● and 1,000 grams in a kilogram.
Use named constants whenever you think they are appropriate.
The last module displays the message, End of job.'''


User_Height = float(input("Enter your height in inches: "))
User_Weight = float(input("Enter your weight in pounds(lbs): "))

#* module below converts user's height to meters and weight to kilograms:
User_Height = User_Height * 2.4
User_Weight = User_Weight * 0.453592
User_BMI = User_Weight / (User_Height ** 2)
print ("End of job")


#! Question 2

#? Main Program: 
'''
declare customer_name as string
declare num_of_bathrooms as integer
declare other_rooms as integer
declare service_charge as float
'''

#? Housekeeping module:
customer_name = str(input("Please enter your last name: ")) #takes user input of their last name

#? Detail Loop: 
num_of_bathrooms = int(input("Enter the number of bathrooms: ")) # takes user input of the # of bathrooms
other_rooms = int(input("Enter how many rooms need to be cleaned: ")) # takes user input of other rooms 
service_charge = (40 + (num_of_bathrooms * 15) + (10 * other_rooms)) # calculates service charge
print (service_charge) # displays service charge
print("Program is complete") #displays a message tht indicates the program is complete


#! Question 3
'''Design a program that:
● prompts the user for a lot number in the River Falls subdivision
● and data about the home to be built there
● Including…
○ number of bedrooms
○ number of bathrooms
○ and the number of cars the garage holds
The program output is:
● the price of the home
● which is a $50,000 base price
● plus $17,000 for each bedroom
● $12,500 for each bathroom
● and $6,000 for each car the garage holds.
Use named constants where appropriate. Also, use appropriate modules, including one that
displays End of job when the program ends.'''

#* User input Module:
lot_number = int(input("Enter your lot number: ")) # prompts user for their lot number 

#* House Information Module:
bedroom_num = int(input("How many bedrooms should be built? "))
bathroom_num = int(input("How many bathrooms should be built? "))
garage_num = int(input("How many cars should the garage hold? "))

#* Cost calculation module:
base_price = 50000
bedroom_cost = 17000 * bedroom_num
bathroom_cost = 12500 * bathroom_num
garage_cost = 6000 * garage_num

#* Program ending module:
print("End of Job")

