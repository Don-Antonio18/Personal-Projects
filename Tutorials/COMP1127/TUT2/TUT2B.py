'''
rational numbers r1 and r2 need to be added
r1 is a tuple of numerator
r2 is a tuple of denominator

A rational num = quotient of numerator / denominator, where b!= 0

1. Create function naive-add that returns sum of r1 + r2
'''
r1 = (numer, denom)
r2 = (numer, denom)
def naive_add(r1, r2):
    return (r1[0] * r2[1] + r2[0] * r1[1]) / r1[1] * r2[1]

'''
The software vendor Rational Numbers Inc. defines 
a constructor for a rational number using
the function make-rational below.
'''
def make_rational(numer, denom):
    return [("rational", numer,denom)]

'''
Complete Rational’s rational number ADT by implementing 
functions get_numer and get_denum
that return the numerator and denominator respectively, 
given a rational number r
'''

def get_numer(r):
    return make_rational(numer)

def get_denum(r):

    return make_rational(denom)
