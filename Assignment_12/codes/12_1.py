#Code by Gautam Singh
#May 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Verify a limit on Negative Binomial Distribution

import numpy as np
from scipy.special import binom

#Generate parameters (m/n = 3, p = 1/4)
N = np.linspace(100, 200, 10)
p = 1.0/4
r = 1
k = 3
eps = 1e-3

#Get calculated values for finite m and n
pr = 1.0*binom(k - 1, r - 1)*(binom(4*N - k, N - r))/(binom(4*N, N))

#Get pmf
pr_conv = np.ones(10)*(binom(k - 1, r - 1))*(p**r)*((1 - p)**(k - r))
print(abs(pr - pr_conv))
if (abs(pr[-1] - pr_conv[-1]) < eps): print("Limit is verified")
