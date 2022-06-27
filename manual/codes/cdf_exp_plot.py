#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-20,20,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
randvar = -2*np.log(1 - randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')

plt.savefig('../figs/exp_cdf.png')
#if using termux
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#endif using termux
