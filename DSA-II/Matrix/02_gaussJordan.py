import numpy as np
def gauss_jordan_method(coeff_matrix, const_vector):
    A = np.array(coeff_matrix, dtype=float)
    b = np.array(const_vector, dtype=float)
    aug_matrix = np.hstack((A, b.reshape(-1, 1)))

    num_eq = len(coeff_matrix)
    for i in range(num_eq):
        aug_matrix[i] = aug_matrix[i] / aug_matrix[i, i]
        for j in range(num_eq):
            if i != j:
                aug_matrix[j] -= aug_matrix[j, i] * aug_matrix[i]
    solutions = aug_matrix[:, -1]
    return solutions


def format_solution(solution):
    return ["x{} = {:.1f}".format(i + 1, val) for i, val in enumerate(solution)]


n = int(input("Enter the number of equations: "))
le = []
lf = []
for i in range(n):
    li = list(
        map(int, input(f"Enter the co-efficients of the {(i+1)}the equation: ").split())
    )
    lz = eval(input(f"Enter the constants of the {(i+1)}th equation: "))
    le.append(li)
    lf.append(lz)
gauss_jordan_solutions = []
solution = gauss_jordan_method(le, lf)
gauss_jordan_solutions.append(format_solution(solution))
print(gauss_jordan_solutions)
