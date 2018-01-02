from pylab import *
from scipy import interpolate, optimize
from numpy import *

# construct data point arrays first
h = array([0.0,1.525,3.050,4.575,6.100,7.625,9.150])
rho = array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])


# Part A
# use Barycentric initally as the most direct path to an answer
print "At 2km, the polynomial, interpolated value is:"
print(str(interpolate.barycentric_interpolate(h,rho,2.0)))

print "And at 4km, the interpolated value is:"
print(str(interpolate.barycentric_interpolate(h,rho,4.0)))

print "And at 8km, the interpolated value is:"
print(str(interpolate.barycentric_interpolate(h,rho,8.0)))


# B: cubic spline
fit = interpolate.interp1d(h,rho,kind='cubic') #set up fit, called as fit(value)

print "At h=2, h=4 and h=8 respectively, using a cubic spline, rho="
print fit(2.0), ", ", fit(4.0), ", ",fit(8.0)


# C: errors
rho_actual = 0.67

print "Absolute error for polynomial interpolation:"
err_abso_poly = np.abs(interpolate.barycentric_interpolate(h,rho,4.0)-rho_actual)
print err_abso_poly
print "Relative error for polynomial interpolation:"
print np.abs((err_abso_poly)/rho_actual)

print "\nAbsolute error for cubic spline:"
err_abso_spline = np.abs((fit(4.0)-rho_actual))
print err_abso_spline
print "Relative error for cubic spline:"
print np.abs((err_abso_spline)/rho_actual)