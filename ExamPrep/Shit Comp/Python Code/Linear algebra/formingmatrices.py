#Forming Matrices

#for a matrix thats elements depend on a function use the following code

A=zeros((n,m),float) #creates a n by n matrix of zeros as n and m

for i in range (0,n):
	for j in range (0,m):
		A[i,j]=(i+j)**2  # where n/m is the matrix lenght/width and (i+j)**2 defines each a component as the row and collumn number added and squared change depending on function


#for a matrix that is given as inital values use an array for example
A=np.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]]) 
