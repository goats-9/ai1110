from cmath import atan
import matplotlib.pyplot as plt
import numpy as np
import math

# Function to define arccot using the well-known identity 
# arccot(x) + arctan(x) = pi/2
def arccot(X):
    Y = (math.pi)/2*np.ones(np.size(X)) - np.arctan(X)
    return Y

X = np.linspace(-2, 2, 10000)
plt.plot(X, 3*np.arctan(X) + arccot(X), label = '$y = 3\\tan^{-1}x + \\cot^{-1}x$')
plt.plot(X, math.pi*np.ones(np.size(X)), label = '$y = \\pi$')
plt.plot(1, math.pi, 'ko')
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best', prop={'size':11})
plt.annotate('(1, $\\pi$)', (1, math.pi), xytext=(-20, 10), textcoords='offset points')
plt.savefig('../figs/1_3.png')