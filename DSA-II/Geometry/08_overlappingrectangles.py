def overlappingArea(l1, r1, l2, r2):
	x = 0
	y = 1
	area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])

	area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])
	x_dist = (min(r1[x], r2[x]) -max(l1[x], l2[x]))

	y_dist = (min(r1[y], r2[y]) -max(l1[y], l2[y]))
	areaI = 0
	if x_dist > 0 and y_dist > 0:
		areaI = x_dist * y_dist

	return (area1 + area2 - areaI)

l1 = [2, 2]
r1 = [5, 7]
l2 = [3, 4]
r2 = [6, 9]

print(overlappingArea(l1, r1, l2, r2))

