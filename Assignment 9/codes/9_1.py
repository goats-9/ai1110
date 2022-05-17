#Code by Gautam Singh
#May 17, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Create a PMF and CDF subplot for a single die roll

from telnetlib import XAUTH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
from scipy.stats import binom

#Function for batch implementation of binom.pmf
#To return a numpy.ndarray with required pmf values
def getpmf(n, p):
    A = np.zeros(n + 1)
    for i in range(n + 1):
        A[i] = binom.pmf(i, n, p)
    return A

#Arrays for PMF
X = np.array(range(11))
Y = getpmf(10, 0.05)
Z = np.cumsum(Y)

#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of Y')
plt.ylabel('Probability Mass Function')
plt.xticks(X)
stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(1, 2, 2)
stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of Y')
plt.ylabel('Cumulative Distribution Function')
plt.xticks(X)
plt.grid()
plt.tight_layout() #Space the subplots properly
plt.savefig('../figs/9_1.png')