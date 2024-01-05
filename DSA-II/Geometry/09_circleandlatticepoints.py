import math
def countLattice(r):

	if (r <= 0):
		return 0
	result = 4
	for x in range(1, r):
		ySquare = r*r - x*x 
		y = int(math.sqrt(ySquare)) 
		if (y*y == ySquare):
			result += 4
	return result 
r = int(input())
print(countLattice(r)) 