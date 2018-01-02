#Imports
from matplotlib import pyplot as plt
import numpy as np

#Constants
StartPoint = 0
EndPoint = 20
NumberOfPoints = 1000
Graph_lower_xlimit = 0
Graph_Higher_xlimit = 5
Graph_lower_ylimit = 0
Graph_Higher_ylimit = 20

#Functions
x = np.linspace(StartPoint,EndPoint,NumberOfPoints) # Domain from StartPoint to EndPoint, with 'NumberOfPoints' points.
y = x**2

#Running
plt.figure(1)
plt.plot(x,y,'b-',label='This is a Generic Graph') # 'b' = blue, '-' = line
# Copy and past the following URL for further detail on graph customisation: jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html
plt.legend(loc = 'upper right') # Can also use other variations such as "lower" and "left".
plt.xlabel('This is the x axis')
plt.ylabel('This is the y axis')
plt.title('This is the title of the graph')
plt.xlim(Graph_lower_xlimit,Graph_Higher_xlimit) #Sets the x limits of the view of the graph to a desired set of values
plt.ylim(Graph_lower_ylimit,Graph_Higher_ylimit) #Sets the y limits of the view of the graph to a desired set of values
plt.show() # Shows the graphs should be put after you have completed all the figures so only one "plt.show()" statement is required.
