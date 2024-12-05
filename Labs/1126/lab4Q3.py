def decoded_string(lst):
    if lst == "":
        return ""
    else:
        char = ord(lst[0]) #gets ascii value of chaarcter
        if char % 2 == 0:  # checks if ascii of char is even
            char -= 4       # subtracts 4 from value
        else:               # otherwise it is odd so no elif needed
            char -= 2       # subtracts 2 to value
        # returns new string
        return chr(char) + decoded_string(lst[1:])

def encoded_string (lst):
    if lst == "":
        return ""
    else:
        char = ord(lst[0]) #gets ascii value of chaarcter
        if char % 2 == 0:  # checks if ascii of char is even
            char += 4       # adds 4 to value
        else:               # otherwise it is odd so no elif needed
            char += 2       # adds 2 to value
        # returns new string
        return chr(char) + encoded_string(lst[1:])
