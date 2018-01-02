"""
Q1: Solving an anharmonic oscillator
Utilises NumPy's odeint()
Compares to a standard oscillator at the end.
"""

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# A
# define function to integrate
def deriv(q,t):
    xi = q[0]
    yi = q[1]
    deriv0 = yi
    deriv1 = (-(omega**2)*(xi**3))
    return [deriv0, deriv1]

omega = 1.0
# inital conditions, must be a vector to supply to odeint
x0 = 1.0
y0 = 0.0
ics = [x0,y0]
t = np.linspace(0,20.0,2000) #integration range

# get sol
sol_1 = integrate.odeint(deriv,ics,t) #returns an array
x_1 = sol_1[:,0]
y_1 = sol_1[:,1]

plt.figure(1)
plt.plot(t,x_1, color='#1C71FF')
plt.xlabel(r'$t$, time')
plt.xlim(0,20)
plt.ylabel(r'$x$, position')
plt.ylim(-1.1,1.1)
plt.axhline(y=0,color='k')
plt.title(r'Anharmonic oscillator: position vs. time [$x(0)$ = 1]')
plt.show()

# add some horizontal lines so we can check the max position
plt.figure(2)
plt.plot(t,x_1,color='#1C71FF')
plt.xlabel(r'$t$, time')
plt.xlim(0,20)
plt.ylabel(r'$x$, position')
plt.ylim(-1.1,1.1)
plt.axhline(y=0,color='k')
plt.axhline(y=-1,color='r')
plt.axhline(y=1,color='r')
plt.title(r'Anharmonic oscillator: position vs. time [$x(0)$ = 1]')
plt.show()


# do again for x0 = 10.0
x0 = 10.0
ics = [x0,y0] #have to restate this otherwise the tuple won't update
sol_10 = integrate.odeint(deriv,ics,t)
x_10 = sol_10[:,0]
y_10 = sol_10[:,1]

plt.figure(3)
plt.plot(t,x_10,color='#84FF84')
plt.xlabel(r'$t$, time')
plt.xlim(0,20)
plt.ylabel(r'$x$, position')
plt.title(r'Anharmonic oscillator: position vs. time [$x(0)$ = 10]')
plt.axhline(y=0,color='k')
plt.show()


# what if x0 = 2?
x0 = 2.0
ics = [x0,y0]
sol_2 = integrate.odeint(deriv,ics,t)
x_2 = sol_2[:,0]
y_2 = sol_2[:,1]


# put all solutions on the same graph
plt.figure(4)
plt.plot(t,x_1,label=r'$x(0)$ = 1', color='#1C71FF', linewidth=2.0)
plt.plot(t,x_2,label=r'$x(0)$ = 2', color='#8600D3', linewidth=2.0)
plt.plot(t,x_10,label=r'$x(0)$ = 10', color='#84FF84', linewidth=2.0)
plt.xlabel(r'$t$, time')
plt.xlim(0,20)
plt.ylabel(r'$x$, position')
plt.title('Anharmonic oscillator: position vs. time')
plt.axhline(y=0,color='k')
plt.legend(loc=0)
plt.show()


# phase-space plot, dx/dt vs x, i.e. y vs x
plt.figure(5)
plt.plot(x_1,y_1,label=r'$x(0)$ = 1', color='#1C71FF')
plt.xlabel(r'$x$, position')
plt.ylabel(r'$\frac{dx}{dt}$, velocity')
plt.axis('equal')
plt.title(r'Phase-space plot: $\frac{dx}{dt}$ vs. $x$ for anharmonic oscillator')
plt.legend(loc=0)
plt.show()


# all of them!
plt.figure(6)
plt.plot(x_1,y_1,label=r'$x(0)$ = 1', color='#1C71FF')
plt.plot(x_2,y_2,label=r'$x(0)$ = 2', color='#8600D3')
plt.plot(x_10,y_10,label=r'$x(0)$ = 10', color='#84FF84')
plt.xlabel(r'$x$, position')
plt.ylabel(r'$\frac{dx}{dt}$, velocity')
plt.axis('equal')
plt.title(r'Phase-space plot: $\frac{dx}{dt}$ vs. $x$ for anharmonic oscillator')
plt.legend(loc=0)
# block below is to put in horizontal lines, for clarity. turned off normally
"""
plt.axhline(y=2,color='k')
plt.axhline(y=-2,color='k')
plt.axhline(y=1,color='k')
plt.axhline(y=-1,color='k')
"""
plt.show()




# C
# what of a 'normal' harmonic oscillator?
def normalOsc(q,t):
    xi = q[0]
    yi = q[1]
    deriv0_n = yi
    deriv1_n = (-(omega**2)*xi)
    return [deriv0_n, deriv1_n]

# assume all other parameters but x0 are constant
x0 = 1.0
ics = [x0,y0]
sol_n1 = integrate.odeint(normalOsc,ics,t)
x_n1 = sol_n1[:,0]
y_n1 = sol_n1[:,1]

x0 = 10.0
ics = [x0,y0]
sol_n10 = integrate.odeint(normalOsc,ics,t)
x_n10 = sol_n10[:,0]
y_n10 = sol_n10[:,1]

# plot
plt.figure(7)
plt.plot(t,x_n1,label=r'$x(0)$ = 1', color='b')
plt.plot(t,x_n10,label=r'$x(0)$ = 10', color='g')
plt.xlabel(r'$t$, time')
plt.xlim(0,20)
plt.ylabel(r'$x$, position')
plt.title('Harmonic oscillator: position vs. time')
plt.axhline(y=0,color='k')
plt.legend(loc=0)
plt.show()

# phase plot
plt.figure(8)
plt.plot(x_n1,y_n1,label=r'$x(0)$ = 1', color='b')
plt.plot(x_n10,y_n10,label=r'$x(0)$ = 10', color='g')
plt.xlabel(r'$x$, position')
plt.ylabel(r'$\frac{dx}{dt}$, velocity')
plt.axis('equal')
plt.title(r'Phase-space plot: $\frac{dx}{dt}$ vs. $x$ for a harmonic oscillator')
plt.legend(loc=0)
"""
plt.axhline(y=10,color='k')
plt.axhline(y=-10,color='k')
plt.axhline(y=1,color='k')
plt.axhline(y=-1,color='k')
"""
plt.show()

# phase plot with ALL of them
plt.figure(9)
plt.plot(x_n1,y_n1,label=r'$x(0)$ = 1, harmonic', color='b')
plt.plot(x_1,y_1,label=r'$x(0)$ = 1, anharmonic', color='#1C71FF')
plt.plot(x_n10,y_n10,label=r'$x(0)$ = 10, harmonic', color='g')
plt.plot(x_10,y_10,label=r'$x(0)$ = 10, anharmonic', color='#84FF84')
plt.xlabel(r'$x$, position')
plt.ylabel(r'$\frac{dx}{dt}$, velocity')
plt.ylim(-70,70)
plt.axis('equal')
plt.title(r'Phase-space plot: $\frac{dx}{dt}$ vs. $x$')
plt.legend(loc=0)
plt.show()