# BabyXOR

## Description

Someone thought XOR with a repeating key would be enough to keep you out. Prove them wrong. The plaintext is English—assuming you’re smart enough to find it.

**Difficulty:** *Warm-up*

## Attachments

- [chal.py](./dist/chal.py)
- [out.txt](./dist/out.txt)

## Solution

This is a simple XOR challenge where the flag is XORed with a 6-byte secret key generated randomly.

To find the flag, we first need to retrieve the key. The first 5 bytes of the key can be retrieved by XORing the known first 5 characters of the flag, which are `flag{`, with the first 5 bytes of the encrypted flag.

We also know that the length of the flag is a multiple of 6, so the last character of the flag, which is `}`, overlaps with the 6th byte of the key in the cycle. XORing the last encrypted byte with `}` will give us the 6th byte of the key.

```
key[:5] = b"flag{" ^ enc_flag[:5]
key[6]  = b"}" ^ enc_flag[-1]    
```

Once the full key is recovered, simply XOR the entire encrypted flag with the key (repeating the key cyclically) to obtain the flag.

```
flag = key ^ enc_flag
```
You can find the solving script here: [sol.py](sol.py)

Flag: *`flag{x0r_th3_tru7h_fr0m_l13s!}`*