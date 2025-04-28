#!/usr/bin/python

from Crypto.Util.number import getPrime
from secret import FLAG

p = getPrime(128)
q = getPrime(128)
n = p*q
e = 0x10001

m = int(bytes.hex(FLAG.encode()),16)

assert m.bit_length() > n.bit_length()

ct = pow(m,e,n)

print(f"ct = {ct}")

print(f"n = {n}")
print(f"e = {e}")
