from sympy import *

M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 
print(f"Matrix : {M} ") 

M_rref = M.rref() 
	
print(f"The Row echelon form of matrix M and the pivot columns:{M_rref[0]}")