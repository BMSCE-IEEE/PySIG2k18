import numpy as np

# numpy includes the math library and string library
# Every Object in numpy is an ndarray

# Data types:
# int8, int16, int32, int64 - Also represented as 'i1', 'i2', 'i4', 'i8'
# uint8, uint16, uint32, uint64 - Also represented as 'u1', 'u2', 'u4', 'u8'
# float16, float32, float64 - Also represented as 'f2', 'f4', 'f8'
# complex64, complex128 - complex is internally 2 floats

# Array creation
sample_array = np.empty((3, 3))  # dtype='i2'
print("The Array using empty:\n", sample_array)

sample_array = np.zeros((2, 2))  # dtype='i2'
print("\nThe Array using zeros:\n", sample_array)

sample_array = np.ones((2, 2))  # dtype='i2'
print("\nThe Array using ones:\n", sample_array)

sample_array = np.arange(10, 15, 2)
print("\nThe Array using arange:\n", sample_array)

sample_array = np.linspace(10, 20, 20, False)  # linspace(start, stop, number, endpoint=True, dtype=)
print("\nThe Array using linspace:\n", sample_array)

sample_array = np.array([[1, 2], [3, 4], [5, 6]], dtype='i4')  # order='C' or 'F' for row and column major
print("\nThe Array:\n", sample_array)

# Shape Property
array_shape = sample_array.shape
print("\n\n\nShape of Array:\n", array_shape)

sample_array.shape = (2, 3)
print("\nArray after shape: 2, 3:\n", sample_array)

sample_array = sample_array.reshape((3, 2))
print("\nArray after reshape: 3, 2:\n", sample_array)


# Slicing
sliced_array = sample_array[1: 3 + 1, 1: 2]
print("\nArray after slicing:\n", sliced_array)

# Dimension Property
dimension = sample_array.ndim
print("\nArray Dimension:\n", dimension)

# Item Size Property
byte_size = sample_array.itemsize
print("\nArray Item Size:\n", byte_size)

# Transpose
sample_array_transpose = sample_array.T  # .transpose() also works
print("\nArray Transpose:\n", sample_array_transpose)

# Matrix Multiplication
multiplied_matrix = sample_array_transpose.dot(sample_array)
print("\nMatrix Multiplication:\n", multiplied_matrix)

# Sum of Array
sum = multiplied_matrix.sum()
print("\nSum:\n", sum)
