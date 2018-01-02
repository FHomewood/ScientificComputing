import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import romberg


# part a

x = np.linspace(0,5,100)
 
Y1 = (x**(1))*(np.exp(-x)) # a = 2
Y2 = (x**(2))*(np.exp(-x)) # a = 3
Y3 = (x**(3))*(np.exp(-x)) # a = 4

plt.plot(x,Y1,'r--',label='a = 2') # first line where a = 2 is red dashes
plt.plot(x,Y2,'b--',label='a = 3') # second line where a = 3 is blue dashes
plt.plot(x,Y3,'g--',label='a = 4') # third line where a = 4 is green dashes
plt.legend(loc=0) # adding a legend
plt.title('Gamma function with varying values of a')
plt.xlabel('x')
plt.ylabel('Gamma function Y')
plt.show() 


# part b

# gamma function integrand (denoted as y for this derivation):

# y = x^(a-1) * e^(-x) where a = real constant
# y' = dy/dx = d/dx (u*v) 
# when u = x^(a-1) and u' = (a-1)*x^(a-2)
# and v = e^(-x) and v' = -e^(-x)

# d/dx (u*v) = u'v+uv'

# u'v+uv' = [e^(-x)]*[(a-1)*x^(a-2)]+[x^(a-1)]*[-e^(-x)]
# = [e^(-x)]*[(a-1)*x^(a-2)]-[x^(a-1)]*[e^(-x)]
# = [e^(-x)]*[(a-1)*x^(a-2)-x^(a-1)]

# plug in x = a-1

# u'v+uv' = [e^(1-a)]*[(a-1)*(a-1)^(a-2)-(a-1)^(a-1)]
# u'v+uv' = [e^(1-a)]*[(a-1)^(a-1)-(a-1)^(a-1)] = 0

# derivative of a f(x) equals zero when x = stationary point
# so, x = a-1 gives stationary point (maximum) 

# part c

def Y(x): # defining gamma quation
    return (x**(0.5))*(np.exp(-x)) #  here, a = 3/2

print "The value of the Gamma function with its error is",quad(Y, 0, np.inf),"at a = 3/2 when we use the built in sci.integrate.quad module. This value is supposed to be around 1/2*(sqrt(pi) which is ~0.886 so this value is good."

print "The value of the Gamma function  is",romberg(Y,0,1e+1),"at a = 3/2 when we use the Romberg method. This value is also around the accepted value of ~0.886 so this value is also good."