#Imports
import numpy as np
from numpy.fft import rfft, irfft #Importing built in Fast Fourier Transforms: rfft is real fast fourier transform, irfft is inverse real fast fourier transform

InputArray = np.zeros(100) #Array to be fourier transformed
for i in range(100):
    InputArray[i] = i
print InputArray[10]

FT = rfft(InputArray) #Fourier transform function takes array as input and outputs an array of 1/2 N +1 size. e.g. If InputArray is 100x100, FT will be 51x51. FT is array of coefficients of sinusoidal functions.
print FT[10]

#FT array can be manipulated e.g. Removing coefficients for smoothing

IFT = irfft(FT) #Inverse fourier transform function takes array as input and outputs an array of 2(N-1) size e.g. If FT is 51x51, IFT will be 100x100
print IFT[10]

#An explicit Discrete Fourier Transform code is supplied in the slides, but is more complex and less efficient than the in built fast fourier transforms.
