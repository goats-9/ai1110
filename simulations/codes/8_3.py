#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy
import matplotlib.pyplot as plt

bv = np.loadtxt('../data/ber_2D.dat', dtype='double')
nv = np.loadtxt('../data/gau_2D.dat', dtype='double')

def emp_err(g):
    sig = (10**(g/10))*bv + nv
    n0 = np.count_nonzero(bv[:,0] > 0)
    e0 = np.count_nonzero((sig[:,0] < sig[:,1]) & (bv[:,0] > 0))
    return e0/n0

emp_err_vec = scipy.vectorize(emp_err, otypes=['double'])

def qfunc(x):
    return (0.5)*mp.erfc(x/np.sqrt(2))

def expected_err(snr):
    snr_new = 10**(snr/10)
    return qfunc(snr_new*np.sqrt(2))

expected_err_vec = scipy.vectorize(expected_err, otypes=['double'])

maxrange=100
G = np.linspace(0,10,11)
x = np.linspace(0,10,1000)
plt.plot(G, emp_err_vec(G), '.')
plt.plot(x, expected_err_vec(x))
plt.grid() #creating the grid
plt.xlabel('SNR')
plt.ylabel('$P_e$(SNR)')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/8_3.png')
