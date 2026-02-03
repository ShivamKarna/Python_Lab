# This is of Feb 3 1:30 PM

import numpy as np

#  Create a NumPy array of floats
arr = np.array([1, 2, 3, 4], dtype=float)
print("Array as floats:")
print(arr)
print("Data type:", arr.dtype)
print()

# Create an array of odd numbers from 1 to 10 using arange
a = np.arange(1, 21, 2)   
print("Odd numbers from 1 to 10:")
print(a)
print()

# Create an array of numbers 0-15 and reshape it to 4x4
b = np.arange(16).reshape(4, 4)
print("Numbers 0-15 reshaped to 4x4:")
print(b)
