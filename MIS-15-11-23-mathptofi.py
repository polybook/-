import matplotlib.pyplot as plt
import math
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.axis('scaled')
plt.xlim(-2, 5)
plt.ylim(-5, 8)


alfa = math.pi / 4
d1, d2 = np.array([2, 2]), np.array([-1, 1])
A = np.array([ d1, d2 ]).transpose()
x, y =  3, -3
v = np.array([x, y])
w = np.dot (A,v)

print (A)

X, Y = w[0], w[1]

ax.arrow(0, 0, X, Y, head_width=0.15, head_length=0.2, length_includes_head=True, facecolor='green')
ax.arrow(0, 0, x, y, head_width=0.15, head_length=0.2, length_includes_head=True, facecolor='black')

plt.show()

A1 = np.linalg.inv(A)
print(np.dot (A1,v))