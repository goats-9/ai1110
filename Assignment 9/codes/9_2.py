#Code by Gautam Singh
#May 20, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Create a PMF and CDF subplot for a single die roll

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
from scipy.stats import binom

#Number of samples
N = 1000000

#Binomial distribution parameters
n = 10
p = 0.05

A = np.random.binomial(n, p, N)
C = np.bincount(A, minlength=n+1)
R = (np.cumsum(C))/N
print(R)
