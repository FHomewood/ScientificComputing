#Imports
from scipy.integrate import romberg as sciRom

#Constants
Lower_Limit = 0.0
Upper_Limit = 10.0


#Generic Function
def function(x):
	return x**2

#Computing the integration between the limits.
Answer = sciRom(function,Lower_Limit,Upper_Limit)

# The inbuilt romberg integration has an absolute and relative tolerance of 1.49e-8. The output is the solution to the numerical integration only.
print Answer
