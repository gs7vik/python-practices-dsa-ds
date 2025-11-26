import numpy as np

# --- CASE 1: 1D VECTORS (Classic Dot Product) ---
v1 = np.array([1, 2])
v2 = np.array([5, 7])

# Result is a SCALAR (single number)
result_1d = np.dot(v1, v2) 
print(f"1D Dot Product (Scalar): {result_1d}") 
# Calculation: (1*5) + (2*7) = 19


# --- CASE 2: 2D MATRICES (Matrix Multiplication) ---
# Notice these are now wrapped in extra brackets [[...]]
m1 = np.array([[1, 2]]) 
m2 = np.array([[5], 
               [7]])

# Result is a MATRIX (2D array)
result_2d = np.dot(m1, m2)
print(f"2D Dot Product (Matrix): \n{result_2d}")
# Calculation is still 19, but wrapped in a 2D shape [[19]]


import numpy as np

# 1. Define the Matrices
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

# ---------------------------------------------------------

# 2. Matrix Multiplication (Three ways to write it)
# The '@' symbol is the standard operator for matmul in Python
matmul_result = A @ B      
# OR: np.matmul(A, B)

print(f"Matrix Multiplication (A @ B):\n{matmul_result}\n")

# ---------------------------------------------------------

# 3. Element-wise Multiplication (Just Mul)
# The '*' symbol does element-by-element multiplication
elementwise_result = A * B 
# OR: np.multiply(A, B)

print(f"Element-wise Multiplication (A * B):\n{elementwise_result}\n")

# ---------------------------------------------------------

# 4. Dot Product
# For 2D arrays, this is exactly the same as MatMul
dot_result = np.dot(A, B)

print(f"Dot Product (np.dot):\n{dot_result}")