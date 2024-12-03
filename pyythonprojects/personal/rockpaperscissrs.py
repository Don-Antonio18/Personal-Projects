import sys
import time
import random
""" figure out how to make text blink """
print("Welcome to Rock, Paper, Scissors!")


art = {
    "rock": ( 
    "    _______",
    "---'   ____)",
            "(_____)",
            "(_____),",
            "(____)",
    "---.__(___)" ),
    
    "paper":(
        "_______",
    "---'   ____)____",
    "          ______)",
    "          _______)",
    "         _______)",
    "---.__________)" 
    ),

    "scissors": (
    "    _______)",
    "---'   ____)____",
    "          ______)",
    "       __________)"
    "      (____)",
    "---.__(___)"
    ),
    }

running = input("Choose Scissors (s), Paper(p), or Rock(r). Press'q to quit. \n").lower()
if running in ["spr"]: running =  True
elif running == "q": running = False
else: print ("You pressed the wrong button there, bud.")

while running == False:
    print("Thanks for playing! 😉")
    exit()

while running == True: 
    user_input = ("Rock (r), paper (p) or scissors (s) ? ")
    """ randomize bot pick from options list"""
    options = ["rock","paper", "scissors"]
    roll = random.choice(options)
    

    



