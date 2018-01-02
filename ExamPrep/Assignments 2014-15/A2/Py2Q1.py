print 'Question 1b'

from ridder import*

#Various Parameters:
G=6.674*10**-11
M=5.974*10**24
m=7.348*10**22
R=3.844*10**8
w=2.662*10**-6

def f(r):
	return G*M*(R-r)**2-G*m*r**2-w**2*r**3*(R-r)**2 #Rearranged so that f=0 and so that there are no fractions
root = ridder(f,0,R,tol=1.0e-9)
print 'Using the ridder function r is calculated to be:'
print '%e' %(root) #gets in scientific form
