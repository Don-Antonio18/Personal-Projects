'''
Write a recursive function in python which calculates the greatest common divisor of two
integers i.e. the largest integer that divides both a and b with no remainder. For example, the
GCD of 16 and 28 is 4. The method for computing GCD is the Euclid’s algorithm. It is based on
the observation that, if r is the remainder when a is divided by b, then the common divisor of a
and b are precisely the same as common divisors of b and r. Thus we can use the equation:
gcd(a,b)= gcd(b,r)
For example,
gcd(206,40) = gcd(40,6)
= gcd(6,4)
= gcd(4,2)
=gcd(2,0)
=2
where 2 is the gcd of 206 and 40.



'''