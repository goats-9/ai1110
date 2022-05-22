#Code by Gautam Singh
#May 20, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Simulate binomial trials to find the CDF

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

#Number of samples
N = 1000000

#Binomial distribution parameters
n = 10
p = 0.05

#Answer for comparison and precision
ans = int(binom(10, 0))*(0.95**10) + int(binom(10, 1))*(0.05)*(0.95**9)
eps = 1e-3

A = np.random.binomial(n, p, N)
C = np.bincount(A, minlength=n+1)
R = (np.cumsum(C))/N
print("Practical probability =", R[1])
print("Theoretical probability =", ans)

#Comparison
if (abs(R[1] - ans) < eps):
    print("The answer is verified.")