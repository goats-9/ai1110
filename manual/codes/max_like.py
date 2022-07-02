import numpy as np

sz = 1000
randvar = np.loadtxt('gau_noise.dat', dtype='double')
chkvar = np.loadtxt('ber_gau.dat', dtype='double')
err_pos = chkvar - randvar - 5*np.ones(sz)
err_neg = chkvar - randvar + 5*np.ones(sz)
print("X = 1: ", (1.0)*np.count_nonzero(err_pos)/sz)
print("X = -1: ", (1.0)*np.count_nonzero(err_neg)/sz)
