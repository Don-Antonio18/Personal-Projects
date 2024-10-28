def excludePunNum (input_string):

    if input_string == []:
        return 0
    else:
        puncs = ",.-?!;:^"
        new_lst = " "
        for char in input_string:        #for loop iterates each char in string
            if char in puncs or if char.isdigit():   # checks to see if char is puncuation mark
                continue    # function skips over integers
            new_lst += char    # adds legitimate character to string        
        return new_lst          #returns string of characters

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

def stringList(str1):
    # splits string into list of strings
    return str1.split() 

def encodedList(lst):
    if lst == []:  # Base case: empty list
        return []
    else:
        # encocdes the list and then reverse the order
        return encodedList(lst[1:]) + [encoded_string(lst[0])]
    
def decodedList(lst):
    if list == []:
        return []
    else: 
        # decodes the list reverses the list
        return decodedList(lst[1:]) + [decoded_string(lst[0])]
        
    

from lab4Q1 import excludePunNum
def main(s):
    slst=excludePunNum(s)
    eList = encodedList(stringList(slst))
    dList = decodedList(eList)
    print("Given string =>", s)
    print("Punctuation removed =>", slst)
    print("List Encoded =>", eList)
    print("List Decoded =>", dList)
    print("Encoded Message =>",' '.join(eList))

print (main("COMP1126!! Sci2024 is a, : lot of, fun?"))