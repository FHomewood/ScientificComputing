from scipy.optimize import fsolve

### Code to solve a given function using fsolve from scipy.

#Constants defined below.
G = 6.674*10**-11
M = 5.974*10**24 
m = 7.348*10**22 
R = 3.844*10**8
w = 2.662*10**-6



def f(r): #defining function fto be solved for the argument variable.
    return ((G*M)/(r**2))-((G*m)/((R-r)**2))-(w**2)*r 
    
L1=fsolve(f,3*10**8) #Here we use the fsolve routine, arguments (function[must already be defined],starting value for fsolve [must be a reasonable estimate of solution])

print 'The distance from Earth to the Lagrange point L1 is ', L1[0], 'meters.' #Prints the root of the function, as found by fsolve.
