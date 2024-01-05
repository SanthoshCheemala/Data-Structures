alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(word, key):
    res = ""
    i = 0
    key_length = len(key)
    for letter in word:
        c = alphabets.index(letter)
        key_ind = alphabets.index(key[i % key_length])
        j = (c + key_ind) % 26
        res += alphabets[j]
        i += 1
    return res


def decrypt(word, key):
    res = ""
    i = 0
    key_length = len(key)
    for letter in word:
        c = alphabets.index(letter)
        key_ind = alphabets.index(key[i % key_length])
        j = (c - key_ind) % 26
        res += alphabets[j]
        i += 1
    return res


word = input("Enter Word:\t")
key = input("Enter Key:\t")
cipher_text = encrypt(word, key)
print("Cipher Text : ", cipher_text)
deciphered_text = decrypt(cipher_text, key)
print("Deciphered Text : ", deciphered_text)
