
print 'Problem Sheet 3'
from scipy import *
from scipy import interpolate
from scipy.interpolate import barycentric_interpolate as bi
import numpy as np
import pylab as pl #where we get graph function
from scipy.optimize import curve_fit
from polyFit import *
from scipy import polyfit 

print 'Q3a'
h=np.array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
p=np.array([1.0,0.8617, 0.7385,0.6292,0.5328,0.4481,0.3741])

z=np.arange(0,9.2,0.1) #gives points to evaluate a polynomial fit going through p and h

a= bi(h, p, 2) #evaluates a polynomial going through the  points p(h) gives p at h=2
print 'Density at 2km using polynomial interpolation'
print a

b= bi(h,p,5) #evaluates a polynomial going through the points p(h) and gives p at h=5
print 'Density at 5km using polynomial interpolation'
print b

print 'Q3b'
 

f=interpolate.interp1d(h,p,kind='cubic') #creates a cubic function that fits the graph 

c=f(2) #uses interpolation function 
print 'Density at 2km using cubic spline interpolation'
print c

d=f(5) #uses interpolation function 
print 'Density at 5km using cubic spline interpolation'
print d

print 'Q3c'

def func(m, a, b, c):
    return a*m**2+b*m+c

m= np.linspace(0,10,500)
popt, pcov=curve_fit(func,h,p) #popt is array of a b and c which is arbitrary constants in themselves
quad2=popt[0]*2**2+popt[1]*2+popt[2]
quad5=popt[0]*5**2+popt[1]*5+popt[2]


print 'Density at 2km using quadratic spline interpolation'
print quad2

print 'Density at 5km using quadratic spline interpolation'
print quad5

print 'Q3d'

pl.figure(1)
pl.plot(h, p, 'o',label="original data")
pl.plot(h,p,"-")
pl.plot(2, a,'ro', label='polynomial')
pl.plot(5, b,'ro')
pl.plot(2, c,'g^',label='cubic splines')
pl.plot(5, d,'g^')
pl.plot(2,quad2, "bs", label="Quadratic Least squares fit")
pl.plot(5, quad5,'bs')
pl.xlabel("Height (km)")
pl.ylabel("Density p")
pl.title("Comparison of interpolations")
pl.legend(loc="upper right")
pl.legend()
pl.show()