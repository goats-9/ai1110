#Code by Gautam Singh
#April 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Create a PMF and CDF subplot for a single die roll

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Array for PMF
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
plt.plot(X, Z, 'ko-')
plt.xlabel('Value of X')
plt.ylabel('Cumulative Probability')
plt.xticks(X)
plt.grid() # minor
#plt.axis('equal')
plt.tight_layout() #Spaace the subplots properly
plt.savefig('../figs/6_1.png')