#Imports
from scipy.integrate import quad as sciquad

#Constants
LowerLimit = 0
UpperLimit = 10

#Defining Function
def function(x):
	return (x**2)

#Using Scipy.Integrate.Quad inputs of the function, the lower integration limit and the upper integration limit	
Answer = sciquad(function,LowerLimit,UpperLimit)

#Returns the Definite intergral and an estimate of the absolute error in an array
#Answer[0] (first term) = The numerical value for the integration
#Answer[1] (second term) = The Error on your integration
print Answer

