import numpy as np

a, b, c = 4, 7, 3

A = (np.random.random_sample(28)*10).reshape((a, b))
B = (np.random.random_sample(21)*10).reshape((b, c))

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

C = np.empty((a, c), dtype='f2')
for k in range(b):
    for j in range(c):
        for i in range(a):
            C[i][j] += A[i][k] * B[k][j]
print("\nMatrix C:\n", C)
