import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as pl

i0=100
R=0.5
t0=0.01

def I(t):
	return (i0*(np.exp(-t/t0)*np.sin((2*t)/t0)))**2

t=np.linspace(0,1,1000)
i = np.zeros(1000)
for x in range(0, 1000):
	i[x] = I(t[x])

pl.figure(1)
pl.semilogy(t,i,'r-') #semilogy makes y axis logarithmic (semilogx for x axis?)
pl.xlabel('Time(s)')
pl.ylabel('I[t]^2')
pl.show()

E=quad(I,0,np.inf) #quad outputs an array --> [answer, absolute error]
Energy=(R*((E[0])))
print Energy 


