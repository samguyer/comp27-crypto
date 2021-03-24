import time

# -- Compute the prime factors of an integer n using
#    the naive method (try all the values up to sqrt(n))
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# -- Call factor, and print the amount of time it takes
def time_factor(n):
    print("Factor {}...".format(n))
    t1 = time.time()
    f = prime_factors(n)
    t2 = time.time()
    print("..done in {:1.8f} seconds".format(t2-t1))
    print(f)

# -- Choose a number and factor it
n1 = 3600
time_factor(n1)


