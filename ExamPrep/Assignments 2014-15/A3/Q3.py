"""
Q3: Fourier filtering and smoothing
Plot the actual data, then calculate Fourier coefficients
Then plot the transformed data
"""

import numpy as np
import matplotlib.pyplot as plt

# import the Dow data
dow = np.loadtxt("dow.txt", float)

# plot it all onto a graph
dow_l = np.arange(len(dow))

plt.figure(1)
plt.title('Closing values of DOW index per day')
plt.xlabel('Number of days since start of data set')
plt.ylabel('Closing value')
plt.xlim(0,(len(dow)))
plt.plot(dow_l, dow, 'g', label='Unprocessed data')
# we won't display this plot yet, since we want to add to it later



# B
# calculate Fourier coefficients
dowft = np.fft.rfft(dow)
#print dowft #and, oh! look. they're complex.



# C
# what point do we cut off for 10%? LET'S FIND OUT
dowft_l = len(dowft)
dowft_10pc_l = (((dowft_l)//10)) # no need to +1 because we're operating on zero

dowft_f10 = np.copy(dowft)
dowft_f10[(dowft_10pc_l):(dowft_l)] = 0.0 # set all values past the 1/10th point to zero



# D
# inverse transform
inv_dowft_f10 = np.fft.irfft(dowft_f10)
# plot
plt.plot(dow_l,inv_dowft_f10, 'r', label='Inverse transform, 10% of coefficients') # plot individual ones too for clarity
plt.legend(loc=0)
plt.show()



# E
# what point do we cut off for 2%? LET'S FIND OUT
dowft_2pc_l = (((dowft_l)//50))

dowft_f2 = np.copy(dowft)
dowft_f2[(dowft_2pc_l):(dowft_l)] = 0.0 # set all values past the 1/10th point to zero

# inverse transform again
inv_dowft_f2 = np.fft.irfft(dowft_f2)

# plot
plt.figure(2)
plt.plot(dow_l,dow,'g', label='Unprocessed data')
plt.plot(dow_l,inv_dowft_f2, 'b', label='Inverse transform, 2% of coefficients')
plt.title('Closing values of DOW index per day')
plt.xlabel('Number of days since start of data set')
plt.ylabel('Closing value')
plt.xlim(0,(len(dow)))
plt.legend(loc=0)
plt.show()

#plot the whole lot too
plt.figure(3)
plt.plot(dow_l,dow,'g', label='Unprocessed data')
plt.plot(dow_l,inv_dowft_f10, 'r', label='Inverse transform, 10% of coefficients') # plot individual ones too for clarity
plt.plot(dow_l,inv_dowft_f2, 'b', label='Inverse transform, 2% of coefficients')
plt.title('Closing values of DOW index per day')
plt.xlabel('Number of days since start of data set')
plt.ylabel('Closing value')
plt.legend(loc=0)
plt.xlim(0,(len(dow)))
plt.show()