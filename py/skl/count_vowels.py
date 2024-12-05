def count_vowels(str):
    c = 0 
    for i in str:
        if i == "a" or i == "e" or i == "i" or i == "o":
            c = c + 1
    return c

count_vowels("orange")