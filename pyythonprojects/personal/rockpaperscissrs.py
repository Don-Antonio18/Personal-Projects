import sys
import time
import random

def blink_text(text):
    count = 1
    while True:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(1.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)
        
""" Initialise print statements: """
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

blink_text("Welcome to Rock Paper Scissors!" ,
        "Best out of 3 rounds. .😈")

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
    user_input = int("Rock (r), paper (p) or scissors (s) ? ")
    
    
    
    pass



