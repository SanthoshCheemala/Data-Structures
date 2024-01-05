import numpy as np
from scipy.linalg import lu

n = int(input("Enter the number of rows: "))
mat = []
for i in range(n):
    row = list(map(int, input(f"Enter the {(i+1)}th row: ").split()))
    mat.append(row)
A = np.array(mat)

P, L, U = lu(A.T)

Y = np.eye(A.shape[0])
Y = np.linalg.solve(L, np.dot(P, Y))

inverse_matrix = np.linalg.solve(U, Y)

print("Inverse Matrix:")
print(inverse_matrix.T)
