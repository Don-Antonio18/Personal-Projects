#Tutorial 1B Question 1

#this program uses a func to convert celcius to farenheit
#it is possible to input data into function
#you can write temporary variable inside of () known as arguments
#add variable to the function with function type, for eg (f" " {variable name}")
#[used f for fstring]

def calcFarenheit(celcius):                                                 #funcdefines celcius as a parameter
    faren_temp  = (celc_temp * 9)  / 5  + 32                                #func calculates F temp based on input
    print(f"{celc_temp} Celcius is equal to {faren_temp} in Farenheit ")    #func writes response to user


celc_temp  = int(input("WHat is the temperature in Celcius? "))             #func prompts user to input Celc temp to pass to parameter
print(calcFarenheit(celc_temp))
