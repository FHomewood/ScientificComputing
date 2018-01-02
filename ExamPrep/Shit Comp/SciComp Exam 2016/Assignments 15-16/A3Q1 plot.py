# Question 1 - Assignment 3 - due 07/12/2015

import math as m
from run_kut4 import *
from printSoln import *
import numpy as np
from pylab import *

# part a

# say T = theta, O = capital omega, w = lower case omega, B = beta, j = gamma 
# d^2T/dt^2 = -(g/L)*sin(T)+C*cos(T)sin(Ot)
# = -w^2 * sin(T) + j*w*cos(T)sin(Bwt)
# = -w^2 * sin(T) + j*w*cos(T)sin(Bx)
# d^2T/dx^2 = -sin(T) + j*cos(T)sin(Bx)

#part b

g = 9.81#m/s^2
L = 0.10#cm
C = 2.0#s^-2
O1 = 5.0#s^-1
w = m.sqrt(g/L)
j = C/(w**2)
B1 = O1/w

def f1(x,T):
    f1 = np.array([0.0,0.0])
    f1[0] = T[1]
    f1[1] = -m.sin(T[0])+j*m.cos(T[0])*m.sin(B1*x)
    return f1

# initial conditions
initial = np.array([0.0,0.0])
tStop = 40*w
h = 0.1
freq = 1
tInitial=0.0

X1,Y1 = integrate(f1,tInitial,initial,tStop,h)
#printSoln(X1,Y1,freq)

figure(1)
plot(X1,Y1[:,0]) # first term of array
show()

#part c

O2 = 9.81
B2 = O2/w

def f2(x,T):
    f2 = np.array([0.0,0.0])
    f2[0] = T[1]
    f2[1] = -m.sin(T[0])+j*m.cos(T[0])*m.sin(B2*x)
    return f2
      
X2,Y2 = integrate(f2,tInitial,initial,tStop,h)
#printSoln(X2,Y2,freq)

figure(2)
plot(X2,Y2[:,0]) # first term of array
show()








