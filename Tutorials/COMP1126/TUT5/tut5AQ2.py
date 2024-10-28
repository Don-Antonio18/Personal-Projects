'''
this function collects a string and returns the amount of     list_of_vowels in it
'''
def vowels(lst):
    if lst == "":
        return 0
    list_of_vowels = "aeiouAEIOU"
    if lst[0] in       list_of_vowels:
        return 1 + vowels(lst[1:])
    else:
        return vowels(lst[1:])
# word1 = str(input("\nEnter word to detect # of vowels "))
# print (vowels(word1))

# this functions returns the # of punctuations marks in a string
def punctuations(lst):
    if lst == "":
        return 0
    puncs = ",.;:?!"
    if lst[0] in puncs:
            return 1 + punctuations(lst[1:])
    else:
            return punctuations(lst[1:])
# word2 = str(input("\nEnter a string to detect # of punctuations marks: "))
# print (punctuations(word2))

# this func returns the # of consonants in a string
def consonants(lst):
    if lst == "":
        return 0
    consts = "BbCcDdFfgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ."
    if lst[0] in consts:
        return 1 + consonants(lst[1:])
    else:
        return consonants(lst[1:])
# word3 = str(input("\nEnter a string to detect # of consonants: "))
# print (consonants(word3))

'''
A function remove_spaces and main has been defined. What would be the output of these
functions?

'''
def remove_spaces(string):      #defines function with parameter (string)
    new_string = ""             # initialises an empty string
    for char in string:         # iterates through the passed argument
        if char != " ":         # checks if character is NOT a space
            new_string += char  #inputs empty charcter into new string
    return new_string       #returns the string with the new character


text="\nHello, how are you? I hope you have enjoyed this course!!\
In this course you have learnt how to solve problems; write python \
code; and have fun"             # text input



def main():                     # defines function main with empty parameter
    print(text)                 # prints text string from above
    st = remove_spaces(text)    # calls function with text input passed as an arugment
    print("Vowels = ",     vowels(st))          # prints # of vowels in the string
    print("Consonants = ", consonants(st))      # prints the # of consonants in the string
    print("punctuationss = ", punctuations(st)) # prints the number of punctuations in the string
    
main()  #calls main function