#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt
import scipy

def uni_cdf(x):
    if (x < 0): return 0
    elif (0 <= x < 1): 
        return x*1.0
    else: return 1

arr_func = scipy.vectorize(uni_cdf, otypes=['double'])

x = np.linspace(-4,4,80)#points on the x axis
#points for analytical cdf
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,80):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err,'.')#plotting empirical CDF
plt.plot(x,arr_func(x))#plotting analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/1_2.png')
