

def encrypt(plaintext, key):
    result = []
    l = len(plaintext)
    plaintext += "    "
    for i in range(0,l,4):
        pb = plaintext[i:i+4]
        ct1 = subst(pb, 10)
        ct2 = (ord(ct1[1]) << 24) + (ord(ct1[0]) << 16) + (ord(ct1[3]) << 8) + ord(ct1[2])
        ct3 = ct2 ^ key
        cc0 = (ct3 >> 24) & 0xFF
        cc1 = (ct3 >> 16) & 0xFF
        cc2 = (ct3 >> 8) & 0xFF
        cc3 = ct3 & 0xFF
        result.append(chr(cc0))
        result.append(chr(cc1))
        result.append(chr(cc2))
        result.append(chr(cc3))

    return result


def decrypt(cyphertext, key):
    result = []
    l = len(cyphertext)
    for i in range(0,l,4):
        cb = cyphertext[i:i+4]
        ct3 = (ord(cb[0]) << 24) + (ord(cb[1]) << 16) + (ord(cb[2]) << 8) + ord(cb[3])
        ct2 = ct3 ^ key
        cc0 = (ct2 >> 24) & 0xFF
        cc1 = (ct2 >> 16) & 0xFF
        cc2 = (ct2 >> 8) & 0xFF
        cc3 = ct2 & 0xFF
        ct1 = chr(cc1) + chr(cc0) + chr(cc3) + chr(cc2)
        pb = subst(ct1, 16)
        result += pb

    return result


def subst(block, shift):
    result = ""
    for c in block:
        if c.isupper():
            result += chr(((ord(c) - 65) + shift) % 26 + 65)
        elif c.islower():
            result += chr(((ord(c) - 97) + shift) % 26 + 97)
        else:
            result += c

    return result


pt = input("Enter plaintext: ")
key = int(input("Enter key:"))
ct = encrypt(pt, key)
de = decrypt(ct, key)
print("Encrypted: {}".format(ct))
print("Decrypted: {}".format(de))
