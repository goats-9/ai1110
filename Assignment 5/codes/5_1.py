#Code by Gautam Singh
#April 22, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify that the sum of pribabilities of mutually exclusive and exhaustive events is 1

import numpy as np
from numpy import linalg as LA
from numpy import random as RN

#Sample size
N =1500

#Generating Samples
x = RN.randint(0, high = 3, size=N)

#Finding the number of 2's, 1's and 0's
ctr_2 = np.count_nonzero(x==2)
ctr_1 = np.count_nonzero(x==1)
ctr_0 = np.count_nonzero(x==0)

#Compute probabilities
pr_2 = 1.0*ctr_2/N
pr_1 = 1.0*ctr_1/N
pr_0 = 1.0*ctr_0/N

#Display probabilities
print("Probabilities:", pr_0, pr_1, pr_2)
print("Sum of probabilities is:", pr_2 + pr_1 + pr_0)