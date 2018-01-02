#Problem sheet 2

from numpy import array
from gaussPivot import *
from gaussElimin import *


a= array([[2.0,-1.0,0.0,0.0], [0.0,0.0,-1.0,1.0], [0.0,-1.0,2.0,-1.0],
[-1.0,2.0,-1.0,1.0]])
b= array([1.0,0.0,0.0,1.0]) #builds the matrix a and b

print 'original matrix'
print a
print 'matrix b'
print b

x=gaussPivot(a,b) #pivots the matrix 
print 'pivot'
print x
print 'part 2'
a= array([[2.0,-1.0,0.0,0.0], [0.0,0.0,-1.0,1.0], [0.0,-1.0,2.0,-1.0],
[-1.0,2.0,-1.0,1.0]])
b= array([1.0,0.0,0.0,1.0]) #builds the matrix a and b

y=gaussElimin(a,b) #does not give an answer, more a nan error

print x
print y


