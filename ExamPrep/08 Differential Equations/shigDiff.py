import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
import run_kut4 as rk

e1=input('Please provide a value for epsilon: ') 
h=input('Please provide a step size: ')
ini1=[0.5,0.0]
tspace = np.linspace(0.0,10*np.pi,(10*np.pi)/h)#time conditions for odeint
tstart=0 #time start for RK
tstop=10*np.pi #time stop for RK

###Function used by RK method
def diff1(t,z): #order of arguments reversed to fit run_kut4
    x=z[0]
    y=z[1]
    diff1=np.zeros(2)
    diff1[0]=y
    diff1[1]=-x-e1*((x**2)-1)*y
    return diff1
###Function used by odeint
def diff2(z,t):
    x=z[0]
    y=z[1]
    diff2=np.zeros(2)
    diff2[0]=y
    diff2[1]=-x-e1*((x**2)-1)*y
    return diff2

R,K=rk.integrate(diff1,tstart,ini1,tstop,h) #Solves using Runge Kutta method, arguments: function, start of interval,initial conditions,end of interval,step size)
ODE=sp.odeint(diff2,ini1,tspace) #Solves using odeint, arguments: function, initial condiions, time interval.

plt.figure(1)
plt.plot(R, K[:,0])
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Motion of a van der Pol oscillator, as found using Runge-Kutta")

plt.figure(2)
plt.plot(K[:,0], K[:,1])
plt.axis('equal')
plt.xlabel("Displacement")
plt.ylabel("Velocity")
plt.title('Phase space of a van der Pol oscillator, as found using Runge-Kutta')

plt.figure(3)
plt.plot(tspace, ODE[:,0])
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Motion of a van der Pol oscillator, as found using odeint")

plt.figure(4)
plt.plot(ODE[:,0],ODE[:,1])
plt.axis('equal')
plt.xlabel("Displacement")
plt.ylabel("Velocity")
plt.title("Phase space of a van der Pol oscillator, as found using odeint")

plt.show()
