# Calculate XOR till n
def calculateXOR(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    elif n % 4 == 3:
        return 0


n = int(input("Enter Number"))
print(f"XOR till {n} is {calculateXOR(n)}")
