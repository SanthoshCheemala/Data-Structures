def binary_to_hexadecimal(binary_number):
    decimal_number = 0
    binary_digits = str(binary_number)[::-1]  
    for i in range(len(binary_digits)):
        if binary_digits[i] == '1':
            decimal_number += 2 ** i

    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hexadecimal_digits[remainder] + hexadecimal_number
        decimal_number = decimal_number // 16
    
    return "0x" + hexadecimal_number

binary_number = "1010"  
hexadecimal_number = binary_to_hexadecimal(binary_number)
print("Hexadecimal representation:", hexadecimal_number)
