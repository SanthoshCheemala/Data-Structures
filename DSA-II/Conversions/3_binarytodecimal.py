def binary_to_decimal(binary_number):
    decimal_number = 0
    binary_digits = str(binary_number)[::-1]

    for i in range(len(binary_digits)):
        if binary_digits[i] == "1":
            decimal_number += 2**i

    return decimal_number


binary_number = input() # string "101001010"
decimal_number = binary_to_decimal(binary_number)
print("Decimal representation:", decimal_number)
