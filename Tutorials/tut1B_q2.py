''' Tutorial 1B Question 2'''

'''A function is_coldday takes the temperature as Fahrenheit value as an argument and returns true if
the temperature is less than 50 and false otherwise.'''

def is_coldday(faren_temp):
       ''' if faren_temp < 50:
            return True
        else:
            return False'''
       return faren_temp < 50  #(BOOLEAN ARGUMENT returns TRUE or FALSE - NO NEED FOR IF/ELSE)
    
''' user provides input to pass into faren_temp parameter '''

temp_input = int(input("What is the temperature in farenheit? "))
print(is_coldday(temp_input))