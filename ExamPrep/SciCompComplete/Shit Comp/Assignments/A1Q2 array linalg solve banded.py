# ***Question 2***

import numpy as np
import scipy as sp
from scipy import linalg

print "Following the equations given to us in the question, the boundaries they impose call for the following matrix in order for them to be represented:"
M = np.zeros([10,10]) # creates an array of zeroes

for i in range (0,9,1): # for within the array, up until the 9th line out of 10, these rules apply:
    M[i,i-1]=-1 # in the array, the integer at (n, n-1) = -1 
    M[i,i]=4 # in the array, the integer at (n,n) = 4 
    M[i,i+1]=-1 # in the array, the integer at (n, n+1) = -1
    
for i in range (9,10,1): # continuing the rules for the 10th and last line because there was an error on the last line under the previous constrictions as we fell outside of our range
    M[i,i-1]=-1 # in the array, the integer at (n, n-1) = -1 
    M[i,i]=4 # in the array, the integer at (n,n) = 4 
    

print M

print "Now to convert it into a cm matrix, i.e. a matrix storing (economically) the non-zero matrix elements."

CM = np.array([[0,-1,-1,-1,-1,-1,-1,-1,-1,-1],[4,4,4,4,4,4,4,4,4,4],[-1,-1,-1,-1,-1,-1,-1,-1,-1,0]], dtype=float)# the dtype=float is to avoid rounding errors

print CM

print "In order to complete the tridiagonal calculation, we also need the RHS matrix (vector), which is composed of the answers to each of the equations given to us in the question ie holding the right hand side of the system."

RHS = np.array([[9],[5],[5],[5],[5],[5],[5],[5],[5],[5]], dtype=float) # again, avoiding rounding errors with floats

print RHS

print "Finally, we obtain our tridiagonal matrix's solution:"

TM = sp.linalg.solve_banded((1,1),CM,RHS) # the (1,1) means that we want to include the 1 diagonal above and 1 diagonal below the main diagonal

print TM 



