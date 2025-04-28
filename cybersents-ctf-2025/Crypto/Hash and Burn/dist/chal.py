import os
import hashlib
from secret import MESSAGE

assert all([(c.isupper() or c in "{_} ") for c in MESSAGE])

salt = os.urandom(8)

def main():
	out_file = open("output.txt", "w")
	for c in MESSAGE:
		combined = salt + c.encode()
		sha1_hash = hashlib.sha1(combined).hexdigest()
		out_file.write(sha1_hash + "\n")

main()