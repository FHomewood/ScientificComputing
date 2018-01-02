###THIS IS THE MASTER MODULE###

import scipy as sp
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
import copy
from error import *
from gaussElimin import *
from gaussPivot import *
from LUdecomp import *
from LUdecomp3 import *
from swap import *


###Long Lines
#1,2
LL001='[1] Gaussian Elimination \n[2] Gaussian Elimination with LU Decomposition \n[3] Gaussian Elimination with Pivoting \n[4] Fast Fourier Transform'
LL002='[1] scipy.linalg.lu (inbuilt module) \n[2] LUdecomp (standard textbook module)'
LL003='Before inputting your integrand make sure that you have factored out all constants, or defined them, either before running this script, or in the expression.'

###INPUT###
#1,2,3,4,5,6,7,8,9,10,11,12,13
print 'Hello, I can solve the following kinds of problems:\n',LL001,'\nPlease note that numpy has been imported as np, scipy as sp, matplotlib as plt \n'
in001=input('What kind of problem would you like to solve? Please enter a number: ')
if in001==1 or in001==2 or in001==3:
    in002=input('How many elements does your matrix contain: ')
    in003=input('Please list the coefficients of independent variables: ')
    in004=input('Please list the values of dependent variables: ')
    a=np.array(in003,dtype=float) #converts independent variable coefficients to an array
    b=np.array(in004,dtype=float) #converts dependent variable to an array
    c=np.reshape(a, (sqrt(in002),sqrt(in002))) #reshape to square matrix
if in001==2:
    print'How would you like to decompose the matirx? \n',LL002
    in005=input('Please enter a number: ')
if in001==4:
    in006=raw_input("Please enter the name of the text file that contains your data. Don't forget to affix '.txt': ")
    a=np.loadtxt(in006)#Retrieves data from .txt file.
    b=np.linspace(0,len(a),len(a)) #Creates a variable for the data to be plotted against.
    in007=input('What percentage of the values would you like to remove for smoothing?: ')
    in008=raw_input('Please provide an x axis label: ')
    in009=raw_input('Please provide a y axis label: ')
    in010=raw_input('Please provide a title: ')

##########Workers##########
###Gaussian Elimination
#solves a set of simultanious equations

if in001==1:
    d=gaussElimin(c,b) #performs the elimination
    print 'The variables are: ' '\n' , d #outputs result of gaussElimin

###Lower/Upper decomposition
#solves a set of simultanious equations, uses the decomp method from scipy

if in001==2 and in005==1:
    P,L,U=sp.linalg.lu(c) #LU decomposition using linalg. Arguments:(square coefficients matrix). First element of result is lower matrix, second element is upper matrix.
    z=gaussElimin(dot(L,P),b) #Arguments: (Lower triangular matrix, colomb answer matrix)
    x=gaussElimin(U,b) #Arguments: (Upper triangular matrix, result of gaussElimin of Lower tri and answer matrix)
    print 'Upper matrix: ', '\n',U, '\n', 'Lower matrix: ','\n', np.dot(L,P) #displays the upper and lower matrices
    print 'Testing L dot U, this should be equal to a: ', '\n', np.dot(np.dot(L,P),U)
    print 'The variables are: ', '\n', x #outputs the result of the gaussElimin

#solves a set of simultanious equations, uses the decomp method from textbook

if in001==2 and in005==2:
    d=LUdecomp(c) #LU decomposition using LUdecomp. Arguments:(square coefficients matrix)
    e=LUsolve(d,b) #solves the decomposed matrix. Arguments:(result of LUdecomp, dependent variable matrix)
    print 'The variables are: ', '\n', e #outputs the result of the LUsolve
    
###Gaussian Pivot
#solves a set of simultanious equations

if in001==3:
    d=gaussPivot(c,b)
    print 'The variables are: ' '\n' , d #outputs result of gaussPivot

###Fourier Transform
#finds the coefficients of a Fourier series and plots the result

if in001==4:
    FT001=np.fft.rfft(a) #Performs the real Fast Fourier Transform. Arguments:(source data)
    for i in range(len(FT001)): #loop removes the requested percentage of data from the array of coefficients, this smooths the graph
        if i>(len(FT001))*(1-(in007*0.01)):
            FT001[i]=0
    iFT001=np.fft.irfft(FT001) #performs the inverse real Fast Fourier Transform. Argument:(Fourier coefficient array)
    plt.figure(1)
    plt.plot(b,a,'g-',label='Original Data')
    plt.plot(b,iFT001,'r-',label='Smoothed Fourier Transform')
    plt.xlabel(in008)
    plt.ylabel(in009)
    plt.title(in010)
    plt.legend(loc='upper right')
    plt.show()
