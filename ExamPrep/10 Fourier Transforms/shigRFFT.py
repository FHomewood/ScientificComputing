import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt('EXAMPLE.txt') #Retrieves data from .txt file.
b=np.linspace(0,len(a),len(a)) #Creates a variable for the data to be plotted against.
###
FT1=np.fft.rfft(a)#Performs the real Fast Fourier Transform, argument: source data.
FT2=np.fft.rfft(a)

#The for loops below zero the last 90% and the last 98% of the data respectively.
for i in range(len(FT1)): 
    if i>((len(FT1))//10):
        FT1[i]=0
for i in range(len(FT2)):
    if i>(len(FT2))*0.02:
        FT2[i]=0

iFT1=np.fft.irfft(FT1) #performs the inverse real Fast Fourier Transform, argument: Fourier coefficient array.
iFT2=np.fft.irfft(FT2)

plt.figure(1)
plt.plot(b,a,'b-')
plt.plot(b,iFT1,'r-')
plt.plot(b,iFT2,'g-')
plt.xlabel('XLABEL')
plt.ylabel('YLABEL')
plt.title('TITLE')
plt.show()
