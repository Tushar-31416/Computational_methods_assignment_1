import numpy as np


a = [[2,-1,0],[-1,2,-1],[0,-1,2]]
b = [1,0,0]
p = 1
i = 0
am = a
r = 0
while(p>0.01):
    u = np.dot(np.dot(am,b),b)*1.0
    am = np.dot(a,am)
    v = np.dot(np.dot(am,b),b)*1.0
    rn = abs(v/u)
    p = rn - r
    r = rn
    i = i +1

print("The largest eigenvalue obtained by power method after ",i," iterations is",rn)
print("And the corresponding eigenvector is ",1/v*np.dot(am,b))
eigv = np.linalg.eigvalsh(a)
print("The largest eigenvalue obtained by 'np.linalg.eigvalsh()' is ",eigv[-1])
print("The accuracy of the power method in this case is ",abs(rn - eigv[-1])/eigv[-1])