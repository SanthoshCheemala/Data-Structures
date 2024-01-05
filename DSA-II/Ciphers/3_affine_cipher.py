alphabets = "abcdefghijklmnopqrstuvwxyz"


def encrypt(word, akey, mkey):
    res = ""
    for letter in word:
        c = alphabets.index(letter)
        i = (c * mkey + akey) % 26
        res += alphabets[i]
    return res


def decrypt(word, akey, mkey):
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
    res = ""
    if mkey not in inverse:
        return -1
    else:
        inv = inverse[mkey]
        for letter in word:
            c = alphabets.index(letter)
            i = ((c - akey) * inv) % 26
            res += alphabets[i]
    return res


word = input("Enter Word:\t")
akey = int(input("Enter Additive Key:\t"))
mkey = int(input("Enter Multiplicative Key:\t"))

cipher_text = encrypt(word, akey, mkey)
print("Cipher Text : ", cipher_text)
deciphered_text = decrypt(cipher_text, akey, mkey)
print("Deciphered Text : ", deciphered_text)
