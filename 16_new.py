import numpy as np


x_k = [7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]
a = [[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]]
b = [1,2,3,4,5]

 

x_g = np.zeros(len(a)) # intial guess
tol = 0.01
w = 1.25

#print(1+a[1][1])


#******************L D U*******************
def ldu(a):
    d,l,u = np.zeros((len(a),len(a))),np.zeros((len(a),len(a))),np.zeros((len(a),len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            if (i<j):
                l[i][j] = a[i][j]
            elif(i>j):
                u[i][i] = a[i][j] 
            else:
                d[i][j] = a[i][j]   
    return [l,d,u]




# *******************JACOBI METHOD*********************
def jacobi(a,b,tol,x_g,x_k):
    diff = 1
    itr = 0
    x=np.zeros(len(a))
    while (diff>tol):
        for i in range(len(a)):
            q1 = 0
            for j in range(len(a)):
                if(i!=j):
                    q1 = q1-a[i][j]*x_g[j]
            x[i] = (1.0/a[i][i])*(q1+b[i])
        x_g = x
        diff = np.linalg.norm(x_k-x)
        itr = itr + 1
    print("Using the Jacobi method, x = ",x)
    print("Number of iterations required for Jacobi method = ",itr)
    return 
jacobi(a,b,tol,x_g,x_k)



# *****************GAUSS-SEIDEL METHOD*******************
def gs(a,b,tol,x_g,x_k):
    diff = 1
    itr = 0
    x=np.zeros(len(a))
    while (diff>tol):
        for i in range(len(a)):
            q1 = 0
            for j in range(len(a)):
                if(j<i):
                    q1 = q1-a[i][j]*x[j]
                elif(j>i):
                    q1 = q1-a[i][j]*x_g[j]
            x[i] = (1.0/a[i][i])*(q1+b[i])
        x_g = x
        diff = np.linalg.norm(x_k-x)
        itr = itr + 1
    print("Using the Gauss-Seidel method, x = ",x)
    print("Number of iterations required for Gauss-Seidel method = ",itr)
    return 
gs(a,b,tol,x_g,x_k)
    


#*********************RELAXATION METHOD***********************
def rel(a,b,tol,x_g,x_k,w):
    diff = 1
    itr = 0
    x=np.zeros(len(a))
    while (diff>tol):
        for i in range(len(a)):
            q1 = 0
            for j in range(len(a)):
                if(j<i):
                    q1 = q1-a[i][j]*x[j]
                else:
                    q1 = q1-a[i][j]*x_g[j]
            x[i] = x_g[i]+(1.0*w/a[i][i])*(q1+b[i])
        x_g = x
        diff = np.linalg.norm(x_k-x)
        itr = itr + 1
    print("Using the Relaxation method, x = ",x)
    print("Number of iterations required for Relaxation method = ",itr)
    return 
rel(a,b,tol,x_g,x_k,w)

#***********************CONJUGATE GRADIANT METHOD*********************

def conj(a,b,tol,x_g,x_k,w):
    r = b-np.dot(a,x_g)
    p = r
    itr = 0
    diff = 1
    while(diff>tol):
        alpha = np.dot(r,r)/np.dot(np.dot(p,a),p)
        x = x_g + np.dot(alpha,p)
        rn = r - np.dot(np.dot(alpha,a),p)
        diff = np.linalg.norm(x-x_k)
        beta = np.dot(rn,rn)/np.dot(r,r)
        p = rn + np.dot(beta,p)
        r = rn
        itr = itr + 1
        x_g = x
    print("Using the CG method, x = ",x)
    print("Number of iterations required for CG method = ",itr)
    return
conj(a,b,0.01,x_g,x_k,w)