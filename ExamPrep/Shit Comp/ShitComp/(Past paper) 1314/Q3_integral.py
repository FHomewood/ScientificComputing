from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# Define constants
i0 = 100.0
R = 0.5
t0 = 0.01

integrand = lambda t: R*(((i0)*np.exp(-t/t0)*(np.sin((2*t)/t0)))**2)

E, error = integrate.quad(integrand,0,np.inf)
print "E = " + str(E) + " with an error of " + str(error)