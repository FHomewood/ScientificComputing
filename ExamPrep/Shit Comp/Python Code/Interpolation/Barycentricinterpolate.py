#barycentric interpolate (example assesment 1 Q3 part a)

from scipy import interpolate
from scipy.interpolate import barycentric_interpolate as bi
import numpy as np

#when you are given an array of x and corresponding y values you can use them to estimate a value y value at a value of x you have not been given (let the unknown x be called xu and its corresponding y value be called yu) using 

#yu=bi(X, Y, xu) where X is an array of know x values and Y an array of known Y values

#Barycentric interpolate gives a polynomial of n-1 where n is the number of data points 

#example (example assesment 1 Q3 part a)
h=np.array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
p=np.array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])

b=bi(h, p, 5)
print b
