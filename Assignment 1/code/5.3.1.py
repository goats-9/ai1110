import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

A = np.array([2, 2])
B = np.array([2, -2])
C = np.array([0, -1])
D = np.array([0, 1])
Ref_Mat = np.array([[-1, 0], [0, 1]])
A_r = A@Ref_Mat
B_r = B@Ref_Mat
C_r = C@Ref_Mat
D_r = D@Ref_Mat
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)
x_r_AB = line_gen(A_r,B_r)
x_r_BC = line_gen(B_r,C_r)
x_r_CD = line_gen(C_r,D_r)
x_r_AD = line_gen(A_r,D_r)
plt.grid()
plt.plot(x_AB[0,:], x_AB[1,:], 'k')
plt.plot(x_BC[0,:], x_BC[1,:], 'k')
plt.plot(x_CD[0,:], x_CD[1,:], 'k')
plt.plot(x_AD[0,:], x_AD[1,:], 'k')
plt.plot(x_r_AB[0,:], x_r_AB[1,:], 'k')
plt.plot(x_r_BC[0,:], x_r_BC[1,:], 'k')
plt.plot(x_r_CD[0,:], x_r_CD[1,:], 'k')
plt.plot(x_r_AD[0,:], x_r_AD[1,:], 'k')
plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points")
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("A'",A_r,xytext=(0,5),textcoords="offset points", ha = 'right')
plt.annotate("B'",B_r,xytext=(0,5),textcoords="offset points", ha = 'right')
plt.annotate("C'",C_r,xytext=(0,5),textcoords="offset points", ha = 'right')
plt.annotate("D'",D_r, xytext=(0,5), textcoords="offset points", ha = 'right')
plt.savefig("../figs/5.3.1.png")
plt.show()