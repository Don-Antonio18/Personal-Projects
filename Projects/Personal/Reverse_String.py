'''? to reverse a string, just set the step to be -1'''
# [start:end:step]

#reversestring = str(input("Enter text to revese it: "))
# leave star and end empty, just set the step to be -1 
#print (reversestring[::-1])


#reverselist = [1,2,3,4,5,6,7,8,9]
#print (reverselist[::-1])

#* using reversed() function to reverse the input
# num_list = list(input("Enter a list of numbers: "))
# print ([num for num in reversed(num_list)])

name_list = str(input("Enter Your Name: "))
print ([char for char in reversed(name_list)])