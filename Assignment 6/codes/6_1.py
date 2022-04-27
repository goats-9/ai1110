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

#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of X')
plt.ylabel('Probability Mass Function')
plt.xticks(X)
stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(1, 2, 2)
plt.plot(X, Z, 'k.')
plt.plot(X[1:], Z[0:5], 'k.', fillstyle='none')
A = np.column_stack((X[:5], Z[:5]))
B = np.column_stack((X[1:], Z[:5]))
batch_plot(A, B)
plt.xlabel('Value of X')
plt.ylabel('Cumulative Probability')
plt.xticks(X)
plt.grid()
plt.tight_layout() #Spaace the subplots properly
plt.savefig('../figs/6_1.png')