# Simple RSA implementation, not secure at all!
# (n,e) = public key
# (d) = private key

# pub.key = n,e (-----BEGIN RSA PUBLIC KEY-----)
# priv.key = n,e,d,p,q,phi

# 1 digit =~ 3 bits
# on veut convertir une suite de bits en base 2 (0,1) en un nombre décimal (0-9) 
# le nombre de bits nécessaires pour écrire un nombre entre 0 et 9 est égal à log2(10) =~ 3.32

import sys

e = 65537
p2 = 49126743421046493081810883098374171184738027699278091635174896189529950024090319537029094953345730447686454341410189354858599774205220821398564195524527007
q2 = 61215577397189469335004731817479704516777274524561218761539090154890470929099997436735971472899220741279185814641192935849612556137005302696637363342316929


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def keygen():
    p = int(input("Choose a prime number p (1999): ") or 1999)
    q = int(input("Choose a prime number q (2011): ") or 2011)

    #p = p2
    #q = q2

    if(isPrime(p) and isPrime(q)):
        n = p * q
        phi = (p-1) * (q-1)
        d = pow(e,-1,phi)
        return n, d;

    else: sys.exit("2 primes required, exiting.")

def encrypt(n):
    m1_ciph = []

    with open('plaintext.txt', 'r') as f:
        m1 = f.read()
    f.close()

    for i in m1:
        m1_ciph.append(pow(ord(i), e, n)) #"apes" => ['a','p','e','s'] => [1,2,3,4] => [21,22,23,24]

    with open('cipher.txt', 'w') as f2:
        for i in m1_ciph:
            f2.write(str(i))
    f2.close()

    return m1, m1_ciph

def decrypt(c,d,n):
    m2_chars = []

    for i in c:
        m2_chars.append(chr(pow(i,d,n))) # [21,22,23,24] => [1,2,3,4] => ['a','p','e','s']

    m2 = ''.join(m2_chars)

    with open('output.txt', 'w') as f:
        f.write(m2)
    f.close()

    return m2


if __name__ == '__main__':
    n, d = keygen()
    print("keygen done...")

    #print(f"{n=}")
    #print(f"{d=}")

    print("encrypting plaintext file..")
    m1, c = encrypt(n)
    print("encryption done.")

    #print(f"{m1=}")
    #print(f"{c=}")

    print("decrypting cipher file..")
    m2 = decrypt(c,d,n)
    print("decryption done.")

    #print(f"{m2=}")
    print(f"{m1==m2=}")