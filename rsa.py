import math

# -- Pick two prime numbers, p and q
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

# -- The modulus n is the product
n = p * q

# -- Compute lambda(n), the Carmichael function
#    Since p and q are prime, lamba(n) = lcm(p-1, q-1)
#    lcm(p-1, q-1) = (p-1)*(q-1) / gcd(p-1, q-1)
g = math.gcd(p-1,q-1)
lam_n = ((p-1) * (q-1)) // g

# -- Choose a small value, less than lam_n, that is
#    relatively prime to lam_n (that is, the only
#    prime factor they share is 1)
e = 5
if lam_n % e == 0:
    print("BAD e value {}".format(e))

# -- Now compute a value d, such that d * e = 1 mod lam_n
for d in range(1,lam_n):
    if ((d*e) % lam_n) == 1:
        break

print("p = {}  q = {}  n = {}  lam_n = {}  e = {}  d = {}".format(p, q, n, lam_n, e, d))


c = int(input("Enter 1 to encrupt, 2 to decrypt: "))
if c == 1:

    # -- Get a secret message to encrypt:
    m = input("Enter secret message (short!): ")
    v = 0
    for x in m:
        v = v << 8
        v = v + ord(x)

    print("Value to encrypt: {}".format(v))

    # Encrypt: Compute m^e mod n
    ct = pow(v, e, n)
    print("Cypher value: {}".format(ct))

if c == 2:

    # -- Get cyphertext
    ct = int(input("Enter cypher value to decrypt: "))

    # Decrypt: Compute ct^d mod n
    pt = pow(ct,d,n)

    print("Decrypted value: {}".format(pt))

    m = ""
    while pt > 0:
        ptc = pt & 0xFF
        m = m + chr(ptc)
        pt = pt >> 8

    # -- Need to reverse the string
    m = m[::-1]

    print("Decrypted message: {}".format(m))

