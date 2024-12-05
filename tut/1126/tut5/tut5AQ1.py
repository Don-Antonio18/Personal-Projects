#Question 1
#What does the following code do:
def outer_function():
    print (x)

# this functions prints current value of x (20)

    def inner_function(y):
        print (y)
        print(x+y)
        
    inner_function(20)
    # function calls itself with 20 passed to parameter y

x =10
outer_function()
# 1. program calls outer function, which prints evaluated everything outside the inner function
#       this means that it prints x(10) first 
# 2. program then calls inner function, which prints y(20) then prints x + y (30)

