#Imports

from romberg import * # Have the romberg file and the trapezoid integration file provided on study direct in the same folder as your code.

#Constants
LowerLimit = 0
UpperLimit = 10

#Defining Function
def function(x):
	return (x**2)

#Returns the integral and the number of panels used. Unless stated otherwise, leave the last term as "tol=1.0e-6". tol stands for tolerance, and controls the size of the error.
#Answer[0] = Numerical value of definite integration.
#Answer[1] = Number of panels (Number of trapeziums used).
Answer = romberg(function,LowerLimit,UpperLimit,tol=1.0e-6)

print Answer


