class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
def gcd(a, b):
	if (b == 0):
		return a 
	return gcd(b, a % b)
def getBoundaryCount(p, q):
	
	if (p.x == q.x): 
		return abs(p.y - q.y) - 1
	if (p.y == q.y): 
		return abs(p.x - q.x) - 1

	return gcd(abs(p.x - q.x), 
			abs(p.y - q.y)) - 1

def getInternalCount(p, q, r):

	BoundaryPoints = (getBoundaryCount(p, q) +getBoundaryCount(p, r) +getBoundaryCount(q, r) + 3)
	doubleArea = abs(p.x * (q.y - r.y) +q.x * (r.y - p.y) +r.x * (p.y - q.y)) 
	return (doubleArea - BoundaryPoints + 2) // 2
	
p = Point(0, 0) 
q = Point(5, 0) 
r = Point(0, 5)
	
print("Number of integral points inside given triangle is ",getInternalCount(p, q, r)) 
