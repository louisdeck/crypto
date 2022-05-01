# Simple RSA implementation, not secure at all!

# (n,e) = public key
# (d) = private key

'''
p = 53
q = 59
e = 3
'''

'''
p = 1999 #2 prime numbers p and q
q = 2011
e = 65537 #exponent

n = p * q #modulo
phi = (p-1) * (q-1) #euler's totient
d = pow(e,-1,phi) #modular multiplicative inverse := e * d = 1 mod phi

m = 89 #plaintext message
c = pow(m, e, n) #encrypted message
m2 = pow(c, d, n) #unencrypted message

print(f"{m=}")
print(f"{c=}")
print(f"{m2=}")
print(f"{m == m2=}")
'''

e = 65537

def keygen():
	p = int(input("Choose a prime number p (1999): ") or 1999)
	q = int(input("Choose a prime number q (2011): ") or 2011)
	n = p * q
	phi = (p-1) * (q-1)
	d = pow(e,-1,phi)

	return n, d;

def encrypt(n):
	m1 = int(input("What message would you like to encrypt? "))
	c = pow(m1,e,n)
	return m1,c

def decrypt(c,d,n):
	m2 = pow(c,d,n)
	return m2


if __name__ == '__main__':
	n, d = keygen()
	#print(f"{n=}")
	#print(f"{d=}")

	m1, c = encrypt(n)
	print(f"{m1=}")
	print(f"{c=}")

	m2 = decrypt(c,d,n)
	print(f"{m2=}")
	print(f"{m1 == m2=}")








