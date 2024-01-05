def graycode(n):

    if n == 2:
        return ["00","01","11","10"]
    else:
        temp = graycode(n-1)
        return ["0"+x for x in temp] + ["1"+x for x in temp[::-1]]

print(graycode(4))