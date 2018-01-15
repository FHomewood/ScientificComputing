import numpy as np
import matplotlib.pyplot as plt
import ridder as ri
import newtonRaphson as nR
from scipy.optimize import fsolve

# part a
# constants:

u=2510 #[m/s], velocity of exhaust relative to the rocket
Mo=2.8e+6 #[kg], mass of rocket at liftoff
dmdt=13.3e+3 #[kg/s], rate of fuel consumption
g=9.81 #[m/s^2], gravitational acceleration

# speed of Saturn V rocket:

t = np.linspace(0,200,500)
def v(p):
	return (u*(np.log(Mo/(Mo-(dmdt*p)))))-(g*p)-335  # this equation has a -335 term because we want to find out when v=335 so we moved the 335 term over


plt.plot(t,v(t))
plt.title('Velocity of rocket over time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

# assume initial t = 60 -- plot tells us v=335 is somewhere between 60 and 80

def dvdt(p):
    return (((dmdt*u)/(Mo-(dmdt*p))-g))

risol = ri.ridder(v,60,80)


print "The Ridder method tells us that the rocket will reach the speed of sound at time =",round(risol,2),"s."

nRsol = nR.newtonRaphson(v,dvdt,60,80,tol=1e-09)

print "The Newton Raphson method tells us that the rocket will reach the speed of sound at time =",round(nRsol,2),"s."
 
fs = fsolve(v,0.1)

print "The scipy.optimize.fsolve method tells us that the rocket will reach the speed of sound at time =",round(fs,2),"s."
 
# answer b in writeup!

