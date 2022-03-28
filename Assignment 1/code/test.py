import matplotlib.pyplot as plt
import numpy as np

x = [2, 0, 2, 0, -2, -2]
y = [2, -1, -2, 1, 2, -2]
t = ["A", "C", "B", "D", "A'", "B'"]
fig, ax = plt.subplots()
ax.plot(x, y, '.k')
x_l = [0, 2, 2, 0, -2, -2, 0, 0]
y_l = [1, 2, -2, -1, -2, 2, 1, -1]
ax.plot(x_l, y_l, 'k-')
for i in range(6):
    ax.annotate(t[i], (x[i], y[i]))
ax.grid()
fig.savefig("../figs/graph.png")
plt.show()