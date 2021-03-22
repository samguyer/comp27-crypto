def encrypt(plaintext):
    result = ""
    for c in plaintext:
        if c.isupper():
            result += chr(((ord(c) - 65) + 13) % 26 + 65)
        elif c.islower():
            result += chr(((ord(c) - 97) + 13) % 26 + 97)
        else:
            result += c

    return result

t = input("Enter plaintext: ")
c = encrypt(t)
print("Cypher text: {}".format(c))

