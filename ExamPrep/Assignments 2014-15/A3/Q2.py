"""
A3, Q2
Solving van der Pol oscillator using both Runge-Kutta and odeint,
taking odeint's result to be the true value
"""
import scipy.integrate as sp_int
import numpy as np
import matplotlib.pyplot as plt
from run_kut4 import *



# define constant
epsilon = 10.0
# inital conditions
x0 = 0.5
y0 = 0.0
ics = [x0,y0] #vector of initial conditions

# define the function as it demands
def f(x,y):
    f = np.zeros(2)
    f[0] = y[1] #f0 == dx, y[0] = x, y[1] = y
    f[1] = (-y[0])-((epsilon*((y[0]**2)-1))*y[1]) #f1 == dy
    return f


# integration parameters. These won't change
x_start = 0.0 
x_stop = (10.0*np.pi)
# integration itself
X_002,Y_002 = integrate(f,x_start,ics,x_stop,0.02)

# plot
plt.figure(1)
plt.plot(X_002,Y_002[:,0],label=r'$h$ = 0.02',color='b')
plt.xlabel(r'time, $t$')
plt.ylabel(r'position, $x$')
plt.title(r'Position vs. time for step-size $h$ = 0.02')
plt.legend(loc=0)
plt.xlim(0,(10*np.pi))
plt.show()



# again for h=0.05
X_005,Y_005 = integrate(f,x_start,ics,x_stop,0.05)

plt.figure(2)
plt.plot(X_005,Y_005[:,0],label=r'$h$ = 0.05',color='g')
plt.xlabel(r'time, $t$')
plt.ylabel(r'position, $x$')
plt.title(r'Position vs. time for step-size $h$ = 0.05')
plt.xlim(0,(10*np.pi))
plt.legend(loc=0)
plt.show()



# again for h=0.1
X_01,Y_01 = integrate(f,x_start,ics,x_stop,0.1)

plt.figure(3)
plt.plot(X_01,Y_01[:,0],label=r'$h$ = 0.1', color='r')
plt.xlabel(r'time, $t$')
plt.ylabel(r'position, $x$')
plt.title(r'Position vs. time for step-size $h$ = 0.1')
plt.legend(loc=0)
#plt.ylim(-2.1,2.1)
plt.xlim(0,(10*np.pi))
plt.show()




# define equations for odeint
def odeint_f(q,t):
    xi = q[0]
    yi = q[1]
    f0 = yi
    f1 = (-xi)-((epsilon*((xi**2)-1))*yi)
    return [f0,f1]

# range to solve for
t = np.linspace(0,(10*np.pi), 100000) #make this huge to get pretty curves
# integrate using odeint
odeint_sol_10 = sp_int.odeint(odeint_f,ics,t)
x_ois_10 = odeint_sol_10[:,0]
y_ois_10 = odeint_sol_10[:,1]


# plot this solution
plt.figure(4)
plt.plot(t,x_ois_10, label='odeint', color='k')
plt.xlabel(r'time, $t$')
plt.ylabel(r'position, $x$')
plt.title(r'Position vs. time, using odeint')
plt.xlim(0,(10*np.pi))
plt.show()


# plot all four
plt.figure(5)
plt.plot(X_01,Y_01[:,0], label=r'RK: $h$ = 0.1', color='r') ##this blows up
plt.plot(X_005,Y_005[:,0], label=r'RK: $h$ = 0.05', color='g')
plt.plot(X_002,Y_002[:,0], label=r'RK: $h$ = 0.02', color='b')
plt.plot(t,x_ois_10, label='odeint', color='k')
plt.xlabel(r'time, $t$')
plt.ylabel(r'position, $x$')
plt.title('Position vs. time')
plt.legend(loc=0)
plt.xlim(0,(10*np.pi))
plt.ylim(-2.1,2.1)
plt.show()




# Errors.
# Both arrays need to be of equal size.
# Generate new true value arrays to match the size of the rk arrays

def trange(x):
    z = np.linspace(0,10*np.pi,len(x[:,0]))
    return z

truev_002 = sp_int.odeint(odeint_f,ics,trange(Y_002))
truev_005 = sp_int.odeint(odeint_f,ics,trange(Y_005))
truev_01 = sp_int.odeint(odeint_f,ics,trange(Y_01))

er_rk_002 = np.abs((truev_002[:,0]) - (Y_002[:,0]))
er_rk_005 = np.abs((truev_005[:,0]) - (Y_005[:,0]))
er_rk_01 = np.abs((truev_01[:,0]) - (Y_01[:,0]))

plt.figure(6)
plt.semilogy(trange(Y_002),er_rk_002, label=r'Error for RK sol with $h$ = 0.02')
plt.semilogy(trange(Y_005),er_rk_005, label=r'Error for RK sol with $h$ = 0.05')
plt.semilogy(trange(Y_01),er_rk_01, label=r'Error for RK sol with $h$ = 0.1')
plt.xlim(0,10*np.pi)
plt.title(r'Graph of log of absolute errors vs. $t$')
plt.xlabel(r'$t$, time')
plt.ylabel(r'semilog($\sigma$), absolute error')
plt.legend(loc=0)
plt.show()

plt.figure(7)
plt.semilogy(trange(Y_002),er_rk_002, label=r'Error for RK sol with $h$ = 0.02')
plt.semilogy(trange(Y_005),er_rk_005, label=r'Error for RK sol with $h$ = 0.05')
plt.xlim(0,10*np.pi)
plt.title(r'Graph of log of absolute errors vs. $t$')
plt.xlabel(r'$t$, time')
plt.ylabel(r'semilog($\sigma$), absolute error')
plt.legend(loc=0)
plt.show()



# C
# get epsilon = 4 sol
epsilon = 4.0
odeint_sol_4 = sp_int.odeint(odeint_f,ics,t)
x_ois_4 = odeint_sol_4[:,0]
y_ois_4 = odeint_sol_4[:,1]

# do again for epsilon = 1
epsilon = 1.0
odeint_sol_1 = sp_int.odeint(odeint_f,ics,t)
x_ois_1 = odeint_sol_1[:,0]
y_ois_1 = odeint_sol_1[:,1]

plt.figure(8)
plt.plot(x_ois_1,y_ois_1, label=r'$\epsilon$ = 1', color='b')
plt.plot(x_ois_4,y_ois_4, label=r'$\epsilon$ = 4', color='g')
plt.plot(x_ois_10,y_ois_10, label=r'$\epsilon$ = 10', color='r')
plt.axis('equal')
plt.title(r'Phase-space plot, $\frac{dx}{dt}$ vs. $x$')
plt.xlabel(r'$x$, position')
plt.ylabel(r'$\frac{dx}{dt}$, velocity')
plt.legend(loc=0)
plt.show()