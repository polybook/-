import math
import numpy as np

f = np.array([[10, 20, 30], [40, 50, 60], [7, 8, 9]])
print(np.linalg.det(f))

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.ones((3,2))
AT = A.transpose()

C = np.dot(A, B.transpose())
print(A)
print(B)

print(C)
print(np.trace(C))

print(np.linalg.matrix_rank(B))