def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0b0"
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    return "0b" + binary_number


decimal_number = int(input())
binary_number = decimal_to_binary(decimal_number)
print("Binary representation using custom function:", binary_number)
