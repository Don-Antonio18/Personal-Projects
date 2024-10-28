name = ("Enter your name: ")
print(help(str))

length = len(name)
size = name.capitalize()
alphanumeric = name.isalnum()
alphabetic = name.isalpha()
digit = name.isdigit()
result = name.upper()
result = name.isupper()
result = name.islower()
result = name.lower()

phone_number = input("enter ur phone number: ")
# check to see how much dashes in phone num:
dashes = phone_number.count("-")

#removes all dashes in phone number by replacing with empty string
clean_num = phone_number.replace("-","")
print(phone_number)





