''' rational numbers r1 and r2 need to be added
    r1 is a tuple of numerator
    r2 is a tuple of denominator
    A rational num = quotient of numerator / denominator, where denominator != 0 '''
    


# 1. Create function naive-add that returns sum of r1 + r2

def naive_add(r1, r2):
    r1 = (n1, d1)
    n2 = (n1, d2)
    return (n1*d2 + n2*d1) / (d1*d2)

''' The software vendor Rational Numbers Inc. defines 
    a constructor for a rational number using
    the function make-rational below. '''
    
def make_rational(numerator, denominator):
    return ["rational", (numerator,denominator)]
    # return {"numer": numer, "denom": denom} 

''' Implement a function rat_add that adds two rational numbers r1 and r2.'''

''' Complete Rational’s rational number ADT by implementing 
functions get_numer and get_denum
that return the numerator and denominator respectively, 
given a rational number r   ''''

#function to make rational num:
def make_rat(numerator, denominator):
   # quotient = quotient < denominator (numerator, denominator)
   # return [ numerator // quotient,  denominator // q]
    return ["rational", numerator, denominator]

def get_numer(r):
    return r[1] #returns numerator (index 1 in rational tuple)

def get_denum(r):
    return r[2] #returns denominator (index 2 in rational tuple)

''' Use the rational number ADT to implement the functions rat_add, rat_subt, rat_mult and rat_div that
implement addition, subtraction, multiplication and division of rational numbers respectively.'''

def rat_add(r1, r2):
    n1 = get_numer(r1)
    d1 = get_denum(r1)
    n2 = get_numer(r2)
    d2 = get_denum(r2)
    return make_rat((n1*d2 + n2*d1) / (d1*d2))

def rat_subt(r1,r2):
    n1 = get_numer(r1)
    d1 = get_denum(r1)
    n2 = get_numer(r2)
    d2 = get_denum(r2)
    return make_rat((n1*d2 - n2*d1) / d1*d2)
    
def rat_mult(r1,r2):
    n1 = get_numer(r1)
    d1 = get_denum(r1)
    n2 = get_numer(r2)
    d2 = get_denum(r2)
    return make_rat((n1*n2 ) / d1*d2)

def rat_mult(r1,r2):
    n1 = get_numer(r1)
    d1 = get_denum(r1)
    n2 = get_numer(r2)
    d2 = get_denum(r2)
    return make_rat((n1*d2 ) / d1*n2)

''' Quite often it is required that a rational number be written in its simplest terms, by dividing
both the numerator and the denominator by the greatest common divisor. The function gcd,
given below, returns the greatest common divisor of two numbers given as arguments.'''

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
    






    
