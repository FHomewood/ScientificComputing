#Imports
import numpy as np
from matplotlib import pyplot as plt

TextArray = np.loadtxt('blur.txt') #Reads in a space delimited (values separated by spaces) text file as an array

plt.gray() #Grayscales image for clearing, because colour is too complex (Ilian doesn't understand colours)
plt.imshow(TextArray) #Generates an image from a 2D array
plt.show()
