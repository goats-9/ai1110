#Code by Gautam Singh
#May 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Verify an identity on Negative Binomial Distribution

import numpy as np
from scipy.stats import binom
from scipy import ndimage as nd

#Randomly generate the parameters
n = np.random.randint(1, 10)
p = np.random.random()

#Get pmf of distribution
r = np.arange(n + 1)
A = binom.pmf(r, n, p)

#Label odd and even indices
L = np.empty(n + 1)
L[1::2] = 2
L[::2] = 1

#Sum required indices
lhs = nd.sum(A, L, 1)

#Use the formula
rhs = 0.5*(1 + (1 - 2*p)**n)

if (abs(lhs - rhs) < 1e-6):
    print("The identity is verified.\nProbability of the event in this simulation =", round(rhs, 6))
