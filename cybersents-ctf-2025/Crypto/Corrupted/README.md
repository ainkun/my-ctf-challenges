# Corrupted

## Description

Alex decrypted the the flag but it came out corrupted. Something’s not right. Help Alex uncover the cause and retrieve the real flag.

**Difficulty:** *Easy*

## Attachments

- [chal.py](./dist/chal.py)
- [output.txt](./dist/output.txt)

## Solution

This is a simple RSA challenge — but with a slight twist.

To find the flag, you first need to **factor the modulus (`n`)**.  
Each prime factor of `n` has a bit length of **128 bits**.  
You can use [FactorDB](https://factordb.com) to find the prime factors of the modulus.

After factoring `n`, simply **decrypt** the ciphertext using the standard (textbook) RSA decryption formula.  
However, after decryption, you will notice the result looks like **random bytes** and **does not directly form the flag**.  
This is where the real challenge begins.

If you look back at the provided code, you'll notice this line:

```python
assert m.bit_length() > n.bit_length()
```

This tells us that the **original message (flag)** was **larger than the modulus (`n`)** before encryption.
Thus, before encrypting, the flag was effectively **reduced modulo `n`**:

```
flag > n
m = flag % n
```

This means that during decryption, we only recover `m`, which is `flag mod n`, not the full flag.

To recover the original flag, you need to find the correct multiple of `n` that was lost during modular reduction.

Since we know:

```
flag = m + i * n
```

for some integer `i ≥ 0`, you can run a loop, incrementing i, and check if `flag_candidate = m + i * n` results in a valid flag format.

You can find the solving script here: [sol.py](sol.py)

Flag: *`flag{overflowed_rsa_corrupted_it}`*