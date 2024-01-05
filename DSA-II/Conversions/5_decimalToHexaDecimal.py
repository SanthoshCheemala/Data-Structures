
def decimal_to_hexadecimal(decimal_number):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_number = ""

    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hexadecimal_digits[remainder] + hexadecimal_number
        decimal_number = decimal_number // 16

    return "0x" + hexadecimal_number


decimal_number = 42  
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print("Hexadecimal representation using custom function:", hexadecimal_number)
