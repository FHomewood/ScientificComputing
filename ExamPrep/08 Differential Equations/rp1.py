import scipy.integrate as scin
import numpy as np
import matplotlib.pyplot as pl


g=9.80665
Cd=0.2028
m=80
ics = ([0,0])
t = np.linspace(0,100,500) #creates an array t, integration range from 0 and inclusive of 100 since its linspace, increment of 500

def deriv(x,t):
	F = np.zeros(2) #creates an array F, with length 2 thats filled with 0's
	F[0]=x[1] #dy/dt = y'
	F[1]=g-((Cd/m)*((x[1])**2)) #d2y/dt2 = g-((cd/m) * (y'^2))
	return F
	
sol_1 = scin.odeint(deriv,ics,t) #odeint outputs array --> [y solution, dy/dt solution]

x_1 = sol_1[:,0] #(every value in) the y solution column 
y_1 = sol_1[:,1] #(every value in) the dy/dt solution column
print sol_1
#print x_1
#print y_1 

pl.figure(1)
pl.plot(t,x_1,'r-')
pl.xlabel('Time(s)')
pl.ylabel('y')
pl.show()

pl.figure(2)
pl.plot(t,y_1,'r-')
pl.xlabel('Time(s)')
pl.ylabel('y')
pl.show()


