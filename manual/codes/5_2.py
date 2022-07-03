#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

sz = int(1e3)
bv = np.loadtxt('../data/ber.dat', dtype='double')
nv = np.loadtxt('../data/gau_noise.dat', dtype='double')
sig = 5*bv + nv
x = np.linspace(0, 1, sz)
plt.plot(x, sig, '.')
plt.xlabel('n ($\\times 10^3$)')
plt.ylabel('y(n)')
plt.grid()
plt.savefig('../figs/5_2.png')
