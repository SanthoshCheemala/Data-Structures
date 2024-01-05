def encrypt(word, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for letter in word:
        c = alphabets.index(letter)
        i = (c * key) % 26
        res += alphabets[i]
    return res


def decrypt(word, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    inverse = {
        1: 1,
        3: 9,
        5: 21,
        7: 15,
        9: 3,
        11: 19,
        15: 7,
        17: 23,
        19: 11,
        21: 5,
        23: 17,
        25: 25,
    }
    keys = inverse.keys()
    if key % 26 not in keys:
        return -1
    else:
        a = key % 26
        inv = inverse[a]
        for letter in word:
            c = alphabets.index(letter)
            i = (c * inv) % 26
            res += alphabets[i]
    return res


word = input("Enter Word:\t")
key = int(input("Enter Key:\t"))
cipher_text = encrypt(word, key)
print("Cipher Text : ", cipher_text)
deciphered_text = decrypt(cipher_text, key)
print("Deciphered Text : ", deciphered_text)
