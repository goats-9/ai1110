import numpy as np

sz = 1000
noisevar = np.loadtxt('gau_noise.dat', dtype='double')
bervar = np.loadtxt('ber.dat', dtype='double')
n0 = np.count_nonzero(bervar > 0)
n1 = np.count_nonzero(bervar < 0)
chkvar = np.loadtxt('ber_gau.dat', dtype='double')
err_pos = np.count_nonzero((chkvar < 0) & (bervar > 0))
err_neg = np.count_nonzero((chkvar > 0) & (bervar < 0))
print("X = 1: ", err_pos)
print("X = -1: ", err_neg)
