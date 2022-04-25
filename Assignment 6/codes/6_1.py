#Code by Gautam Singh
#April 25, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To compute the probability regarding the sum
#of two die given a tablular input of the 
#possible outcomes.

import numpy as np
import pandas as pd

#Import Data
df = pd.read_excel('../tables/intab.xlsx', 'Sheet1')
A = df.to_numpy()

#Number of possible outcomes
N = 36

#Number of favourable probabilities
x_0 = np.count_nonzero(A % 2 == 0)
x_1 = np.count_nonzero(A == 6)
x_2 = np.count_nonzero(A >= 6)

#Compute theoretical probabilities
p_0 = x_0/N
p_1 = x_1/N
p_2 = x_2/N

#Display theoretical probabilities
print("Theoretical probabilities: ", p_0, p_1, p_2)