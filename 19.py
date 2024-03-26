import time
import numpy as np


i_t=time.time()

a1 = [[2,1],[1,0]]
a2 = [[2,1],[1,0],[0,1]]
a3 = [[2,1],[-1,1],[1,1],[2,-1]]
a4 = [[1,1,0],[-1,0,1],[0,1,-1],[1,1,-1]]
a5 = [[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]]

a = [a1,a2,a3,a4,a5]
b = []

for i in range(5):
    decomposed = []
    s_time = time.time_ns()
    d = np.linalg.svd(a[i])
#    c_time = time.time_ns() - s_time
    print("Time taken for decomposition of matrix ",i+1," is = ",time.time_ns()-s_time, " nano seconds.")
    for j in range(3):
        decomposed.append(d[j])
    b.append(d)
    print("The decomposed matrices of matrix ",i+1, " is :",d)
#print (b)

# CHECKING IF THE DECOMPOSITION IS CORRECT

singular = []
for ele in range((len(b))):
    s = np.zeros((len(a[ele]),len(a[ele][0])))
    for d in range(len(b[ele][1])):
        s[d][d] = b[ele][1][d]
#    print("s = ",s)
    print("multiplication = ", np.dot(np.dot(b[ele][0],s),b[ele][2]))
print("Note that the multiplication gives back the same matrices we started from.")

#print("time taken =",time.time()-i_t)