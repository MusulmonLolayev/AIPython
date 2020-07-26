import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [2, 5, 8]
Z = [6, 4, 5]
colors=["#0000FF", "#00FF00", "#FF0066"]

fig = plt.figure()
ax = fig.add_subplot(111)

import random
r = lambda: random.randint(0,255)
print('#%02X%02X%02X' % (r(),r(),r()))


for i in range(100):
    ax.scatter(X[i], Y[i], Z[i], color=colors[i])
plt.show()