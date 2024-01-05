def prepare_input(text):
    text = text.upper().replace("J", "I")

    digraphs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            digraphs.append(text[i] + "X")
            i += 1
        else:
            digraphs.append(text[i] + text[i + 1])
            i += 2

    return digraphs


def create_cipher_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    key = key.upper().replace("J", "I")
    for char in key:
        if char not in table:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    cipher_table = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(table[i * 5 + j])
        cipher_table.append(row)

    return cipher_table


def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j

    return x, y


def encrypt(message, key):
    cipher_table = create_cipher_table(key)
    digraphs = prepare_input(message)
    ciphertext = []
    for digraph in digraphs:
        pos1 = find_position(cipher_table, digraph[0])
        pos2 = find_position(cipher_table, digraph[1])
        if pos1[0] == pos2[0]:
            if pos1[1] == 4:
                pos1 = (pos1[0], 0)
            if pos2[1] == 4:
                pos2 = (pos2[0], 0)
            ciphertext.append(cipher_table[pos1[0]][pos1[1] + 1])
            ciphertext.append(cipher_table[pos2[0]][pos2[1] + 1])
        elif pos1[1] == pos2[1]:
            if pos1[0] == 4:
                pos1 = (0, pos1[1])
            if pos2[0] == 4:
                pos2 = (0, pos2[1])
            ciphertext.append(cipher_table[pos1[0] + 1][pos1[1]])
            ciphertext.append(cipher_table[pos2[0] + 1][pos2[1]])
        else:
            ciphertext.append(cipher_table[pos1[0]][pos2[1]])
            ciphertext.append(cipher_table[pos2[0]][pos1[1]])

    return "".join(ciphertext)


def decrypt(message, key):
    cipher_table = create_cipher_table(key)
    digraphs = prepare_input(message)
    plaintext = []
    for digraph in digraphs:
        pos1 = find_position(cipher_table, digraph[0])
        pos2 = find_position(cipher_table, digraph[1])
        if pos1[0] == pos2[0]:
            if pos1[1] == 0:
                pos1 = (pos1[0], 5)
            if pos2[1] == 0:
                pos2 = (pos2[0], 5)
            plaintext.append(cipher_table[pos1[0]][pos1[1] - 1])
            plaintext.append(cipher_table[pos2[0]][pos2[1] - 1])
        elif pos1[1] == pos2[1]:
            if pos1[0] == 0:
                pos1 = (5, pos1[1])
            if pos2[0] == 0:
                pos2 = (5, pos2[1])
            plaintext.append(cipher_table[pos1[0] - 1][pos1[1]])
            plaintext.append(cipher_table[pos2[0] - 1][pos2[1]])
        else:
            plaintext.append(cipher_table[pos1[0]][pos2[1]])
            plaintext.append(cipher_table[pos2[0]][pos1[1]])

    return "".join(plaintext)


message = input("Enter message: ")
keyword = input("Enter keyword: ")

print("Encrypted message: ", encrypt(message, keyword))
print("Decrypted message: ", decrypt(encrypt(message, keyword), keyword))
