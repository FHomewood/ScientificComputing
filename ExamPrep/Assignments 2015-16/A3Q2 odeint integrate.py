# Question 2 -Assignment 3 -  due in 07/12/2015

import scipy
from scipy import integrate
import numpy as np
import pylab as pl

a = 5.0
b = 0.9
c1 = 8.2 #calling this c1 because we will use a different c value later and call that c2

def F(y,t):
    F=np.zeros(3)
    F[0]=-a*(y[0]-y[1])
    F[1]=c1*y[0]-y[1]-y[0]*y[2]
    F[2]=-b*y[2]+y[0]*y[1]
    return F
    
x_a = 0.0 # beginning of integration 
x_b = 100.0 # end ofintegration
y_initial = np.array([0.0,1.0,2.0])

x=np.linspace(0.0,x_b,50000)
I_1=integrate.odeint(F,y_initial,x)

Y_1=I_1[:,0] # using first term of array

pl.figure(1)
pl.plot(x,Y_1)
pl.title('Plotting u vs t where c = 8.2')
pl.xlabel('Time(s)')
pl.ylabel('Function u(t)')
pl.show(1)


c2 = 8.3

def G(y,t):
    G=np.zeros(3)
    G[0]=-a*(y[0]-y[1])
    G[1]=c2*y[0]-y[1]-y[0]*y[2]
    G[2]=-b*y[2]+y[0]*y[1]
    return G

I_2=integrate.odeint(G,y_initial,x)

Y_2=I_2[:,0] # using first term of array

pl.figure(2)
pl.plot(x,Y_2)
pl.title('Plotting u vs t where c = 8.3')
pl.xlabel('Time(s)')
pl.ylabel('Function u(t)')
pl.show(2)

#Lorentz trajectory

Y_3=I_2[:,1] 

pl.figure(3)
pl.plot(Y_2,Y_3)
pl.title('Lorentz Trajectory')
pl.show(3)

