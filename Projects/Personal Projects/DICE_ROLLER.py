import random
#* ● ┌ ─ ┐ │ └ ┘  
running = True
while running == True: 
    
    dice_dict = { 
            1: ("┌─────────┐", 
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"
    ), 
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            
            4:( "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            
            6:( "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘" ),   }
    dice = []
    total = 0
    print("----DICE ROLLLER.exe----")
    NumOfDice = int(input("How many dice to roll? (0 to quit): "))
    if NumOfDice == 0:
        print("Dice Roller Programme terminated successfully.")
        break
    else:
        orientation = str(input("Press 'v' to see them vertically, or 'h' to see them horizontally: "))
        if orientation == "v":
            #!---------Printing Dices Vertically------

            # randomize dice through list of die
            for die in range(NumOfDice):
                dice.append(random.randint(1,6))
            #print(dice)

            # Outer loop looping through each die
            for die in range(NumOfDice):
            # gets dice(value) for each key that was randomly chosen 
                for line in dice_dict.get(dice[die]):
                    print (line)
                
            # print num of dice
            for die in dice:
                total += die
            print(f"Total: {total}")
            
        elif orientation == "h":
            
        #!-------Printing Dices Horizontally------
        
            for die in range(NumOfDice):
                    dice.append(random.randint(1,6))
                
            # Each die is made up of 5 lines
            for line in range(5):
                for die in dice:
                    # get current val found within list of dice
                    print(dice_dict.get(die)[line], end="")
                print()
                
            total = sum(dice)
            print(f"Total: {total}")
                
        else:
            print("ValueError: Orientation Key not recognized. Enter v or h")
        
            
        # for die in dice:
        #     total += die
        # print(f"Total: {total}")
            
#! Things to add:
#! 1. make each dice blink one after the other
#! 2. Make menu blink
#! 3. add "rolling..." print statement and sleep func before displaying dice


                
                
                
            

