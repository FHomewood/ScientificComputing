#Imports
from scipy.integrate import tplquad

#Constants
LowerLimit_x = 0.0
UpperLimit_x = 1.0

LowerLimit_y = 0.0
UpperLimit_y = 2.0

LowerLimit_z = 0.0
UpperLimit_z = 3.0

#Defining Function
def function(x,y,z):
	return (x**2)+(y**2)+(z**2)

# Turning the constant limits into a function. This makes the code callable (work).
def Lfy(x): # The function is in terms of x (constant).
	return LowerLimit_y
def Ufy(x):
	return UpperLimit_y

def Lfz(x,y): # The function is in terms of x and y (constant).
	return LowerLimit_z
def Ufz(x,y):
	return UpperLimit_z

#Using Scipy.Integrate.dblQuad inputs of the function, the lower integration limit and the upper integration limit	
Answer = tplquad(function,LowerLimit_x,UpperLimit_x,Lfy,Ufy,Lfz,Ufz)

#Returns the Definite intergral and an estimate of the absolute error in an array
#Answer[0] (first term) = The numerical value for the integration
#Answer[1] (second term) = The Error on your integration
print Answer


