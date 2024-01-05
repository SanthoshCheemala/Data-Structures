def encrypt(word, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for letter in word:
        c = alphabets.index(letter)
        i = (c + key) % 26
        res += alphabets[i]
    return res


def decrypt(word, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for letter in word:
        c = alphabets.index(letter)
        i = (c - key) % 26
        res += alphabets[i]
    return res


word = input("Enter Word:\t")
key = int(input("Enter Key:\t"))
cipher_text = encrypt(word, key)
print("Cipher Text : ", cipher_text)
deciphered_text = decrypt(cipher_text, key)
print("Deciphered Text : ", deciphered_text)
