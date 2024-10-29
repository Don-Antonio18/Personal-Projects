name = ("Enter your name: ")
print(help(str))

#returns the number of characters in a string.
length = len(name)

# converts the first character of a string to uppercase and makes all other characters lowercase.
size = name.capitalize()

#returns True if all characters in the string are alphanumeric (either alphabets or numbers).
alphanumeric = name.isalnum()

#True if all characters in the string are alphabets.
alphabetic = name.isalpha()

# True if all characters in the string are digits.
digit = name.isdigit()

# returns True if all characters in the string are uppercase.
result = name.isupper()

#returns True if all characters in the string are lowercase.
result = name.islower()

# converts all characters in a string to uppercase.
result = name.upper()

# The lower() function converts all characters in a string to lowercase.
result = name.lower()

#the count() function returns the number of characters that meet the condition

phone_number = input("enter ur phone number: ")
# check to see how much dashes in phone num:
dashes = phone_number.count("-")

#removes all dashes in phone number by replacing with empty string
clean_num = phone_number.replace("-","")
print(phone_number)





