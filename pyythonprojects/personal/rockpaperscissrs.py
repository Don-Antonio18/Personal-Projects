import sys
import time
import random
""" figure out how to make text blink """
print("Welcome to Rock, Paper, Scissors!")
user_input = input("Will you choose Scissors, Paper, or Rock?\n").lower()

options = {
    1: ( 
    "    _______",
    "---'   ____)",
            "(_____)",
            "(_____),",
            "(____)",
    "---.__(___)" ),

    2:(
        "_______",
    "---'   ____)____",
    "          ______)",
    "          _______)",
    "         _______)",
    "---.__________)" 
    ),

    3: (
    "    _______)",
    "---'   ____)____",
    "          ______)",
    "       __________)"
    "      (____)",
    "---.__(___)"
    ),
    }



running = int(input("Enter s to start, or q to quit." ))

if running == "s": running =  True
if running == "q": running = False

while running == False:
    print("Thanks for playing! 😉")
    exit()

while running == True: 
    """ randomize bot pick from dictionary"""
    roll = random.sample(options.items(), 1)
    
    #get user input:
    user_input = ("Rock (r), paper (p) or scissors (s) ? ")
    
    
    
    pass



