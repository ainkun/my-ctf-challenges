from Crypto.Util.number import isPrime, bytes_to_long
from secrets import randbits
from secret import FLAG

class LCG:
    n = (2**257)-1

    def __init__(self, seed, mul, inc):
        self.state = seed
        self.m = mul
        self.c = inc

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        return self.state


def main():
    seed = randbits(256)
    mul = randbits(256)
    inc = randbits(256)

    gen = LCG(seed, mul, inc)
    prime_array = []
    prime_modulus = 1

    sample = []

    i = 1
    while True:
        possible_prime = gen.next()
        if i <= 3:
            sample.append(possible_prime)
        if isPrime(possible_prime) and possible_prime.bit_length() == 256:
            prime_array.append(possible_prime)
            prime_modulus = prime_modulus * possible_prime
            if len(prime_array) == 8:
                break
        i = i+1

    #RSA encryption
    n = prime_modulus
    e = 0x10001
    
    m = bytes_to_long(FLAG.encode())
    ct = pow(m, e, n)

    out_file = open("out.txt", "w")
    out_file.write("s = " + str(sample) + "\n")
    out_file.write(f"n = {n}\n")
    out_file.write(f"e = {e}\n")
    out_file.write(f"ct = {ct}\n")

    out_file.close()



main()