#Code by Gautam Singh
#April 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Create a PMF for a single die roll

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Array for PMF
X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

#Plotting the PMF
stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.savefig('../figs/6_1.png')