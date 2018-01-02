#spline (interp1d) 
#interpolates a 1-D function


#f=interpolate.interp1d(x,y, kind='cubic') #creates a cubic function that fits the graph can use kind= linear, quadratic ect or 1 2,3 for polynomial order

#yu=f(xu) #uses interpolation function returned by interp1d to find yu at a point xu
#print yu

#example (assesment 1 Q3 part b)
from scipy import interpolate
import numpy as np


h=np.array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
p=np.array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])

f=interpolate.interp1d(h,p, kind='cubic') #creates a cubic function that fits the graph

c=f(2) #uses interpolation function returned by interp1d to plot at 2

print c

