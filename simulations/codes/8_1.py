#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy
import matplotlib.pyplot as plt

bv = np.loadtxt('../data/ber_2D.dat', dtype='double')
nv = np.loadtxt('../data/gau_2D.dat', dtype='double')
a = 10**(0.5)
sig = a*bv + nv
print(bv)
#Specify colours
C = np.where(bv[:,0] > 0, 'b', 'r')

plt.scatter(sig[:,0], sig[:,1], s=3, c=C)
plt.grid() #creating the grid
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.scatter([], [], s=3, c='r')
plt.legend(["$y|s_0$", "$y|s_1$"])
plt.savefig('../figs/8_1.png')
