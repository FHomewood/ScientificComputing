import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("EXAMLE.txt") # imports the data from the text file
FT = np.fft.rfft(s[:,1]) # finds fourier coefficients of the second column in a
b = np.linspace(0, len(a), len(a))
c = np.linspace(0, len(a)/2, len(a)/2)

for i in range(len(FT)): #Squares every element of the Fourier Transform
    FT[i] = (FT[i])**2

plt.figure(1)
plt.suptitle("TITLE")
plt.plot(c, FT)
plt.xlabel("XLABEL")
plt.ylabel("YLABEL")
plt.show()
