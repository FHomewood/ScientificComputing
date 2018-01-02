#Imports
from bisection import *

#Constants
LowerLimit = 0.0
UpperLimit = 10.0

def f(x):
    return (x)**2

Root = bisection(f,LowerLimit,UpperLimit)
print Root
