#Imports
import numpy as np
from numpy.fft import rfft2, irfft2 #Importing built in 2D Fast Fourier Transforms: rfft2 is 2D real fast fourier transform, irfft2 is 2D inverse real fast fourier transform

InputArray = np.zeros((100,100)) #Array to be fourier transformed
for i in range(100):
    for j in range(100):
        InputArray[i,j] = i+j
print InputArray[10,10]

FT = rfft2(InputArray) #Fourier transform function takes array as input and outputs an array of 1/2 N +1 size. e.g. If InputArray is 100x100, FT will be 100x51. FT is array of coefficients of sinusoidal functions.
print FT[10,10]

#FT array can be manipulated e.g. Removing coefficients for smoothing

IFT = irfft2(FT) #Inverse fourier transform function takes array as input and outputs an array of 2(N-1) size e.g. If FT is 100x51, IFT will be 100x100
print IFT[10,10]

#An explicit Discrete Fourier Transform code is supplied in the slides, but is more complex and less efficient than the in built fast fourier transforms.
