'''
rational numbers r1 and r2 need to be added
r1 is a tuple of numerator
r2 is a tuple of denominator

A rational num = quotient of numerator / denominator, where denominator != 0

1. Create function naive-add that returns sum of r1 + r2
'''

def naive_add(r1, r2):
    r1 = (n1, d1)
    n2 = (n1, d2)
    return (n1*d2 + n2*d1) / (d1*d2)

''' The software vendor Rational Numbers Inc. defines 
    a constructor for a rational number using
    the function make-rational below. '''
    
def make_rational(numer, denom):
    return ["rational", numer,denom]

''' Complete Rational’s rational number ADT by implementing 
functions get_numer and get_denum
that return the numerator and denominator respectively, 
given a rational number r   ''''

def get_numer(r):
    return r[1]

def get_denum(r):
    return r[2]

''' Use the rational number ADT to implement the functions rat_add, rat_subt, rat_mult and rat_div that
implement addition, subtraction, multiplication and division of rational numbers respectively.'''

def rad_add(r1, r2)