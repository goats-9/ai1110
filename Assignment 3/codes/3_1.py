'''
Author: Gautam Singh.
Date: April 15, 2022.

-----Documentation-----
This code sorts an unsorted array, and displays it along with the sorted array,
the maximum, minimum, and range of the data.
'''

import numpy as np
import pandas as pd

df = pd.read_excel('../tables/raw.xlsx', 'Sheet1')
A = df.columns.to_numpy()
A_srt = np.sort(A)
df_srt = pd.DataFrame(A_srt)
df_srt = df_srt.transpose()
df_srt.to_excel('../tables/sort.xlsx', header=False, index=False)