# Question 3 - Assignment 3 -due 07/12/2015
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt
 # part a

A = np.ones(500) # first 500 ones are even, so f(t)=1
B = np.array(-A) # next 500 ones are odd, so f(t)=-1

N = np.concatenate((A,B)) # combines A and B to describe the function

# part b

DFT = fft.rfft(N) # real part

print '---DIRECT FOURIER TRANSFORM ---'
print DFT

# part c

DFT_5 = fft.rfft(N)
for i in range (5,501):
    DFT_5[i]=0
    
DFT_10 = fft.rfft(N)
for i in range (10,501):
    DFT_10[i]=0
    
DFT_50 = fft.rfft(N)    
for i in range (50,501):
    DFT_50[i]=0
    
# part d
IFT =fft.irfft(DFT)
IFT_5 = fft.irfft(DFT_5)
IFT_10 = fft.irfft(DFT_10)
IFT_50 = fft.irfft(DFT_50)

# part e

t = np.linspace(0,1,1000) # 1000 time values between 0-1

plt.plot(t,N)
plt.plot(t,IFT)
plt.plot(t,IFT_5)
plt.plot(t,IFT_10)
plt.plot(t,IFT_50)
plt.title('Inverse Fourier transform')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

