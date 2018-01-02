#This script takes a pair of inputs, one of a point and another of an interval width, then differentates f(x) at the selected point, using the given step size. to input f(x) and f'(x) simply replace " 'FUNC' " or " 'FUNCPRIME' " with the function.

import numpy as np

#User inputs below.
x=input('Please pick an x value: ')
h=input('Please pick an h value: ')


g=h/2 #Splits the step in half for use in Richardson Extrapolation formula in case that h_2=h_1/2.
#Creates 4 arguments for tanh functions.
x1=x+g
x2=x-g
x3=x+h
x4=x-h

G=(('FUNC'(x1)-'FUNC'(x2))*(4/(3*h)))-(('FUNC'(x3)-'FUNC'(x4))*(1/(6*h))) #The Richardson Formula.
error=((G-('FUNCPRIME'(x))**-2)/('FUNCPRIME'(x)**-2))*100 #Error on approximation as a percentage of the true value.

print 'Richardson Extrapolation Result: ',G
print 'Error: ', error,'%'
