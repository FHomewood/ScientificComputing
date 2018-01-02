import numpy as np

# part (a)

# from lecture notes (week 6)
# G = g(h1)+E(h1) = g(h1)+ch1^p
# G = g(h2)+E(h2) = g(h2)+ch2^p

# >> Eliminate c and solve for G

# G = [ (h1/h2)^p * g(h2) - g(h1) ] / [ (h1/h2)^p - 1 ]

# >> Assume h2 = h1/2

# G = [ 2^p * g(h1/2) - g(h1) ] / [ 2^p - 1 ]

# >> Use Taylor expansion

# f(x+h) = f(x) + hf'(x) + (h^2/2!)f''(x) + (h^3/3!)f'''(x) + (h^4/4!)fiv(x) + (h^5/5!)fv(x) + ...

# f(x-h) = f(x) - hf'(x) + (h^2/2!)f''(x) - (h^3/3!)f'''(x) + (h^4/4!)fiv(x) - (h^5/5!)fv(x) + ...

# >> Sum an d subtract the two expansions

# f(x+h)+f(x-h) = 2f(x) + (h^2)f''(x) + (h^4/12)fiv(x) 

# f(x+h)-f(x-h) = 2hf'(x) + (h^3/3)f'''(x) + (h^5/60)fv(x)

# >> Rearrange for f'(x). The higher orders can be considered errors and not part of the actual solution. 
# Rearranging is only possible using f(x+h)-f(x-h) because f'(x) is cancelled out in f(x+h)+f(x-h)

# f(x+h)-f(x-h) - (h^3/3)f'''(x) - (h^5/60)fv(x) = 2hf'(x)

# [ f(x+h)-f(x-h) ] / 2h = centered approximation 

# [ (h^3/3)f'''(x) - (h^5/60)fv(x) ] / 2h = error associated with centered approximation

# Refer to equation G(h)=g(h)+E(h) where E(h) is the error 
 
# [ f(x+h)-f(x-h) ] / 2h = g(h)

# [ f(x+{h/2})-f(x-{h/2}) ] / h = g(h/2)

# Substitute g(h) and g(h/2) into our equation for G

# G = [ 2^p * ( [ f(x+{h1/2})-f(x-{h1/2}) ] / h ) - ([ f(x+h)-f(x-h) ] / 2h ]) ] / [ 2^p - 1 ]

# part (b)

x=1.0
h=0.5
p=2.0 # this is the order of the error

def f(x): # equation given in Q
    return x+(np.exp(x))

def dfdx(p, x, h): # central difference estimation of a differential
    return (p(x+h/2)-p(x-h/2))/h

g1 = dfdx(f, 1.0, 0.5) # plugging in constants given
g2 = dfdx(f, 1.0, 0.25) 


# say h = h1 --> h2 = h1/2

G = (((2**p)*g2)-g1)/((2**p)-1)

# the error would be the difference between the derivative of f and the estimations g1 and G

def fi(x):
    return 1+(np.exp(x))
    
trueValue=fi(1)

err1=G-trueValue
err2=g1-trueValue


print "The Richardson extrapolation equals",round(G,3),"when x is equal to ",round(x,4)," and h is equal to",h,"with an error of",round(err1,8)
print "The central difference extrapolation equals",round(g1,3),"when x is equal to ",x," and h is equal to",h,"with an error of",round(err2,3)
print "The central difference and Richardson techniques give values that are within each others' error ranges, which is expected."







