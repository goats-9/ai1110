#Code by Gautam Singh
#June 8, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Find pdf of np.random.random()

import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB


#Set sample size
sz = 10000000

mu = np.random.random(size=sz)
B = np.linspace(0, 1, 100)
plt.hist(mu, bins=B, density=True)
A = np.array([0, 1])
B = np.array([1, 1])
L_AB = line_gen(A, B)
plt.axhline(y=0, c='black')
plt.axvline(x=0, c='black')
plt.xlabel('x')
plt.ylabel('$p_X(x)$')
plt.plot(L_AB[0, :], L_AB[1, :], 'k')
plt.savefig('../figs/np_random.png')
