#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt
import scipy

def ral_cdf(x):
    if (x < 0): return 0
    else: return 1 - np.exp(-(x**2)/2)

ral_cdf_vec = scipy.vectorize(ral_cdf, otypes=['double'])

maxrange=50
x = np.linspace(0,5,maxrange)#points on the x axis
#points for analytical cdf
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/ral.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err,'.')#plotting empirical CDF
plt.plot(x,ral_cdf_vec(x))#plotting analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_A(x)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/6_3_cdf.png')
