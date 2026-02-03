# Scalar operation, and relation operations
import numpy as np

# Create two arrays using arange
a = np.arange(1, 6)  # [1 2 3 4 5]
b = np.arange(6, 11) # [6 7 8 9 10]

print("Array a:", a)
print("Array b:", b)
print()

# Scalar (Arithmetic) Operations 
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Modulo (b % a):", b % a)
print("Power (a ** 2):", a ** 2)
print()

#  Relational (Comparison) Operations 
print("a > b :", a > b)       
print("a < b :", a < b)       
print("a == b :", a == b)     
print("a != b :", a != b)     
print("a >= b :", a >= b)    
print("a <= b :", a <= b)     

# Round off operation
div_result = a / b
rounded = np.round(div_result, 2)  # round to 2 decimal places
print("Division rounded to 2 decimals:", rounded)
print()