#Imports
from scipy.optimize import fsolve

#Constants
InitialEstimate = 10.0

def f(x):
    return (x)**2

Root = fsolve(f,InitialEstimate)
print Root
