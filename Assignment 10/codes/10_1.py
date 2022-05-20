#Code by Gautam Singh
#May 20, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Verify number of subsets containing k elements is n choose k

from ctypes import sizeof
import time
import numpy as np
import itertools as it
import scipy.special as sp

a = np.random.randint(0, 20)
b = np.random.randint(0, a + 1)
#Theoretical answer
th = sp.comb(a, b, exact=True)
#Counting answer
ct = len(list(it.combinations(np.arange(a), b)))
print("Theoretical count =", th, "\nEmpirical count =", ct)