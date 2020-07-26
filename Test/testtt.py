import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = 2*x + 1
y2 = 3*x - 5

plt.plot(x,y1, 'o-', lw=6, ms=14)
plt.plot(x,y2, 'o', ms=14, markerfacecolor="None",
         markeredgecolor='red', markeredgewidth=5)

plt.show()