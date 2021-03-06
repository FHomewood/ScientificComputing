import numpy as np
import polyFit
import scipy
from scipy import interpolate
import matplotlib.pyplot as plt

h=[0.0,1.525,3.050,4.575,6.1,7.625,9.15] #x values
den=[1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741] #y values
hrang=np.linspace(0,9.15,100)

print 'Using Polynomial Interpolation: ', '\n'

l_001=interpolate.barycentric_interpolate(h,den,(2,5)) #Using interpolate from scipy. Uses barycentric polynomial interpolation. Arguments: (x values, y values, points at which you wish to evaluate)

print 'At 2km the density of air will be ', l_001[0]

print 'At 5km the density of air will be ', l_001[1]

###
print '\n', 'Using Cubic Splines: ', '\n'

l_002=interpolate.interp1d(h,den,kind='cubic') #Interpolatioon from scipy. Uses cubic splines. Arguments: (x values, y values, order of splines)

print 'At 2km the density of air will be ', l_002(2) #Calls for interpolation to be evaluated at argument

print 'At 5km the density of air will be ', l_002(5)


###

print '\n', 'Using Least Squares Fit: ', '\n'

l=polyFit.polyFit(h,den,2) #Using polyFit module to generate a list of coefficients. Arguments: (x values, y values, degree of polynomial)

def l_003(x): #defining a function for the polynomial generated by polyFit
	l_003=l[0]+l[1]*x+l[2]*x**2
	return l_003

print 'At 2km the density of air will be ', l_003(2) #using function as defined above

print 'At 5km the density of air will be ', l_003(5)



###

denl_001=interpolate.barycentric_interpolate(h,den,hrang)
denl_002=l_002(hrang)
denl_003=l_003(hrang)

plt.figure(1)
plt.plot(hrang,denl_001,'r-',2,interpolate.barycentric_interpolate(h,den,2),'bo',5,interpolate.barycentric_interpolate(h,den,5),'bo')
plt.axis([0,10,0.2,1])
plt.xlabel('Height (km)')
plt.ylabel('Air Density')
plt.title('Barycentric Interpolation')
plt.show()

plt.figure(2)
plt.plot(hrang,denl_002,'r-',2,l_002(2),'bo',5,l_002(5),'bo')
plt.axis([0,10,0.2,1])
plt.xlabel('Height (km)')
plt.ylabel('Air Density')
plt.title('Cubic Splines')
plt.show()

plt.figure(3)
plt.plot(hrang,denl_003,'r-',2,l_003(2),'bo',5,l_003(5),'bo')
plt.axis([0,10,0.2,1])
plt.xlabel('Height (km)')
plt.ylabel('Air Density')
plt.title('Least Squares Fit')
plt.show()

plt.figure(4)
plt.plot(h,den,'ro')
plt.axis([0,10,0.2,1])
plt.xlabel('Height (km)')
plt.ylabel('Air Density')
plt.title('Original Data')
plt.show()
