def collinear(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if a == 0:
        print("yes")
    else:
        print("No")

x1, x2, x3, y1, y2, y3 = list(map(int, input().split()))
collinear(x1, y1, x2, y2, x3, y3)
