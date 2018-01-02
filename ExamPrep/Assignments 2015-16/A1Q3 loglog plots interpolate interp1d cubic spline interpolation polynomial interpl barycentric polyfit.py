# ***Question 3***

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from polyFit import *
from swap import *
from error import *


Re = np.array([0.2,2,20,200,2000,20000]) # the Re values given to us, on x axis
cD = np.array([103,13.9,2.72,0.800,0.401,0.433]) # the cD values given to us, on y axis

plt.figure(1)
plt.loglog(Re,cD) # plotting Re and cD on a log-log scale


f = interpolate.interp1d(Re,cD,kind='cubic') # using cubic spline to interpolate Re vs. cD plot

newRe = np.array([5,50,500,5000]) # an array of the values at which we want Re
newcD = f(newRe) # making the y values of the cubic function using the new Re values we are using

plt.loglog(Re,cD,'o',newRe,newcD,'-') # first plot is circles, new plot is dashes
plt.title('Re vs cD on loglog scale')
plt.xlabel('logRe')
plt.ylabel('logcD')

print "\n\n Cubic spline interpolation results:" # printing the numerical value of the function at the given new Re values when using the cubic spline interpolation

print "Value at Re = 5: " + (str(f(5)))
print "Value at Re = 50: " + (str(f(50)))
print "Value at Re = 500: " + (str(f(500)))
print "Value at Re = 5000: " + (str(f(5000)))


print "\n\n Polynomial interpolation results:" # printing the numerical value of the function at the given new Re values when using the polynomial/barycentric interpolation


print "Value at Re = 5: " + (str(interpolate.barycentric_interpolate(Re,cD,5)))
print "Value at Re = 50: " + (str(interpolate.barycentric_interpolate(Re,cD,50)))
print "Value at Re = 500: " + (str(interpolate.barycentric_interpolate(Re,cD,500)))
print "Value at Re = 5000: " + (str(interpolate.barycentric_interpolate(Re,cD,5000)))

lRe=np.log(Re)
lcD=np.log(cD)

p = polyFit(lRe,lcD,3) # this gives the coefficients of the polynomial on the logged values of Re and cD
print "The polynomial interpolation results are: "
print p



x = np.arange(np.log(Re[0]),np.log(Re[5]),0.1) # making a range of the relevant Re log values to use with our polyfit
y = p[0]+x*(p[1])+(x**2)*(p[2])+(x**3)*(p[3]) # the polyfit

plt.loglog(np.e**x, np.e**y, '+') # putting them back into exponentials

plt.show(1)

plt.figure(2)
plt.plot(Re,cD, '-')
plt.title('Re vs cD (not loglog)')
plt.xlabel('Re')
plt.ylabel('cD')
plt.axis([-500,20500,-10,110])
plt.show(2)









