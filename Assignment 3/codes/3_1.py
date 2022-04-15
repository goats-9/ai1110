'''
Author: Gautam Singh
Date: April 15, 2022.

-----Documentation-----
This code sorts an unsorted array, and displays it along with the sorted array,
the maximum, minimum, and range of the data.
'''

import numpy as np

A = np.array([55, 36, 95, 73, 60, 42, 25, 78, 75, 62])
A_sort = np.sort(A)
print("The raw data is:", A)
print("The sorted data is:", A_sort)
print("The maximum marks are:", A_sort[-1])
print("The minimum marks are:", A_sort[0])
print("The range of the data is:", A_sort[-1] - A_sort[0])