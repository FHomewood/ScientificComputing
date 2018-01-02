#Imports
import numpy as np
from euler import *

# Example: x''(t) + x(t) = 0

#Constants
StartValue = 0.0 #Starting value of t
InitialxValue = 1.0 #Starting x value
InitialxPrimeValue = 0.0 #Starting x' value
InitialConditions = [InitialxValue,InitialxPrimeValue] # Initial x and x' values.
StepSize = 0.1
NoofSteps = 100

#Defining the equation
def function(t,y):
	f = np.zeros(2) # The function is an array of 2 zeros (empty).
	f[0] = y[1] # The first term of the array is the first differential of x. y[0] = x (first term = full)
	f[1] = -y[0] # The second term of the array is the second differential of x. y[1] = x' (second term = full)
	return f # Returns the function of an array that contains the first differential of x and the second differential of x. f = [x'(t),x''(t)]

#Integrating
#Answer[0] = x values
#Answer[1] = x' values.
Answer = odeeuler(function,)

print Answer
