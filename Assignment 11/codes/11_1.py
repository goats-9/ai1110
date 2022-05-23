#Code by Gautam Singh
#May 23, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Verify an identity of n-component Boolean Algebra
#Using Bernoulli Trials

from ctypes import sizeof
import time
import numpy as np
import itertools as it
import scipy.special as sp

#Sample size (3 for simplicity)
n = 3

#Randomly generate the parameters
p = np.random.random()
q = 1 - p

#Generate the outcome of the experiment
A = np.random.randint(0, 2, n)

lhs = rhs = 1
#Manual calculations
lhs *= (p if A[0] == 1 else q)
lhs *= (p if A[1] == 1 else q)
lhs *= (p if A[2] == 1 else q)

#Using the identity
rhs = (p**(np.count_nonzero(np.where(A == 1, 1, 0))))*(q**(np.count_nonzero(np.where(A == 0, 1, 0))))

if (lhs == rhs): 
    print("The identity is verified.\nProbability of occurence in this simulation =", rhs)
