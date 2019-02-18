# Author: K Nitesh Srivats
import numpy as np

matrix = np.load("Matrix.npy")
window = np.load("Window3.npy")
pool_size = int(input("Enter Pool Size: "))
size = len(matrix)
window_size = window.shape[0]
result = np.zeros((size - window_size + 1, size - window_size + 1))
# Convolution
for i in range(size - window_size + 1):
    for j in range(size - window_size + 1):
        for k in range(window_size):
            for l in range(window_size):
                result[i][j] += window[k][l] * matrix[i + k][j + l]
print(result)
# Max Pooling
pool_result = np.empty(
    (int(result.shape[0] / pool_size), int(result.shape[0] / pool_size)))
for i in range(pool_result.shape[0]):
    for j in range(pool_result.shape[0]):
        pool_result[i][j] = np.amax(result[i * pool_size: (i + 1) * pool_size,
                                    j * pool_size: (j + 1) * pool_size])
print(pool_result)
