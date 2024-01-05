import numpy as np


def jacobi_iteration(coeff_matrix, constants, initial_guess, num_iterations):
    num_eq = len(coeff_matrix)
    x = np.array(initial_guess, dtype=float)
    for _ in range(num_iterations):
        x_new = np.zeros_like(x)
        for i in range(num_eq):
            s = sum(coeff_matrix[i][j] * x[j] for j in range(num_eq) if i != j)
            x_new[i] = (constants[i] - s) / coeff_matrix[i][i]
        x = x_new

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
initial_guess_1 = list(map(int, input("Enter the initial guess: ").split()))
num_iterations_1 = int(input("Enter the number of iterations: "))
solution_1 = jacobi_iteration(le, lf, initial_guess_1, num_iterations_1)
solution_1_formatted = [f"x{i+1} = {x:.4f}" for i, x in enumerate(solution_1)]
print(solution_1_formatted)
