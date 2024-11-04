#   ID Number: 620170333
#   Hackerrank Handle: antoniokerruni
#   Hackerank Exercise: Bird Watcher




''' function check_colour() that accepts a tuple with RBG 
(Red, Blue, Green) values. The function must 
return the string "R" if the bird is red, "G" if it is green and "B" if it is blue. 
If the bird's main colour does not match any of the above, 
the function must return "O" for other. '''
# function check colour accepts a tuple containing red,green and blue values
def check_colour(RGB):
    Red, Blue, Green = RGB
    if      Red > Blue + Green:
        return "R"
    elif    Green > Red + Blue:
        return "G"
    elif    Blue > Red + Green:
        return "B"
    else:   return "O"

''' if the decibel value falls between the ranges indicated 
the function must return the type value that the decibel is closer to.'''
# function chirp_range that accepts a parameter of decimal value 
def chirp_range(db):
    if   db <=25:
        return 1
    elif  db <= 35:
        # midpoint between 25 and 35 is 30, hence: 
        # bird is type 2 if db val is closer to 35 than it is to 25, & vice versa
        return 2 if (db - 30) <= (db -25) else 1
    elif 35 < db <= 77:
        return 2 
    elif 77 < db <= 89:
        # midpoint between 77 and 89 is 83, hence:
        # bird is type 3 if db val is closer to 89 than it is to 77, & vice versa
        return 3 if (db - 83) <= (db - 77) else 2
    elif db > 89:
        return 3
    else: 
        return 0

'''Complete the function bird_type() that uses the other two functions created to determine the bird
type. The function accepts five parameters. The first parameter is the beak type,
the second is the red value, then the green, then the blue value and finally the decibel value.

If all three characteristics point to the same bird type the function must return the string 
associated with that type ("T1", "T2" or "T3"). However, if only the beak type and the colour 
agrees (and the pitch disagrees) on the type the function should return "UD" for undecided.'''
def bird_type(btype, Red, Green, Blue, db):
    # create tuple containing inputs from check_colour
    colour = check_colour((Red, Green, Blue))
    chirp = chirp_range(db)

    if (btype, colour, chirp) == ("SCB", "R", 1):
        return "T1" if chirp == 1 else "UD"
    elif (btype, colour, chirp) == ("LSB", "B", 2):
        return "T2" if chirp == 2 else "UD"
    elif (btype, colour, chirp) == ("HB", "G", 3):
        return "T3" if chirp == 3 else "UD"



'''Complete the function closest_match() that accepts two parameters: the characteristics of the bird
recently observed and a list of tuples (Bird Database). 
Each tuple in the list has six elements. The first element is the family name of the bird, 
the second is its beak type, the third is the red value, then the green, then the blue value 
and finally the decibel value. The function iterates through the list and returns the family name 
of the bird with the closest match to the one just observed.

If the bird recently observed (a tuple of its beak type, red value, green value, blue value, 
decibel value) matches a type found in the list, return the name of 
the first bird that matches its type. Otherwise, compare the birds solely on chirp pitch. 
The bird in the database that has the closest pitch to the one observed is the closest match.'''

def closest_match(newbird, b_database):
   # Unpack the new bird's characteristics using * to pass them as individual parameters to bird_type()
    new_bird_type = bird_type(*newbird)
    closest_match = ""
    min_difference = float('inf')  # Initialize min_difference as infinity

    for bird in b_database:
        # Unpack the bird's characteristics from the database tuple
        (family_name, btype, Red, Green, Blue, db) = bird

        # Get the bird type for the current bird in the database
        b_database_type = bird_type(btype, Red, Green, Blue, db)

        # If the new bird's type matches the current bird's type, update closest_match and break the loop
        if new_bird_type == b_database_type:
            closest_match = family_name
            break
        else:
            # Calculate the absolute difference between the new bird's decibel value and the current bird's decibel value
            difference = abs(db - newbird[4])

            # If the difference is smaller than the current minimum difference, update closest_match and min_difference
            if difference < min_difference:
                min_difference = difference
                closest_match = family_name

    return closest_match

    

