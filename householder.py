import numpy as np

def lamb_house(func,x0,e):
    x[0]=x0
    n=0
    x[1]=x[0]+d
    f1=(3*T*x - 2 + 2*l**3*x/y)/(1-x**2)
    f2=(3*T - 5*x*f1+ 2*(1-l**2*x**3/y**3))/(1-x**2)
    f3=(7*x+5*x*f2+8*f1-6*(1-l**2)*l**5 *x /y**5)/(1-x**2)

    while x[n]-x[n-1]>e:
        xn=x[n]
        x[n+1]=xn-f(xn)*(f1(xn)**2-f(xn)*f2(xn)/2)/(f1(xn)*(f1(xn)**2-f(xn)*f2(xn))+(f3(xn)*f(xn)**2)/6)


lamb_house(x,x,y)
