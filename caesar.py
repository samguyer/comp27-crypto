def encrypt(plaintext, shift):
    result = ""
    for c in plaintext:
        if c.isupper():
            result += chr(((ord(c) - 65) + shift) % 26 + 65)
        elif c.islower():
            result += chr(((ord(c) - 97) + shift) % 26 + 97)
        else:
            result += c

    return result


# --- Test it out here

#t = input("Enter plaintext: ")
#s = int(input("Enter shift: "))
#c = encrypt(t, s)
#print("Cypher text: {}".format(c))

ct = "nkmdibdnczmz"
for i in range(1,26):
    print("{} {}".format(i, encrypt(ct, i)))
