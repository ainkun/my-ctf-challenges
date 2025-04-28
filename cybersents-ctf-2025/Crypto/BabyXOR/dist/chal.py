#!/usr/bin/python

import os

FLAG = "flag{************************}"
key = os.urandom(6)

def xor_data(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

print(bytes.hex(xor_data(FLAG.encode(), key)))