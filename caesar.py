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

t = input("Enter plaintext: ")
s = int(input("Enter shift: "))
c = encrypt(t, s)
print("Cypher text: {}".format(c))

