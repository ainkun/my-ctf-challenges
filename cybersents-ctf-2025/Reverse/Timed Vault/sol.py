vault_key =[]

# Part1

vault_key.append("1337")

# Part2

import hashlib

def md5Hash(data1, lic2):
    md5_obj = hashlib.md5()
    md5_obj.update(data1.encode()) 
    md5_obj.update(lic2.encode()) 
    digest = md5_obj.digest()
    
    return digest
hash1 = bytes.fromhex("F7 95 B9 14 E1 0A 41 CF 54 7A 98 13 C1 3E B7 38")


users = ["admin", "guest", "ainkun", "noob"]

for user in users:
    for num in range(1000,9999):
        if md5Hash(user, str(num)) == hash1:
            username = user
            vault_key.append(str(num))
            break



# Part3

p_keys = []

from z3 import *
s = Solver()
integers = [BitVec(f"a{i}", 8) for i in range(6)]
for i in range(6):
    s.add(integers[i] < 10)
    s.add(integers[i] > 0)
s.add(integers[0] + integers[1] == 13)
s.add(integers[2] - integers[3] == 2)
s.add( integers[4] * integers[4] == 9)
s.add( integers[5] % integers[3] == 3)
s.add( integers[1] * integers[0] == 36)
a = If(integers[4] == 4, BitVecVal(1, 8), BitVecVal(0, 8))
s.add(integers[2] != a)
print(s.check())
while s.check() == sat:
    model = s.model()
    key = []
    for i in range(6):
        key.append(str(model[integers[i]].as_long()))
    p_keys.append(''.join(key))
    s.add(Or([integers[i] != model[integers[i]] for i in range(6)]))



for k in p_keys:
    print(username + " " + vault_key[0] + "-" + vault_key[1] + "-" + k)