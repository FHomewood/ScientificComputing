print 'Q4b'
import numpy as np
import scipy.integrate

def W(x):
   return (x**3/(np.exp(x)-1))
I=scipy.integrate.quad(W,0,np.inf)
print I
print "Work=",I[0]
print "error=",I[1]
#constants I need to times the integral by:
Kb=float (1.380648813*10**(-23))
h=float(1.05457172647*10**(-34))
c=float(299792458)


w=float(I[0]*(Kb**4)/(4.0*(np.pi)**2*c**2*h**3))
print "Work equals",w #THIS IS EQUAL TO STEFAN BOLTZMAN CONSTANT YAY
