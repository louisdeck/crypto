# Diffie-Hellman ELI5

p = 23 #modulus
g = 5 #base

a = 4 #alice's secret
b = 3 #bob's secret

A = pow(g,a,p)
B = pow(g,b,p)

s_a = pow(B,a,p) #shared secret
s_b = pow(A,b,p) #shared secret

print(f"{s_a=}")
print(f"{s_b=}")
print(f"{s_a == s_b=}")




