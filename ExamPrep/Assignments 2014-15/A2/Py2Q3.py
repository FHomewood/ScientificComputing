print 'Question 3b'


import math as m

#Variables

h1=0.5
h2=0.1
m.tanh(1+h1)
def G(h):
	x=1.0
	return (((4*m.tanh(x+(h/2)))-(4*m.tanh(x-(h/2))))/(3*h))-((m.tanh(x+h)-m.tanh(x-h))/(6*h))

print "at x=1 and h=0.5"
print "G(0.5) =",G(h1)
print "at x=1 and h=0.1"
print "G(0.1) =",G(h2)

