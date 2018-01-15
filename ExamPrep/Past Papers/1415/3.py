from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# Define constants
k = 1.3807e-23

# Define integrand and range of points to integrate over
integrand = lambda x: (((x**4)*(np.exp(x)))/(((np.exp(x))-1)**2))
urange = np.arange(0.05,1.05,0.05)


def g(u):
    intres, interror = integrate.quad(integrand,0,(1/u),epsabs=1.49e-08)
    res = (u**3)*intres
    return res

gu_plot = np.zeros(len(urange))
for i in range(0,(len(urange))):
    gu_plot[i] = g(urange[i])
    
plt.figure(1)
plt.plot(urange,gu_plot)
plt.title(r'$g(u)$ vs $u$')
plt.xlabel(r'$u$')
plt.ylabel(r'$g(u)$')
plt.show()