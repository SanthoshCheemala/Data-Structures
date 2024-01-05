import numpy as np
import math


def extend_plaintext(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    n = len(key)
    l = len(plaintext)
    remainder = l % n

    if remainder != 0:
        to_add = n - remainder
        plaintext += "X" * to_add

    return plaintext


def create_plaintext_matrix(plaintext, key):
    n = len(key)
    plaintext = extend_plaintext(plaintext, key)
    rows = len(plaintext) // n  # Use integer division to determine the number of rows
    plaintext_matrix = np.array([char for char in plaintext]).reshape((rows, n))
    return plaintext_matrix


def encrypt(plaintext, key):
    e_plaintext = extend_plaintext(plaintext, key)
    plaintext_matrix = create_plaintext_matrix(e_plaintext, key)

    transposed_matrix = plaintext_matrix.T

    d = {}

    for i in range(len(key)):
        d[key[i]] = transposed_matrix[i]

    sorted_d = sorted(d.items())
    encrypted_matrix = np.array([value for key, value in sorted_d])

    encrypted_text = ""

    for i in range(encrypted_matrix.shape[0]):
        for j in range(encrypted_matrix.shape[1]):
            encrypted_text += encrypted_matrix[i][j]

    return encrypted_text


# Example usage:
plain_text = input("Enter message: ")
key = input("Enter key: ")
print("Encrypted Text: ", encrypt(plain_text, key))
