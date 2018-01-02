#Imports
from ridder import *

#Constants
LowerLimit = 0.0
UpperLimit = 10.0

def f(x):
    return (x)**2

Root = ridder(f,LowerLimit,UpperLimit)
print Root
