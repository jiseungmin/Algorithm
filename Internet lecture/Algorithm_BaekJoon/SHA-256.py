import hashlib

data = input()
print(hashlib.sha256(data.encode('utf8')).hexdigest())
