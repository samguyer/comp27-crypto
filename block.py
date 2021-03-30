

def encrypt(plaintext, key):
    result = []
    l = len(plaintext)
    plaintext += "    "
    for i in range(0,l,4):
        # -- Process the plain text in "blocks" (four character chunks)
        pb = plaintext[i:i+4]
        # -- First, perform a Caesar cypher with shift 10
        ct1 = subst(pb, 10)
        # -- Second, combine the four characters into a 32-bit number,
        #    but rearrange the bytes: instead of 0123, use 1032
        ct2 = (ord(ct1[1]) << 24) + (ord(ct1[0]) << 16) + (ord(ct1[3]) << 8) + ord(ct1[2])
        # -- XOR the key value
        ct3 = ct2 ^ key
        # -- Extract the four bytes
        cc0 = (ct3 >> 24) & 0xFF
        cc1 = (ct3 >> 16) & 0xFF
        cc2 = (ct3 >> 8) & 0xFF
        cc3 = ct3 & 0xFF
        # -- Convert the bytes back into characters
        result.append(chr(cc0))
        result.append(chr(cc1))
        result.append(chr(cc2))
        result.append(chr(cc3))

    s = ''
    return s.join(result)


def decrypt(cyphertext, key):
    result = []
    l = len(cyphertext)
    for i in range(0,l,4):
        # -- Take a block of cypher text
        cb = cyphertext[i:i+4]
        # -- Assemble them into a 32-bit number
        ct3 = (ord(cb[0]) << 24) + (ord(cb[1]) << 16) + (ord(cb[2]) << 8) + ord(cb[3])
        # -- XOR the key
        ct2 = ct3 ^ key
        # -- Extract the four bytes
        cc0 = (ct2 >> 24) & 0xFF
        cc1 = (ct2 >> 16) & 0xFF
        cc2 = (ct2 >> 8) & 0xFF
        cc3 = ct2 & 0xFF
        # -- Rearrange them, reversing the permutation performed in encrypt
        ct1 = chr(cc1) + chr(cc0) + chr(cc3) + chr(cc2)
        # -- Undo the Caesar cypher by applying it again with shift 16
        pb = subst(ct1, 16)
        result.append(pb)

    s = ''
    return s.join(result)


# -- Caesar cypher
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

# --- Test it out here

pt = input("Enter plaintext: ")
key = int(input("Enter key:"))
ct = encrypt(pt, key)
print("Encrypted: {}".format(ct))

de = decrypt(ct, key)
print("Decrypted: {}".format(de))
