#Imports
import pylab as pyl
import numpy as np

#Constants
StartPoint = 0 #Lower x limit of the graph
EndPoint = 20 #Higher x limit of the graph
NumberOfPoints = 1000
Graph_lower_xlimit = 0 #Lower x limit for the field of view of the graph.
Graph_Higher_xlimit = 5 #Higher x limit for the field of view of the graph.
Graph_lower_ylimit = 0 #Lower y limit for the field of view of the graph.
Graph_Higher_ylimit = 20 #Higher y limit for the field of view of the graph.

#Functions
x = np.linspace(StartPoint,EndPoint,NumberOfPoints) # Domain from StartPoint to EndPoint, with 'NumberOfPoints' points.
y = x**2

#Running
pyl.figure(1)
pyl.plot(x,y,'b-',label='This is a Generic Graph') # 'b' = blue, '-' = line
# Copy and past the following URL for further detail on graph customisation: jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html
pyl.legend(loc = 'upper right') # Can also use other variations such as "lower" and "left".
pyl.xlabel('This is the x axis')
pyl.ylabel('This is the y axis')
pyl.title('This is the title of the graph')
pyl.xlim(Graph_lower_xlimit,Graph_Higher_xlimit) #Sets the x limits of the view of the graph to a desired set of values
pyl.ylim(Graph_lower_ylimit,Graph_Higher_ylimit) #Sets the y limits of the view of the graph to a desired set of values
pyl.show() # Shows the graphs should be put after you have completed all the figures so only one "pyl.show()" statement is required.
