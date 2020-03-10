

#Original file is located at
 #   https://colab.research.google.com/drive/1F4h7OwUCxa09l-WFXdXCBiYHYkzIZhXH
"""

import sys


def shiftEncrypt(contents, s):
    result = ""

    # traverse text 
    for i in range(len(contents)):
        char = contents[i]

        # Encrypt uppercase characters 
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def shiftDecrypt(contents, s):
    result = ""

    # traverse text 
    for i in range(len(contents)):
        char = contents[i]

        # Encrypt uppercase characters 
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


def shift(op, input, out, key):
    key = int(key)
    f = open(input, "r")


if f.mode == 'r':
    text = f.read()
    if (op == "decrypt"):
        if (f.mode == 'w'):
            f.write(shiftDecrypt(text, key))
            f.close()
elif (op == "encrypt"):
    if f.mode == 'w':
        f.write(shiftEncrypt(text, key))
        f.close()
    f.close()

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


def affineDec(contents, key1, key2):
    inversekey1 = 0
    for i in range(26):
        if (key1 * i % 26 == 1):
            inversekey1 = i
            break
        # decipher
    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha():
            plaintext += I2L[(inv_a * (L2I[c] - b)) % 26]
        else:
            plaintext += c
    return plaintext


L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


def affineEnc(contents, key1, key2):
    ciphertext = ""

    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += I2L[(L2I[c] * a + b) % 26]
    else:
        ciphertext += c

    return ciphertext


def affine(op, input, out, key1, key2):
    keya = int(key1)
    keyb = int(key2)
    f = open(input, "r")
    if f.mode == 'r':
        text = f.read()
    f.close()


if (op == "decrypt"):

    f = open(out, "w")
    if f.mode == 'w':
        f.write(affineDec(text, keya, keyb))
        f.close()

    elif (op == "encrypt"):
        if f.mode == 'w':
            f.write(affineEnc(text, keya, keyb))
            f.close()


def vigenereEnc(contents, key):
    cipher_text = []
    for i in range(len(contents)):
        x = (ord(contents[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


def vigenereDec(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

    def generateKey(text, key):
        key = list(key)
        if len(text) == len(key):
            return (key)
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))


def vigenere(op, input, out, key):
    f = open(input, "r")
    if f.mode == 'r':
        text = f.read()
    f.close()

    key = generateKey(text, key)
    if (op == "decrypt"):
        f = open(out, "w")
        if f.mode == 'w':
            f.write(vigenereDec(text, key))
            f.close()
    elif (op == "encrypt"):
        if f.mode == 'w':
            f.write(vigenereEnc(text, key))
            f.close()


def main(agr):
    if arg[1] == "shift":
        operation, inputFile, outFile, key = argv[2:]
        shift(operation, inputFile, outFile, key)
    elif arg[1] == "affine":
        operation, inputFile, outFile, key1, key2 = argv[2:]
        affine(operation, inputFile, outFile, key1, key2)
    elif argv[1] == "vigenere":
        operation, inputFile, outFile, key = argv[2:]
        vigenere(operation, inputFile, outFile, key)


main(sys.argv)
