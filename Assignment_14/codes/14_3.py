#Code by Gautam Singh
#June 8, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Find pdf of np.random.random()

import numpy as np
import matplotlib.pyplot as plt

#Set sample size
sz = 10000000

mu = np.random.random(size=sz)
B = np.linspace(0, 1, 100)
plt.hist(mu, bins=B, density=True)
plt.savefig('../figs/np_random.png')
