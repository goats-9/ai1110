#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

sz = int(1e3)
randvar = np.loadtxt('ber_gau.dat', dtype='double')
x = np.linspace(0, 1, sz)
plt.plot(x, randvar, 'o')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()
plt.savefig('../figs/wave.png')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
