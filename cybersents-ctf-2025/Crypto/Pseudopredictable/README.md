# Pseudopredictable

## Description

An RSA key was generated using a custom, deterministic algorithm that produces valid primes—no randomness, just pure number-theoretic trickery. Designed by the ever-smug Professor Hexman, who claims it's "uncrackable unless you're smarter than me,". Find the hidden primes, and break the encryption. Think you're up for it? Prove him wrong.

**Difficulty:** *Medium*

## Attachments

- [chal.py](./dist/chal.py)
- [out.txt](./dist/out.txt)

## Solution

This challenge uses an LCG (Linear Congruential Generator) to produce 256-bit prime numbers for generating the RSA modulus (`n`). A random `seed`, `mul` (multiplier), and `inc` (increment) are generated to initialize a custom LCG. Each LCG output is checked for primality and stored. Once 8 primes are generated, they are multiplied together to produce the modulus (`n`), which is then used to encrypt the flag.

The first three outputs from the LCG are provided. To retrieve the flag, we need to recover the initial state of the LCG, for which the three sample outputs are enough. LCGs are predictable if enough outputs are known. Our first goal is to recover the LCG parameters (`seed`, `mul`, `inc`) using the provided samples in `s`.

The formula used by the LCG to generate numbers is:

```
s[1] = (s[0] * m + c) mod n
```
where `m` is the multiplier and `c` is the increment.

We are given `s[1]`, `s[2]`, and `s[3]` (note that `s[0]`, the seed, needs to be recovered).

#### Step 1: Recover `m` (Multiplier)

irst, subtract `s[2]` from `s[3]` and `s[1]` from `s[2]`. Then multiply the results with the modular inverse of the second difference:

```
s[3] - s[2] = (s[2] * m + c) - (s[1] * m + c) mod n
s[3] - s[2] = (s[2] - s[1]) * m mod n
```

Thus, we can recover `m` as:

```
m = (s[3] - s[2]) * (s[2] - s[1])^(-1) mod n
```
where `^(-1)` represents the modular inverse.

#### Step 2: Recover `c` (Increment)

Once `m` is known, we can plug it into the LCG formula and solve for `c`:

```
s[2] = (s[1] * m + c) mod n
c = (s[2] - s[1] * m) mod n
```

#### Step 3: Recover `s[0]` (Seed)

Finally, using the first equation, we can solve for `s[0]`:

```
s[1] = (s[0] * m + c) mod n
s[1] - c = s[0] * m mod n
s[0] = (s[1] - c) * m^(-1) mod n
```

After recovering `seed`, `mul`, and `inc`, simply re-use the prime generation code (which checks LCG outputs for primality) to regenerate the original 8 primes. Multiply them together to reconstruct `n`, and use standard RSA decryption to recover the flag.

You can find the solving script here: [sol.py](sol.py)

Flag: *`flag{lcg_outputs_revealed_seed_computed_rsa_primes!!}`*

