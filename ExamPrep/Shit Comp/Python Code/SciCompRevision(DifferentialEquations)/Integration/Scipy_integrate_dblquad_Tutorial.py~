#Imports
from scipy.integrate import dblquad

#Constants
LowerLimit_x = 0.0
UpperLimit_x = 10.0

LowerLimit_y = 0.0
UpperLimit_y = 10.0

#Defining Function
def function(x,y):
	return (x**2)+(y**2)

# Turning the constants into a function. (Makes the code work).
def Lfy(x):
	return LowerLimit_y
def Ufy(x):
	return UpperLimit_y

#Using Scipy.Integrate.dblQuad inputs of the function, the lower integration limit and the upper integration limit	
Answer = dblquad(function,LowerLimit_x,UpperLimit_x,Lfy,Ufy)

#Returns the Definite intergral and an estimate of the absolute error in an array
#Answer[0] (first term) = The numerical value for the integration
#Answer[1] (second term) = The Error on your integration
print Answer


