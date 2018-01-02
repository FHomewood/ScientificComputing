#polyFit (least squares fit) (example assesment 1 Q3 part c)
#creates a least squares polynomial fit 

'''
c = polyFit(xData,yData,m).
    Returns coefficients of the polynomial
 
P=polyFit(x,y,m) #uses least squares fit to create a polynomial P of m degrees
yu=P[0]+P[1]*(xu)+P[2]*(xu)**2  #can use coefficients of the polynomial to find yu using P[n]*xu**n
'''
#gives a polynomial of degree n as you specify when using P[n]*xu**n

#example (assesment 1 Q3 part c)

from polyFit import * #where polyFit is a file on study direct
import numpy as np

h=np.array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
p=np.array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])

P=polyFit(h,p,2) #uses least squares fit to create a quadratic polynomial 
P1=P[0]+P[1]*2+P[2]*2**2   #a[n]*2**n 
P2=P[0]+P[1]*5+P[2]*5**2   #a[n]*5**n

print 'density at 2km using quadratic least squares fit='
print P1

print 'density at 5km using quadratic least squares fit='
print P2

