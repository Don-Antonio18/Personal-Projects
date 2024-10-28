# FIBONACCI SEQUENCE
# (the previous 2 numbers are added to get 
# the next number in sequence)

# let n represent the # of months:
# let fibonacci(n) represent the # of rabbit pairs

# 	n = 0, 1 , 2 , 3, 4, 5, 6, 7, 8…..
#  fibonacci(n) = 0, 1 , 1, 2, 3, 5, 8, 13, 21….

# fibonacci(4) = fibonacci(3) + fibonacci(2)
# 	2 = 1 + 1

# fibonacci(3) = fibonacci(2) + fibonacci (1)
# 	1 = 1 + 0

# fibonacci(2) = fibonacci(1) + fibonacci(0)
# 	1 = 1 + 0

#return fibonacci(n-1) + fibonacci(n-2) 
		#code returns the fibonnaci sequence value of the index


	#code creates empty python dictionary 
import sys
def fibonacci(n,  dictionary ={}): 
	sys.setrecursionlimit(999999999)
	n = int(n)
		#checks to see if n index is in dictionary
	if n in dictionary: 
		#code returns current index of n 
		return dictionary[n]
	# code sets base cases
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		#code updates values of dictionary
		dictionary[n] = fibonacci(n-1, dictionary) + fibonacci(n-2, dictionary) 
		#code returns new dictionary value
		return dictionary[n]
		
position = int(input("\nWhich number of the fibonnaci sequence do you want?: "))
print (f"\nThe {position}th number of the fibonnaci sequence is", fibonacci(position))


