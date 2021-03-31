import math


# -- Compute the modular inverse of a number a for modulus m
def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x


# -- Generate an RSA key pair given two primes, p and q
def generate():
    # -- Pick two prime numbers, p and q
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))

    # -- The modulus n is the product
    n = p * q

    # -- Compute lambda(n), the Carmichael function
    #    Since p and q are prime, lambda(n) = lcm(p-1, q-1)
    #    lcm(p-1, q-1) = (p-1)*(q-1) / gcd(p-1, q-1)
    g = math.gcd(p-1,q-1)
    lam_n = ((p-1) * (q-1)) // g

    # -- Choose a small value, less than lam_n, that is
    #    relatively prime to lam_n (that is, the only
    #    prime factor they share is 1)

    # Hopefully, one of these values works!
    e_values = [5,7,11,13,3,17]
    for e in e_values:
        if e < lam_n and lam_n % e == 1:
            break

    # -- Now compute a value d, such that d * e = 1 mod lam_n
    d = mod_inverse(e, lam_n)

    # -- This is too slow
    #for d in range(1,lam_n):
    #    if ((d*e) % lam_n) == 1:
    #        break

    print("p = {}  q = {}  n = {}  lam_n = {}  e = {}  d = {}".format(p, q, n, lam_n, e, d))

    return (e, n, d)


# -- Encrypt a message using the given public key (e,n)
def encrypt(e, n):
    # -- Get a secret message to encrypt:
    m = input("Enter secret message: ")
    v = 0
    for x in m:
        v = v << 8
        v = v + ord(x)

    print("Value to encrypt: {}".format(v))

    # Encrypt: Compute m^e mod n
    ct = pow(v, e, n)
    print("Cypher text (value): {}".format(ct))

    return ct


# -- Decrypt a message using the private key (d,n)
def decrypt(d, n):

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

# -----------------
#  Main program
# -----------------

done = False
has_key = False
e = 0
d = 0
n = 0
while not done:
    print("Choose:")
    print("1 -- generate RSA key pair")
    print("2 -- encrypt a message")
    print("3 -- decrypt a message")
    print("Any other value to exit.")
    choice = input(">")
    if choice == '1':
        (e, n, d) = generate()
        print("Public key: ({}, {})".format(e, n))
        print("Private key: {}".format(d))
        has_key = True
    elif choice == '2':
        if has_key:
            encrypt(e, n)
        else:
            print("ERROR: Generate a key pair first")
    elif choice == '3':
        if has_key:
            decrypt(d, n)
        else:
            print("ERROR: Generate a key pair first")
    else:
        done = True
