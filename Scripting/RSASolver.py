#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
from sympy import factorint

print("=== Simple RSA Solver ===")

n = int(input("n = "))
e = int(input("e = "))
c = int(input("c = "))

print("\n[+] Factoring n...")

factors = factorint(n)

if len(factors) != 2:
    print("[-] Gagal: n bukan hasil perkalian 2 prima yang mudah difaktorkan.")
    exit()

p, q = factors.keys()

print(f"[+] p = {p}")
print(f"[+] q = {q}")

phi = (p - 1) * (q - 1)

print(f"[+] phi = {phi}")

d = pow(e, -1, phi)

print(f"[+] d = {d}")

m = pow(c, d, n)

print(f"[+] Plaintext integer = {m}")

try:
    print(f"[+] Plaintext bytes = {long_to_bytes(m)}")
except:
    print("[-] Gagal convert ke bytes")
