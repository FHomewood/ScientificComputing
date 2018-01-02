from scipy import *
from scipy import interpolate
from scipy.interpolate import barycentric_interpolate as bi
import numpy as np
import pylab as pl #where we get graph function
from scipy.optimize import curve_fit
from polyFit import *
from scipy import polyfit 

h=np.array([0.0,1.525,30.050,4.575,6.10,7.625,9.150])
p=np.array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])

z=np.arange(0,9.3,0.1) #gives points to evaluate a polynomial fit going through p and h
a=bi(h,p,2) #evaluates a polynomial going through the  points p(h) gives p at h=2
print a

z=np.arange(0,9.3,0.1)
b=bi(h,p,4)
print b

z=np.arange(0,9.2,0.1)
c=bi(h,p,8)
print c

print 'part b'
f=interpolate.interp1d(h,p,kind='cubic') #creates a cubic function that fits the graph 

d=f(2) #uses interpolation function 
print 'Density at 2km using cubic spline interpolation'
print d

e=f(4) #uses interpolation function 
print 'Density at 4km using cubic spline interpolation'
print e

f=f(8) #uses interpolation function 
print 'Density at 8km using cubic spline interpolation'
print f

print 'part c- getting errors'
actualvalue=0.67
e1= (b-actualvalue)/actualvalue 
print e1

actualvalue=0.67
e2= (e-actualvalue)/actualvalue 
print e2

