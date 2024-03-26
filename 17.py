import numpy as np


t = 0.0001        #tolerance
a = [[5,-2],[-2,8]]
b = a
v = [[1,0],[0,1]]
b01 = 1
b10 = 1
i = 0
while (abs(b01)>t or abs(b10)>t):
    q = np.linalg.qr(b)[0]
    r = np.linalg.qr(b)[1]
    b = np.dot(r,q)
    v = np.dot(v,q)
    b01 = b[0][1]
    b10 = b[1][0]
eig = [b[0][0],b[1][1]]
eig.sort()
eig_other = np.linalg.eigh(a)[0]
print("The eigenvalues produced by 'qr decomposition' are : ",eig)
print("The eigenvalues produced by 'numpy.linalg.eigh' are : ",eig_other)

print("Note that they match upto ",abs(eig[0]-eig_other[0])/eig_other[0] * 100, "% and ", abs(eig[1]-eig_other[1])/eig_other[1] * 100,"% respectively.")