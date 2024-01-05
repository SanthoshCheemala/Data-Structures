import numpy as np

def gaussian_elimination_with_numpy(coefficients, constants):
    A = np.array(coefficients)
    b = np.array(constants)
    solutions = np.linalg.solve(A, b)
    return solutions.tolist()


n = int(input("Enter the number of equations: "))
le = []
lf = []
for i in range(n):
    li = list(
        map(int, input(f"Enter the co-effiecients of the {(i+1)}th equation: ").split())
    )
    lz = int(input(f"Enter the constant of the {(i+1)}th equation: "))
    le.append(li)
    lf.append(lz)
print(le, lf)
solution_1 = gaussian_elimination_with_numpy(le, lf)
print(solution_1)
