#Code by Gautam Singh
#May 21, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify an identity concerning the probability 
#of getting an even number of heads on tossing n coins.

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.stats import binom

#Number of samples
N = 1000000

#Binomial distribution parameters
n = np.random.randint(30)
p = np.random.random()

#Answer and precision
ans = (1 + (1 - 2*p)**n)*(0.5)
eps = 1e-3

#Label array
L = np.empty(n + 1,)
L[::2] = 1
L[1::2] = 2

A = np.random.binomial(n, p, N)
C = np.bincount(A, minlength=n+1)
R = (ndimage.sum(C, L, 1))/N
print("Practical probability =", R)
print("Theoretical probability =", ans)

#Verifying result
if (abs(R - ans) < eps):
    print("The identity is verified.")