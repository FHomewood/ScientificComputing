print 'Question 2b'
print ""
h1=0.03 #because 1-0.97 as we take x0 to be 1
h2=0.05 #because 1.05-1.00 again as we take x0 to be 1
fxh1=0.85040 
fx=0.84147
fxh2=0.82612


y1=(fxh2-fxh1)/(h2+h1)

print "f'(1.00)=",y1 
print ""

y2= (2*(fxh2+fxh1-(2*fx)-(y1*(h2-h1))))/(h2**2+h1**2)
print ""
print "f''(1.00)=",y2



