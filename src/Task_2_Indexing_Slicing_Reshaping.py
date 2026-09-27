import numpy as np

# Original 1D array
array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(array)

# Indexing
print("\nElement at index 0:", array[0])
print("Element at index 4:", array[4])
print("Last element:", array[-1])

# Slicing
print("\nElements from index 2 to 6:")
print(array[2:7])

print("\nFirst five elements:")
print(array[:5])

# 2D array
two_d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(two_d)

# Access rows
print("\nFirst Row:")
print(two_d[0])

print("\nSecond Row:")
print(two_d[1])

# Access columns
print("\nFirst Column:")
print(two_d[:, 0])

print("\nSecond Column:")
print(two_d[:, 1])

# Reshaping
reshaped = array.reshape(2, 5)

print("\nReshaped Array (2 x 5):")
print(reshaped)

reshaped_again = array.reshape(5, 2)

print("\nReshaped Array (5 x 2):")
print(reshaped_again)