from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def sys(q,t):
    yi = q[0]
    xi = q[1]
    f0 = xi
    f1 = (g - ((cD/m)*(xi**2)))
    return [f0,f1]
    

# Constants
g =  9.80665
cD =  0.2028
m = 80

# ICS
x0 = 0
y0 = 0
ics = [y0,x0]

t = np.linspace(0,100,10000)
sol = integrate.odeint(sys,ics,t)
y = sol[:,0]
x = sol[:,1]

plt.figure(1)
plt.plot(t,y, label='Position')
plt.plot(t,x, label='Velocity')
plt.ylim(0,5000)
plt.legend(loc=0)
plt.plot()

print "Time to fall 5000m is between:"
t5000_b1 = np.min(np.where(y>5000))-1
t5000_b2 = np.min(np.where(y>5000))
print str((t5000_b1/100)) + " seconds; here y = " + str(y[t5000_b1]) 
print "and"
print str((t5000_b2/100)) + " seconds; here y = " + str(y[t5000_b2]) 

plt.figure(2)
plt.plot(t,x, label='Velocity')
plt.legend(loc=0)
plt.title('Skydiver velocity vs time')
plt.xlabel(r'$t$')
plt.ylabel(r'$v$')
plt.plot()

xmax = np.max(x)
print "maximum speed is " + str(xmax)

# and we are dooooon