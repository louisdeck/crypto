# Simple RSA implementation, not secure at all!
# (n,e) = public key
# (d) = private key

import sys

e = 65537

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def keygen():
    p = int(input("Choose a prime number p (1999): ") or 1999)
    q = int(input("Choose a prime number q (2011): ") or 2011)

    if(isPrime(p) and isPrime(q)):
        n = p * q
        phi = (p-1) * (q-1)
        d = pow(e,-1,phi)
        return n, d;

    else: sys.exit("2 primes required, exiting.")

def encrypt(n):
    m1_ciph = []
    m1 = str(input("What message would you like to encrypt? "))

    for i in m1:
        m1_ciph.append(pow(ord(i), e, n)) #"apes" => ['a','p','e','s'] => [1,2,3,4] => [21,22,23,24]

    return m1, m1_ciph

def decrypt(c,d,n):
    m2_chars = []

    for i in c:
        m2_chars.append(chr(pow(i,d,n))) # [21,22,23,24] => [1,2,3,4] => ['a','p','e','s']

    m2 = ''.join(m2_chars)
    return m2


if __name__ == '__main__':
    n, d = keygen()
    print(f"{n=}")
    print(f"{d=}")

    m1, c = encrypt(n)
    print(f"{m1=}")
    print(f"{c=}")

    m2 = decrypt(c,d,n)
    print(f"{m2=}")
    print(f"{m1==m2=}")







