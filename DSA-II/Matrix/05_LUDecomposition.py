import numpy as np
from scipy.linalg import lu_factor, lu_solve


def lu_decomposition(coeff_matrix, const_vector):
    A = np.array(coeff_matrix, dtype=float)
    b = np.array(const_vector, dtype=float)
    lu, piv = lu_factor(A)
    x = lu_solve((lu, piv), b)
    return x


n = int(input("Enter the number of equations: "))
le = []
lf = []
for i in range(n):
    li = list(
        map(int, input(f"Enter the co-efficients of the {(i+1)}th equation: ").split())
    )
    lz = eval(input(f"Enter the constants of the {(i+1)}th equation: "))
    le.append(li)
    lf.append(lz)
solution = lu_decomposition(le, lf)
solution_formatted = [f"x{i+1}={x}" for i, x in enumerate(solution)]
print(solution_formatted)
