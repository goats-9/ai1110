#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

def tri_pdf(x):
    if (0 <= x < 1): return x
    elif (1 <= x < 2): return 2 - x
    else: return 0

arr_func = scipy.vectorize(tri_pdf, otypes=['double'])
maxrange=60
x = np.linspace(-2,4,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('../data/tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)],pdf,'.')
plt.plot(x,arr_func(x))#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$p_T(x)$')
plt.legend(["Simulation","Analysis"])
plt.savefig('../figs/4_3.png')
