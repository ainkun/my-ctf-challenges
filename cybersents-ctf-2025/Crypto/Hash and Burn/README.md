# Hash and Burn

## Description

Description: Agent CipherStrike tried to be clever—too clever. Instead of encrypting a top secret message, they hashed it and now can’t remember what it said. Classic.

Now the agency’s in chaos, and you're their last hope. Recover the original message from a string of hashes before CipherStrike puts “Unbreakable Genius” to work.

**Difficulty:** *Medium*

## Attachments

- [chal.py](./dist/chal.py)
- [output.txt](./dist/output.txt)

## Solution

The code imports the `MESSAGE` externally, iterates through each character, adds a random salt, hashes it, and saves the results to an `output.txt` file.

Since a random salt is added to each character before hashing, it is not possible to brute-force individual characters directly.

The intended approach to retrieve the secret message is **frequency analysis**, because each character still consistently produces a different hash (despite the salt). By substituting each unique hash with a random letter and then applying to a frequency analysis tool like [quipqiup](https://quipqiup.com/), we can recover the original message.

However, before we can effectively apply frequency analysis, we must first identify the hashes corresponding to special characters like `{}`, spaces `" "`, and underscores `_`. Here's the method I followed:

1. **Identifying curly brackets `{}`:**
   - The cipher output with an open `{` and a close `}` will not repeat elsewhere.
   - The **first** special hash corresponds to `{` (opening bracket).
   - The **second** special hash corresponds to `}` (closing bracket).

2. **Identifying spaces `" "`:**
   - The format of the flag is typically `FLAG{.....}`.
   - If the hash *one step after* the closing bracket's hash matches the hash *five steps before* the opening bracket's hash, then that specific hash corresponds to a **space** `" "`.

3. **Identifying underscores `_`:**
   - If the hashes *between* the curly brackets do not match any hashes **outside** the brackets, those hashes likely correspond to **underscores** `_`.

4. **Substituting the rest:**
   - After substituting for `{}`, `}`, `" "`, and `_`, replace all remaining unique hashes with random uppercase letters (A-Z).

Once this preprocessing is done, the output of the script (`sol.py`) will map all hashes to provisional characters. Then, by pasting the provisional text into a frequency analysis tool like [quipqiup](https://quipqiup.com/), I can recover the correct message, thus obtaining the flag.

Flag: *`flag{overflowed_rsa_corrupted_it}`*

---

**Note:**  
The challenge inspiration is taken from the *Perfect Synchronization* challenge from *HTB Cyber Apocalypse 2023* CTF.

I have also written a detailed writeup on that challenge, which you can find [here](https://ainkun.medium.com/crypto-conspiracy-part-4-htb-ca-picoctf-2023-2480a39b264f).

