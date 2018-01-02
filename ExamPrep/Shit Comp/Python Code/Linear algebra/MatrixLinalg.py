#scipy.linalg

#x=linalg.solve(A,b)#where A and b are matrices and vectors defined as arrays. Solves Ax=b where x is your output given as a vector 

#example
from scipy import linalg
import numpy as np

A=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]])
b=np.array([5.0,0.0,5.0,0.0]) 

x=linalg.solve(A,b)
print x
