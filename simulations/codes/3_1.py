#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt

x = np.linspace(-10,10,50)#points on the x axis
x1 = np.linspace(-10,0,50)
y1 = np.zeros(50)
x2 = np.linspace(0,10,50)
y2 = 1 - np.exp(-x2/2)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/uni.dat',dtype='double')
randvar = -2*np.log(1 - randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x,err,'.')#plotting the CDF
plt.plot(np.concatenate([x1,x2]), np.concatenate([y1,y2]))
plt.grid() #creating the grid
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/3_1.png')
