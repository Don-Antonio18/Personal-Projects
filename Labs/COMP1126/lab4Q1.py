def excludePunNum (input_string):
    if input_string == []:
        return 0
    else:
        puncs = ",.-?!;:^"
        new_lst = " "
        for char in input_string:        #for loop iterates each char in string
            if char in puncs:   # checks to see if char is puncuation mark
                continue        # function skips over punctuation marks
            if char.isdigit():  # checks to see if char is integer
                continue        # function skips over integers
            new_lst += char    # adds legitimate character to string        
        return new_lst          #returns string of characters



