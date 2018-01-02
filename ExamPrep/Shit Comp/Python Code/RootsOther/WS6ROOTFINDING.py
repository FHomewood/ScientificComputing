# module imports
from math import sqrt



# *****IMPORTANT*****
#The function must equal 0.

#IMPORTANT
#These methods (excluding in-build fsolve) require a bracket in which each root is found. These brackets can be found by looking at a plot.
# For example, on a plot of (y = x^2 - 1) there are two roots. An estimate for the upper and lower brackets could be -1.5 and -0.5 and 0.5 for the first root 0.5 and and 1.5 for the second root. (The actual roots are x=+1 and x=-1).

###########################################################################

# defining function f on range x
x = Np.linspace(xmin,xmax,numberofxvalues)
def f(x):
	return x**2

###########################################################################

# Ridder's Method (do this for each root)

import ridder
# root = ridder(function, lower bracket, upper bracket, tolerance)
root = ridder.ridder(f,a,b,tol=1.0e-9)
# Each root is returned as one number.

###########################################################################

# Newton-Raphson Method (do this for each root)

import newtonRaphson
#defining derivative of g (differentiate by hand)
def df(x):
	return x**2
# root = newtonRaphson(function, dervivative of function, lower bracket, upper bracket, tolerance)
root = newtonRaphson.newtonRaphson(f,df,e,k,tol=1.0e-9)
# The root is returned as one number.

###########################################################################

# In-build fsolve Method (returns both roots in an array and so the upper and lower brackets are of the entire interval in which all roots lie).

from scipy.optimize import fsolve
# root = fsolve(function, [lower limit of INTERVAL, upper limit of INTERVAL])
root = fsolve(f,[intlow,intupp])
# The roots are returned in array and are seperated out and defined individually below.
1stroot = root[0]
2ndroot = root[1]

###########################################################################

# Bisection Method (do this for each root)

import bisection
# root = bisection.bisection(function, lower bracket, upper bracket, switch=1, tolerence)
root = bisection.bisection(f,x1,x2,switch=1,tol=1.0e-9)
# The root is returned as one number.

###########################################################################





