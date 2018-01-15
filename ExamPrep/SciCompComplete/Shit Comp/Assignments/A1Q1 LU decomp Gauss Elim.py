# ***Question (1)***
# 
# Part (a)
# 
# Simultaneous equations for the loops:
# 80*i1-50*i2-30*i3 = 240
# 50*i1-100*i2-10*i3-25*i4 = 0
# -30*i1-10*i2+65*i3-20*i4 = 0
# -25*i2-20*i3-100*i4 = 0


# Part (b)

import scipy as sp
import numpy as np
import gaussElimin as gE

A = sp.array([[80.0,-50.0,-30.0,0.0],[-50.0,100.0,-10.0,-25.0],[-30.0,-10.0,65.0,-20.0],[0.0,-25.0,-20.0,100.0]]) # array of coefficients in simultaneous equations
b = sp.array([240.0,0.0,0.0,0.0]) # results for all the simultaneous equations



print "For the first array, plug in all of the coefficients of the simultaneous equations derived from the circuit diagrams. This array, A:"
print A

print "For the second array, plug in all the results of the simultaneous equations derived from the circuit diagram. This array, b:"
print b 


x = gE.gaussElimin(A,b)

print "Using the Gaussian elimination module, we can solve:"
print x 

# Part (c)

from scipy import linalg

P, L, U = linalg.lu(A) # computes LU factorisation explicitly where P is the permutation matrix, L is the lower triangular matrix, and U is the upper triangular matrix

print "We can use an LU (Lower-Upper) decomposition to decompose our resultant matrix into an upper part and a lower part. The lower part:"
print L

print "And the upper part:"
print U

# Part (d)

print "Next, use the LU decomposition to solve Ax = b"

y1 = gE.gaussElimin(L,b) # lower triangular matrix and b

x1 = gE.gaussElimin(U,y1) # upper triangular matrix and the gE of lower and b
print x1

print "Now we want to use our LU decomposition to prove that we can go the other direction and get an answer from it too." 
print "Using a new array where the voltage across is 120 V instead of 240 V (as the range is 0 V to +120 V instead of -120 V to +120 V:"

c = sp.array([240.0,0.0,0.0,0.0]) # new b array where the -120 V is = 0 V

y2 = gE.gaussElimin(L,c) # same process as with y1 and x1

x2 = gE.gaussElimin(U,y2)


print x2



