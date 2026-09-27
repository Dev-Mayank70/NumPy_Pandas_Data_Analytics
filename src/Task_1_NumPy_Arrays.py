import numpy as np

# NumPy array containing 10 numbers
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("NumPy Array:")
print(numbers)

print("\nShape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

# One-dimensional array
one_dimensional = np.array([1, 2, 3, 4, 5])

print("\nOne-Dimensional Array:")
print(one_dimensional)

# Two-dimensional array
two_dimensional = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTwo-Dimensional Array:")
print(two_dimensional)

print("Shape of 2D Array:", two_dimensional.shape)