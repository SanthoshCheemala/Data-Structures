import numpy as np
def gauss_jordan(matrix):
    size = len(matrix)
    augmented_matrix = np.hstack((matrix, np.eye(size)))
    for i in range(size):
        a = augmented_matrix[i][i]
        if a == 0:
            for j in range(i+1, size):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
            a = augmented_matrix[i][i]
            if a == 0:
                raise ValueError("Matrix is singular and cannot be inverted.")
        for j in range(2*size):
            augmented_matrix[i][j] /= a
        for k in range(size):
            if k != i:
                b = augmented_matrix[k][i]
                for j in range(2*size):
                    augmented_matrix[k][j] -= b * augmented_matrix[i][j]
    inverse_matrix = augmented_matrix[:, size:]
    return inverse_matrix
def get_inverse_or_message(matrix):
    try:
        inverse_matrix = gauss_jordan(matrix)
        return inverse_matrix
    except ValueError as e:
        return str(e)
    
n = int(input('Enter the number of rows: '))
mat = []
for i in range(n):
    le = list(map(int, input(f'Enter the {(i+1)}th rows: ').split()))
    mat.append(le)
matrix = np.array(mat)
result = get_inverse_or_message(matrix)
if isinstance(result, np.ndarray):
    print("The inverse matrix is:")
    print(result)
else:
    print(result)
