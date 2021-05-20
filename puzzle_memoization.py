import numpy as np 

N=500

T = np.full((N+1,N+1), -1.)

#This array is only for pairs with y==1
Yequals1 = np.full((2, N+1), -1.)#line 0 is for anticlockwise and line 1 for clockwise


def f(x, y, clockwise, t):
    print("x=", x, " e y=",y)

    if T[x,y] >= 0. and y!=1:
        return T[x,y]
    
    value = -1.

    if x==y and y==1:
        print("a")
        value = 1 + (1/(N+1))*f(N,1, True, t+1) + (N/(N+1))*f(2,1, False, t+1)
        T[1,1] = value
    elif x!=y and y==1:

        print("y==1")
        if x==N or x==2:
            print("t = ", t, "x = ", x)
            if t>1:
                print("t>1: ",t)
                return 0.       

        if clockwise:
            if Yequals1[1,x] >= 0.:
                return Yequals1[1,x]
            value = (x/(N+1))*(1+f(x-1,y,True,t+1)) + ((N-x+1)/(N+1))*(N+1-x+y+f(y+1,x,False,t+N+1-x+y))
            Yequals1[1,x] = value
        else:
            if Yequals1[0,x] >= 0.:
                return Yequals1[0,x]
            value = (x/(N+1))*(x+f(N,x, True,t+x)) + ((N-x+1)/(N+1))*(1+f(x+1,y, False,t+1))
            Yequals1[0,x] = value
    elif x > y and y!=1:
        print("c")
        if x==y+1:
            value = 0.
        else:
            value = (x/(N+1))*(1+f(x-1,y, True,t+1)) + ((N-x+1)/(N+1))*(N+1-x+y+f(y+1,x, False,t+N+1-x+y))
    elif x < y and y!=1:
        print("d")
        if y == x+1:
            value = 0.
        else:
            value = (x/(N+1))*(N+1-y+x + f(y-1,x, True,t+N+1-y+x)) + ((N-x+1)/(N+1))*(1+f(x+1, y, False,t+1))

    #if not (y==1 and value == 0.):
    if y!=1:
        T[x,y] = value
    
    return value

f(1,1, True, 0)

print(T[1,1])
#print(T)
