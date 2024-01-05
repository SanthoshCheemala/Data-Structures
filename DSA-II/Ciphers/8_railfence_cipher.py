def plaintext_s(plaintext):
    plaintext = plaintext.upper().replace(" ", "")
    return plaintext


def encrypt(plaintext):
    plaintext = plaintext_s(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ciphertext += plaintext[i]

    for i in range(1, len(plaintext), 2):
        ciphertext += plaintext[i]

    return ciphertext


def decrypt(encrypted):
    plaintext = [""] * len(encrypted)

    for i in range(len(encrypted)):
        if i % 2 == 0:
            plaintext[i] = encrypted[i // 2]
        else:
            plaintext[i] = encrypted[len(encrypted) // 2 + i // 2]

    return "".join(plaintext)


print(encrypt("nothing is as it seems"))
print(decrypt(encrypt("nothing is as it seems")))
