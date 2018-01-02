#Problem sheet 1

print 'Problem Sheet 1'

from gaussElimin import *
import numpy as np
from scipy import linalg

print 'Q1a'
#4v1-v2-v3-v4=v+
#-v1+3v2+0v3-v4=0
#-v1+0v2+3v3-v4=v+
#-v1-v2-v3+4v4=0
print '4v1-v2-v3-v4=v+'
print '-v1+3v2+0v3-v4=0'
print '-v1+0v2+3v3-v4=v+'
print '-v1-v2-v3+4v4=0'

print 'Q1b'
x=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]], dtype = float)
print x
y=np.array([[5.0],[0.0],[5.0],[0.0]], dtype = float) #creates a matrix
print y

z=gaussElimin(x,y)
print z

print 'Q1c - Using LuDecomposition of our matrix'

from LUdecomp import *

P,L,U=linalg.lu(x) #in this case P is just an identitiy matrix because its just 1

print 'The original matrix'
print (x)
print ''
print 'The L matrix'
print (L)
print ''
print 'The U matrix'
print (U)
print ''

print 'Q1D'

x1=np.array([[5.0],[0.0],[5.0],[0.0]]) #vector b when vo is 0
x2=np.array([[5.0],[1.0],[5.0],[1.0]]) #vector b when v0 is now 1

print 'original vector b when v0=0'
print x1
print "Below are the vectors b where instead of V=0 V0=1:"
print x2 

x=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]])

P,L,U=linalg.lu(x) 
k=gaussElimin(L,x2)#solves Lz=b where b is new vector and L is from part c, which redefines b when you use gaussElimin solving as Ux=z it puts in your new b in this case x2 and spits out your original answer
J=gaussElimin(U,k)
M=gaussElimin(L,x1)
N=gaussElimin(U,M)
print 'when v0=1'
print J #Solutions match
print 'When v0=0'
print M #Solutions match from before with part b
