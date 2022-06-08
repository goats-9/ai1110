#Code by Gautam Singh
#June 8, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Plot the region where the null hypothesis is rejected

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

#Set up plots of standard normals
mu_0 = 0
mu_1 = 3
z = norm.ppf(0.99)
sigma = 1
X_0 = np.linspace(mu_0 - 3*sigma, mu_0 + 3*sigma, 10000)
X_1 = np.linspace(mu_1 - 3*sigma, mu_1 + 3*sigma, 10000)
plt.plot(X_0, norm.pdf(X_0, mu_0, sigma), 'b-')
plt.plot(X_1, norm.pdf(X_1, mu_1, sigma), 'g-')
plt.grid()
plt.axhline(y=0, c="black")
plt.axvline(x=0, c="black")
plt.xlabel("x")
plt.ylabel("$p_{X}(x)$")
plt.annotate("$Z_{0.99}$", (z, 0), textcoords="offset points", xytext=(0, -10), ha="center")
X_t = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
plt.xticks(X_t)

#Shade the region where null hypothesis
#is accepted
X_fill = np.linspace(z, mu_1 + 3*sigma, 10000)
plt.fill_between(X_fill, norm.pdf(X_fill, mu_1, sigma))
#Border line
plt.plot([z, z], [0, norm.pdf(z, mu_1, sigma)], 'k-')

plt.legend(['$X_1 \sim N(0, 1)$', '$X_2 \sim N(3, 1)$'], loc='best')
plt.savefig('../figs/14_1.png')
