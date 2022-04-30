#Code by Gautam Singh
#April 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Create a PMF and CDF subplot for a single die roll

def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

#Function for batch usage of line_gen
def batch_plot(A, B):
    len = A.shape[0]
    for i in range(len):
        x_AB = line_gen(A[i, :], B[i, :])
        plt.plot(x_AB[0, :], x_AB[1, :], 'k-')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Arrays for PMF
X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
Z = np.cumsum(Y)

#Extra points
X_pmf = np.array([0, 7])
Y_pmf = np.array([0, 0])
X_cdf = np.array([-1, 0, 7])
Y_cdf = np.array([0, 0, 1])

#Arrays for ticks
T = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7])

#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of X')
plt.ylabel('Probability Mass Function')
plt.xticks(T)
stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')
stem(X_pmf, Y_pmf, linefmt='k--', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(1, 2, 2)
stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
stem(X_cdf, Y_cdf, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of X')
plt.ylabel('Cumulative Distribution Function')
plt.xticks(T)
plt.grid()
plt.tight_layout() #Space the subplots properly
plt.savefig('../figs/6_1.png')