import numpy as np
from matplotlib import pyplot as plt
import scipy

def error(a):
    bv = np.loadtxt('ber.dat', dtype='double')
    nv = np.loadtxt('gau_noise.dat', dtype='double')
    sig = a*bv + nv
    e0 = np.count_nonzero((sig < 0) & (bv > 0)) 
    e1 = np.count_nonzero((sig > 0) & (bv < 0))
    return (e0 + e1)/2000

err_vec = scipy.vectorize(error, otypes=['double'])

bervar = np.loadtxt('ber.dat', dtype='double')
noisevar = np.loadtxt('gau_noise.dat', dtype='double')
A = np.linspace(0, 6, 1000)
E = err_vec(A)
plt.plot(A, E)
plt.grid()
plt.xlabel('$A$ (dB)')
plt.ylabel('$P_e(A)$')
plt.savefig('../figs/error.png')
