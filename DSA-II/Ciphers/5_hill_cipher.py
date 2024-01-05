import numpy as np
def create_digraph(text, key):
    n = int(len(key)**0.5)
    no_space = text.replace(" ", "")
    digraphs = [no_space[i:i+n] for i in range(0, len(no_space), n)]
    return digraphs
def create_plaintext_column(digraph):
    return [[ord(char) - 65] for char in digraph]
def create_key_matrix(key):
    n = int(len(key)**0.5)
    key_matrix = np.array([ord(char) - 65 for char in key]).reshape((n, n))
    return key_matrix

def encrypt(plaintext, key):
    key_matrix = create_key_matrix(key)
    digraphs = create_digraph(plaintext, key)

    encrypted_text = ""

    for digraph in digraphs:
        plaintext_column = np.array(create_plaintext_column(digraph))
        result_matrix = np.dot(key_matrix,plaintext_column) % 26

        for i in range(result_matrix.shape[0]):
            encrypted_text += chr(result_matrix[i, 0] + 65)

    return encrypted_text

def decrypt(ciphertext, key):
    key_matrix = create_key_matrix(key)
    if np.linalg.det(key_matrix) == 0:
        raise ValueError("The key matrix is not invertible. Choose a different key.")

    digraphs = create_digraph(ciphertext, key)

    decrypted_text = ""

    for digraph in digraphs:
        ciphertext_column = np.array(create_plaintext_column(digraph))
        result_matrix = np.dot(np.linalg.inv(key_matrix), ciphertext_column) % 26

        for i in range(result_matrix.shape[0]):
            decrypted_text += chr(int(result_matrix[i, 0]) % 26 + 65)

    return decrypted_text


message = input("Enter message: ").upper()
key = input("Enter key: ").upper()

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypt(encrypted_message, key))