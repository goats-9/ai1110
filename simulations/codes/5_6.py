import numpy as np
import mpmath as mp
from matplotlib import pyplot as plt
import scipy

bv = np.loadtxt('../data/ber.dat', dtype='double')
nv = np.loadtxt('../data/gau.dat', dtype='double')

def error(a):
    a_new = 10**(a/10.0)
    sig = a_new*bv + nv
    n0 = np.count_nonzero(bv > 0)
    n1 = np.count_nonzero(bv < 0)
    e0 = np.count_nonzero((sig < 0) & (bv > 0)) 
    e1 = np.count_nonzero((sig > 0) & (bv < 0))
    return 0.5*(e0/n0 + e1/n1)

err_vec = scipy.vectorize(error, otypes=['double'])

def qfunc(x):
    return (0.5)*mp.erfc(x/np.sqrt(2))

qfunc_vec = scipy.vectorize(qfunc, otypes=['double'])

A = np.linspace(0, 10, 11)
plt.plot(A, err_vec(A), '.')
plt.plot(A, qfunc_vec(10**(A/10.0)))
plt.grid()
plt.xlabel('$A$ (dB)')
plt.ylabel('$P_e(A)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/5_6.png')
