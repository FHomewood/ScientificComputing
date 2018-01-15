import numpy as np
from scipy import optimize #we'll need fsolve
import matplotlib.pyplot as plt

#######
####### [PART A]
#######
# Constants
c = 2.

# Equation
def f(x):
    eqn = (1-np.exp((-c*x))-x)
    return eqn
    
sol = optimize.fsolve(f,1.,xtol=1e-7) # 0.2 is an initial guess

print "Solution calculated as " + str('%e' %sol) + " with an error of less than 1e-7 for c = 2."




#######
####### [PART B]
#######
c_range = np.arange(0,3.01,0.01)

def x_filler(c_i):
    eq = lambda x : (1-np.exp((-c_i*x))-x)
    eq_sol = optimize.fsolve(eq,1.,xtol=1e-7)
    return eq_sol

x_plot = np.zeros(len(c_range))
for i in range(len(c_range)):
    x_plot[i] = x_filler(c_range[i])
    
plt.figure(1)
plt.plot(c_range,x_plot,label=r'$x(c)$')
plt.title(r'Graph of $x(c)$ vs $c$')
plt.legend(loc=0)
plt.xlabel(r'$c$')
plt.ylabel(r'$x(c)$')
plt.show()
