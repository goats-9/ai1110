#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

def ral_pdf(x):
    if (0 <= x): return x*np.exp(-(x**2)/2)
    else: return 0

ral_pdf_vec = scipy.vectorize(ral_pdf, otypes=['double'])
maxrange=50
x = np.linspace(0,5,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('../data/ral.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)],pdf,'.')
plt.plot(x,ral_pdf_vec(x))#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$p_A(x)$')
plt.legend(["Simulation","Analysis"])
plt.savefig('../figs/6_3_pdf.png')
