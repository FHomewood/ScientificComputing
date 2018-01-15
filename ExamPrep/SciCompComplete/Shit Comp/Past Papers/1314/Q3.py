from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt



# Define functions
def i_squared(x):
    q = (((i0)*np.exp(-x/t0)*(np.sin((2*x)/t0))))
    return (q**2)
    
integrand = lambda t: R*(((i0)*np.exp(-t/t0)*(np.sin((2*t)/t0)))**2)


# Define constants
i0 = 100.0
R = 0.5
t0 = 0.01



# Ranges and matrices for plots
t_range = np.linspace(0,1,100000)
i_squared_plot = np.zeros(len(t_range))

for n in range(len(t_range)):
    i_squared_plot[n] = i_squared((t_range[n]))
    
# Plot all dat guuud
plt.figure(1)
plt.semilogy(t_range,i_squared_plot,label=r'$[i(t)]^2$')

plt.title(r'$[i_t]^2$ vs $t$')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$[i(t)]^2$ (${A^2}$)')
plt.legend(loc=0)
plt.show()


# Integrate me, baby
E, error = integrate.quad(integrand,0,np.inf)
print "E = " + str(E) + " with an error of " + str(error)