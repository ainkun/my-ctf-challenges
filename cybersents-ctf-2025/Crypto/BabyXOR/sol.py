known = "flag{}"

def xor_data(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])



enc = bytes.fromhex("96ae4b57cd2cc0b07544de67afb65845813cafa45800db0b9cf319439729")

key = xor_data(enc[:5],known.encode())
key = key + bytes([ord("}") ^ enc[-1]])
print(key)


print(xor_data(enc,key))