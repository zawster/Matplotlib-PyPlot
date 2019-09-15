import time
import psutil
import matplotlib.pyplot as plt

%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)

fig.show()
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X = np.linspace(0, 10, 40)
C = np.cos(X)
S = np.sin(X)
T = np.tan(X)

ax.scatter(C, S, T, c='r', marker='o')
ax.scatter(X, S, C, c='g', marker='+')
ax.scatter(S, C, X, c='b', marker='*')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
