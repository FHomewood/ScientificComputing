#LU Decompositon 
from scipy import linalg
 
#from Q1.py assesment 1 part C
P, L, U = linalg.lu(A)
#where L is the lower triangular matrix, U is the upper triangular matrix and P is the permutaion matrix and A is your matrix you are wishing to decompose 

#to solve the syatem Ax=b using the L and U matrices (from Q1.py assesment 1 part d) you have made use 
from gaussElimin import *

xL=gaussElimin(L,b) #gaussElimin changes b so no need to recombine xL and x

x=gaussElimin(U,b) #where x is shown as a vector and is the final answer or 'x' from Ax=b

print dot(dot(L,P),U)#checks answer by geting back to origonal matix 

