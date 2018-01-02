import numpy as np

t = np.array([0.97,1,1.05]) #Three points at which measurments have been taken: t_1,t_2,t_3				                        
y = np.array([0.85040,0.84147,0.82612])

a = y[0]
b = y[2]
c = t[1] - t[0]
d = t[2] - t[1]
e = y[1]

def diff(f1, f2, g, h):                                                            
    return (f2 - f1)/(g + h)
print "f'(t_2) = ",diff(a,b,c,d)

def diff2(f1, f2, g, h, f):                                                            
    return (2*(f2 + f1-2*f)/(g**2 + h**2))
print "f''(t_2) = ",diff2(a, b, c, d, e)
