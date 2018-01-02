
'''arange'''
# an arange returns evenly spaced values (where you give the space size) within a given interval and is part of the numpy package

#numpy.arange(start,stop,step)

#where start is a number that you want to start with, the interval includes this value 
#stop is the end of the interval the interval does not include this number
#step is the spacing between values  

#example
import numpy as numpy 

a=numpy.arange(1,11,1)
print a

#this gives [1,2,3,4,5,6,7,8,9,10]


'''linspace'''

#linspace returns evenly spaced values (where you give the number of spaces) within a given interval and is part of the numpy package

#numpy.linspace(start,stop,num=x)

#where start is a number that you want to start with, the interval includes this value 
#stop is the end of the interval the interval does include this number (unless you add endpoint=False,)
#num=x is the number of spaces you want and the interval will be split evenly amoung these spaces

b=numpy.linspace(0,10,num=5)
print b
