def odeeuler(F,x0,y0,h,N):
    x = x0
    y = y0
    for i in range(1,N+1):
        y += h*F(x,y)
        x += h
    return y
