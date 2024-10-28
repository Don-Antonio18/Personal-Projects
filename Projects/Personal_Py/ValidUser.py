name = input("Enter your full name:")
#username should be no more than 12 characters
#username should not contain digits
#username should not contain spaces

if len(name) > 12 or name.count(" ") > 0 or name.isalpha != True:
    print("invalid user input")
else:
    print(f"Welcome,{name}")
