"""
I already know this doesn't work. I didn't have time to fix it.
"""

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


# Define constants
c = 0.005
g = 9.81

# Angles
a_r10 = np.deg2rad(10)
a_r20 = np.deg2rad(20)
a_r80 = np.deg2rad(80)

alpha = a_r10

# ICS
x0 = 0
y0 = 0
a0 = 1000*(np.cos(alpha))
b0 = 1000*(np.sin(alpha))
ics = [x0,y0,a0,b0]


# Set up range
t_range = np.linspace(0,30,3000)

# Define function to integrate
def sys(q,t):
    xi = q[0]
    ai = q[1]
    yi = q[3]
    bi = q[2]
    f0 = ai #dx = a
    f2 = bi #dy = b
    f1 = (-c*(ai)*(np.sqrt((ai**2)+(bi**2))))
    f3 = (-c*(bi)*(np.sqrt((ai**2)+(bi**2))))-g
    return [f0,f1,f2,f3]
    

# Define alpha and get answer
alpha = a_r10
x_10, y_10 = integrate.odeint(sys,ics,t_range)

plt.figure(1)
plt.plot(x_10,y_10)
plt.show()