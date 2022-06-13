#Code by Gautam Singh
#June 8, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Hypothesis Testing

import numpy as np
from scipy.stats import norm

#Set percentile
a = 0.01
z = norm.ppf(1-a)

#Generate array of samples given n_0 = 8.7 and n = 8
n_0 = 8.7
n = 8
sigma = 2
N = 64

#Set sample size
sz = 10000

n_q = np.sqrt(N)*(n_0 - n)/sigma
mu = n_q*np.random.random()
A = norm.rvs(loc=mu, scale=1, size=sz)
ans = sz - np.count_nonzero(np.where(A > z))
print("Data drawn from normal distribution with mean", mu)
print("Number of data points in critical region =", ans)
print("Percentage of data points in critical region =", (100.0*ans)/sz)
