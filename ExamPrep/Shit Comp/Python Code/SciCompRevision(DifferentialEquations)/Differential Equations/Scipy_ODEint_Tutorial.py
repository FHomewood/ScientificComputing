#Imports
import numpy as np
from scipy.integrate import odeint

# Example: x''(t) + x(t) = 0.

#Constants
InitialxValue = 1.0 #Starting x value
InitialxPrimeValue = 0.0 #Starting x' value
InitialConditions = np.array([InitialxValue,InitialxPrimeValue]) # Initial x and x' values.
Initial_t_Value = 0.0 #Starting value of t
Final_t_Value = 10.0 # Final value of t
StepSize = 0.01
tRange = np.arange(Initial_t_Value,Final_t_Value,StepSize)

#Defining the equation
def function(y,t): 
	f = np.zeros(2) # The function is an array of 2 zeros (empty).
	f[0] = y[1] # The first term of the array is the first differential of x. y[0] = x (first term = full)
	f[1] = -y[0] # The second term of the array is the second differential of x. y[1] = x' (second term = full)
	return f # Returns the function of an array that contains the first differential of x and the second differential of x. f = [x'(t),x''(t)]

#Integrating
# Answer[0] = x values
# Answer[1] = x' values
Answer = odeint(function, InitialConditions, tRange)

print Answer
