#Code by Gautam Singh
#April 18, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To simulate tossing one coin 1000 times

import numpy as np
from numpy import linalg as LA
from numpy import random as RN 

#Sample size
N =1000 

#Generating Samples
x = RN.randint(0, high = 2, size=N)

#Finding the number of 1's and 0's
ctr_1 = np.count_nonzero(x==1)
ctr_0 = N - ctr_1

#Theoretical probabilities
pr_1 = pr_0 = 0.5

#Display probabilities
print("Theoretical Probabilities:", pr_0, pr_1)
print("Practical Probabilities:", ctr_0/N, ctr_1/N)