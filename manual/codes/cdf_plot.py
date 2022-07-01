#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-4,4,80)#points on the x axis
#points for analytical cdf
c1 = np.zeros(40)
c2 = np.linspace(0,1,10)
c3 = np.ones(30)
c = np.concatenate([c1, c2, c3])
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,80):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err,'o')#plotting empirical CDF
plt.plot(x,c)#plotting analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/uni_cdf.png')
#if using termux
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#endif using termux
