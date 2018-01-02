# GaussElimination

#when you have a matrix A and a vector b you can solve you system using gaussian elimination in the following way say you would solve Ax=b where x is your output 

# x=gaussElimin(A,b) #where A and b are matrices and vectors defined as arrays  
# print x #gives out a vector

#example (assesment 1 Q1)

import numpy as np
from gaussElimin import * 

A=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]])
b=np.array([5.0,0.0,5.0,0.0])

x=gaussElimin(A,b)
print x
