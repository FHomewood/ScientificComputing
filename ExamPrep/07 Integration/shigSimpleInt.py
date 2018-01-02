#This code finds an estimate for the Stefan Boltzmann (SB) constant using numerical integration.

import numpy as np
from scipy.integrate import quad


#Required constants defined below.
K=1.3806488*10**-23
h=1.054571726*10**-34
c=299792458
SB=5.670373*10**-8

def I(x):
    return (x**3)/(np.exp(x)-1) #expression to be integrated.

W=quad(I,0,710) #This function carries out the integration, arguments(integrand, lower limit, upper limit).
print W
sigma=((K**4)/(4*(np.pi)**2*c**2*h**3))*W[0] #Finds an estimate of SB constant.

error=((SB-sigma)/SB)*100 #finds the error on the calculation as a percentage of the true value.

print 'Result of integration=', W[0]
print 'Stefan Boltzmann Constant=',sigma,'Wm^-2K^-4'
print 'The relative error on this calculation is ',error,'%'
