#interpolation -predicting missing points using a polynomial fit baised on points you are given.
# three types barycentric interpolate, least squares fit (polyFit) and cubic spline (interp1d).

-----------------------------------------------------------------------------------------------
#barycentric interpolate (example assesment 1 Q3 part a)
from scipy import interpolate
from scipy.interpolate import barycentric_interpolate as bi
#when you are given an array of x and corresponding y values you can use them to estimate a value y value at a value of x you have not been given (let the unknown x be called xu and its corresponding y value be called yu) using 

yu=bi(X, Y, xu) #where X is an array of know x values and Y an array of known Y values

#Barycentric interpolate gives a polynomial of n-1 where n is the number of data points 

-------------------------------------------------------------------------------------------------
#polyFit (least squares fit) (example assesment 1 Q3 part c)
#creates a least squares polynomial fit 
from polyFit import * #where polyFit is a file on study direct

c = polyFit(xData,yData,m).
    Returns coefficients of the polynomial
 
P=polyFit(x,y,xu) #uses least squares fit to create a polynomial P
yu=P[0]+P[1]*(xu)+P[2]*(xu)**2  #can use coefficients of the polynomial to find yu using P[n]*xu**n

#gives a polynomial of degree n as you specify when using P[n]*xu**n

------------------------------------------------------------------------------------------------------------------
#cubic spline (interp1d) (example assesment 1 Q3 part b)

from scipy import interpolate

f=interpolate.interp1d(x,y, kind='cubic') #creates a cubic function that fits the graph can use kind= linear, quadratic ect or 1 2,3 for polynomial order

yu=f(xu) #uses interpolation function returned by interp1d to find yu at a point xu
print yu
