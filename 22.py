import numpy as np
import math


a = [[math.pi,-math.e,2**(1/2),-(3**(1/2)),11**(1/2)],[(math.pi)**2,math.e,-math.e**2,3.0/7.0,0],[5**(1/2),-(6**(1/2)),1,-(2**(1/2)),math.pi],[(math.pi)**3,(math.e)**2,-(7**(1/2)),1.0/9.0,2**(1/2)]]

print(" :  Start   :",a)
for i in range(len(a)-1):
    b = []
    for ii in range(i,len(a)):
        b.append(abs(a[ii][i]))
    b.sort()
    for jj in range(i,len(a)):
        if(b[-1]==abs(a[jj][i])):
            p = a[i]
            a[i] = a[ii]
            a[ii] = p
    print(i," :  Pivoting  :",a)
    x = a[i][i]
    for j in range(len(a)+1):
        a[i][j] = a[i][j]/x
    print(i," :  Normalizing  :",a)
    for k in range(i+1,len(a)): 
        y = a[k][i]
        for f in range(len(a)+1):
            a[k][f] = a[i][f]*y - a[k][f]
    print(i," :  Making zeros  :",a)
    print("")
