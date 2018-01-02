#Forming Matrices

#for a matrix thats elements depend on a function use the following code

A=zeros((n,m),float) #creates a n by n matrix of zeros as n and m

for i in range (0,n):
	for j in range (0,m):
		A[i,j]=(i+j)**2  # where n/m is the matrix lenght/width and (i+j)**2 defines each a component as the row and collumn number added and squared change depending on function

------------------------------------------------------------------------------------------------------------------------------------------

#for a matrix that is given as inital values use an array for example
A=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]]) 

----------------------------------------------------------------------------------------------------------------------------------------

# GaussElimination / scipy.linalg
#uses the imports 
from gaussElimin import * #where gaussElimin is a file on study direct
from scipy import linalg 

#when you have a matrix A and a vector b you can solve you system using gaussian elimination in the following way say you would solve Ax=b where x is your output 

#from Q1.py assesment 1 part B
x=gaussElimin(A,b) #where A and b are matrices and vectors defined as arrays  
print x #gives out a vector

-----------------------------------------------------------------------------------------
#scipy.linalg

x=linalg.solve(A,b)#where A and b are matrices and vectors defined as arrays solves Ax=b where x is your output given as a vector 

-----------------------------------------------------------------------------------
#LU Decompositopn 
from scipy import linalg
 
#from Q1.py assesment 1 part C
P, L, U = linalg.lu(A)
#where L is the lower triangular matrix, U is the upper triangular matrix and P is the permutaion matrix 

#to solve the syatem Ax=b using the L and U matrices (from Q1.py assesment 1 part d) you have made use 
from gaussElimin import *

xL=gaussElimin(L,b) #gaussElimin changes b so no need to recombine xL and x

x=gaussElimin(U,b) #where x is shown as a vector and is the final answer or 'x' from Ax=b

print dot(dot(L,P),U)#checks answer by geting back to origonal matix 


